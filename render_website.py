import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
# from livereload.server import Server, shell
from http.server import HTTPServer, SimpleHTTPRequestHandler
import math


def create_index_html(page=1):
    with open("static/books.json", "r", encoding='utf-8') as my_file:
        books_json = my_file.read()
    books = json.loads(books_json)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template/template.html')

    for i in range(1, len(books), 10):
        books_info = books[i:i + 10]
        paginate_by = math.ceil(len(books) / 10)
        rendered_page = template.render(
            books_info=books_info,
            page=page,
            paginate_by=paginate_by
        )
        if page == 1:
            filepath = f'pages/index.html'
        else:
            filepath = f'pages/index{page}.html'
        with open(filepath, 'w', encoding="utf8") as file:
            file.write(rendered_page)
        page += 1


def on_reload(port=5500):
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
    # server = Server()
    # server.watch('template/*.html')
    # server.serve(port=port)


def main():
    create_index_html()
    on_reload()


if __name__ == "__main__":
    main()
