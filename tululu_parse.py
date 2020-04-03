import requests
from pathvalidate import sanitize_filename
import os
import json
import argparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin
URL = 'http://tululu.org/l55/'


def get_response_text(response):
    if response.status_code == 200:
        return response.text
    else:
        print(f'Ошибка при загрузке страницы: {response.request.url}')
        return


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start_page', default=1, type=int)
    parser.add_argument('--end_page', default=3, type=int)
    parser.add_argument('--dest_folder', default='parse_tululu')
    parser.add_argument('--skip_imgs', action='store_true', default=True, help='Булевое значение True или False')
    parser.add_argument('--skip_txt', action='store_true', default=True, help='Булевое значение True или False')
    parser.add_argument('--json_path', default='books.json')
    return parser


def make_dirs(folder, args):
    path = os.path.join(args.dest_folder, folder)
    os.makedirs(path, exist_ok=True)
    return path


def download_txt(url, args, name_book):
    folder = make_dirs('books', args)
    url = urljoin(URL, url)
    response = requests.get(url)
    response_text = get_response_text(response)
    if not response_text:
        return
    path = os.path.join(folder, name_book)
    filepath = os.path.normpath(path)
    with open(filepath, 'wb') as file:
        file.write(response.content)
        return filepath


def download_image(img_link, img, args):
    folder = make_dirs('images', args)
    url = urljoin(URL, img_link)
    response = requests.get(url)
    response_text = get_response_text(response)
    if not response_text:
        return
    path = os.path.join(folder, img)
    filepath = os.path.normpath(path)
    with open(filepath, 'wb') as file:
        file.write(response.content)
        return filepath


def download_comments(args, id_book, comments):
    folder = make_dirs('comments', args)
    path = os.path.join(folder, f'{id_book}.txt')
    filepath = os.path.normpath(path)
    with open(filepath, 'wt', encoding='utf8') as file:
        for line in comments:
            file.write('%s\n' % line)


def get_info_book(link_book, args):
    response = requests.get(link_book)
    response_text = get_response_text(response)
    if not response_text:
        return
    soup = BeautifulSoup(response.text, 'lxml')
    card_tag = soup.select_one('body table.tabs td.ow_px_td')
    title_section = card_tag.select_one('h1').text.split('::')
    title = [title_element.strip("\xa0 ") for title_element in title_section]
    genres_section = card_tag.select_one('span.d_book').select('a')
    genres = [genres_element.text for genres_element in genres_section]
    comments_section = card_tag.select('div.texts')
    comments = [comment_element.select_one('span.black').text for comment_element in comments_section]
    img_link = card_tag.select_one('img')['src']
    img = img_link.split('/')[::-1][0]
    tag_tr = card_tag.select_one('table.d_book').select('tr')
    tag_a_all = [tag_element_tr.select_one('td').select('a') for tag_element_tr in tag_tr]
    tag_a = [tag_element for tag_element in tag_a_all if tag_element]
    name_book = ''
    for elem_a in tag_a:
        for tag in elem_a:
            if tag.text == 'скачать txt':
                link_txt = tag['href']
                id_book = tag['href'].split('=')[::-1][0]
                title_book = sanitize_filename(title[0])
                name_book = f'{id_book}. {title_book}'

    file_path_txt = ''
    file_path_img = ''
    if name_book and args.skip_txt:
        file_path_txt = download_txt(link_txt, args, name_book)
    if name_book and args.skip_imgs:
        file_path_img = download_image(img_link, img, args)
    if name_book:
        download_comments(args, id_book, comments)

    return {
        'title': name_book,
        'author': title[1],
        'img_src': file_path_img,
        'book_path': file_path_txt,
        'comments': comments,
        'genres': genres
    }


if __name__ == '__main__':
    books = []
    parser = get_parser()
    args = parser.parse_args()
    for page in range(args.start_page, args.end_page):
        url = urljoin(URL, f'{page}')
        response = requests.get(url)
        response_text = get_response_text(response)
        if not response_text:
            continue
        if response.history:
            break
        soup = BeautifulSoup(response.text, 'lxml')
        selector = "body table.tabs td.ow_px_td table.d_book"
        books_cards = soup.select(selector)
        for book_card in books_cards:
            link_book = urljoin(URL, book_card.find('a').get('href'))
            info_book = get_info_book(link_book, args)
            books.append(info_book)
    filepath = os.path.join(args.dest_folder, args.json_path)
    with open(filepath, 'w') as file:
        json.dump(books, file, ensure_ascii=False, sort_keys=True, indent=4)