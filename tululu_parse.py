import requests
from pathvalidate import sanitize_filename
import os
import json
import argparse
from bs4 import BeautifulSoup
URL = 'http://tululu.org'


def checking_the_status(response):
    try:
        response.raise_for_status()
    except Exception as error:
        print('Ошибка при загрузке страницы: ' + str(error))


def get_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start_page', default=2, type=int)
    parser.add_argument('--end_page', default=3, type=int)
    parser.add_argument('--dest_folder', default='parse_tululu')
    parser.add_argument('--skip_imgs', action='store_true', default=True, help='Булевое значение True или False')
    parser.add_argument('--skip_txt', action='store_true', default=True, help='Булевое значение True или False')
    parser.add_argument('--json_path', default='description_of_books.json')
    return parser.parse_args()


def create_or_update_folder(folder, args):
    path = os.path.join(args.dest_folder, folder)
    os.makedirs(path, exist_ok=True)
    return path


def download_txt(url, args, name_book):
    folder = create_or_update_folder('books', args)
    url = os.path.join(f'{URL}{url}')
    response = requests.get(url)
    checking_the_status(url, response)
    if not response.history:
        path = os.path.join(folder, name_book)
        filepath = os.path.normpath(path)
        with open(filepath, 'wb') as file:
            file.write(response.content)

            return filepath


def download_image(img_link, img, args):
    folder = create_or_update_folder('images', args)
    response = requests.get(f'{URL}{img_link}')
    checking_the_status(url, response)
    path = os.path.join(folder, img)
    filepath = os.path.normpath(path)
    with open(filepath, 'wb') as file:
        file.write(response.content)

        return filepath


def download_comments(args, id_book, comments):
    folder = create_or_update_folder('comments', args)
    path = os.path.join(folder, f'{id_book}.txt')
    filepath = os.path.normpath(path)
    with open(filepath, 'wt', encoding='utf8') as file:
        for line in comments:
            file.write('%s\n' % line)


def get_info_book(link_book, args):
    response = requests.get(link_book)
    checking_the_status(url, response)
    if not response.history:
        soup = BeautifulSoup(response.text, 'lxml')
        selector = 'body table.tabs td.ow_px_td'
        card_tag = soup.select_one(selector)
        title_section = card_tag.find('h1').text.split('::')
        title = [title_element.strip("\xa0 ") for title_element in title_section]
        genres_section = card_tag.find('span', class_='d_book').find_all('a')
        genres = [genres_element.text for genres_element in genres_section]
        comments_section = card_tag.find_all('div', class_='texts')
        comments = [comment_element.find('span', class_='black').text for comment_element in comments_section]
        img_link = card_tag.find('img')['src']
        img = img_link.split('/')[::-1][0]
        tag_tr = card_tag.find('table', class_='d_book').find_all('tr')
        tag_a_all = [tag_element_tr.find('td').find_all('a') for tag_element_tr in tag_tr]
        tag_a = [tag_element for tag_element in tag_a_all if tag_element]
        name_book = ''
        for elem_a in tag_a:
            for tag in elem_a:
                if tag.text == 'скачать txt':
                    link_txt = tag['href']
                    id_book = tag['href'].split('=')[::-1][0]
                    name_book = f'{id_book}. {sanitize_filename(title[0])}'

        file_path_txt = ''
        file_path_img = ''
        if name_book:
            if args.skip_txt:
                file_path_txt = download_txt(link_txt, args, name_book)
            if args.skip_imgs:
                file_path_img = download_image(img_link, img, args)
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
    description_of_books = []
    args = get_args_parser()
    for page in range(args.start_page, args.end_page):
        url = f'{URL}/l55j/{page}'
        response = requests.get(url)
        checking_the_status(response)
        if not response.history:
            soup = BeautifulSoup(response.text, 'lxml')
            selector = "body table.tabs td.ow_px_td table.d_book"
            books_cards = soup.select(selector)
            for book_card in books_cards:
                link_book = os.path.join(f'''{URL}{book_card.find('a').get('href')}''')
                info_book = get_info_book(link_book, args)
                description_of_books.append(info_book)
    filepath = os.path.join(args.dest_folder, args.json_path)
    with open(filepath, 'w') as file:
        json.dump(description_of_books, file, ensure_ascii=False, sort_keys=True, indent=4)