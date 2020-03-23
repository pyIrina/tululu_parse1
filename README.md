# Сайт - http://tululu.org

## Программа скачивает книги с сайта http://tululu.org, жанр - фантастика.

## Окружающая обстановка

### Требования

Должен быть установлен Python3.

## Аргументы для запуска

* ```--start_page``` - начальная страница
    * ```python tululu_parse.py --start_page 10```

* ```--end_page``` - последняя страница
    * ```python tululu_parse.py --end_page 20```

* ```--dest_folder``` - основная папка хранения данных, по умолчанию - 'parse_tululu'
    * ```python tululu_parse.py --dest_folder 'Название_папки'```

* ```--skip_imgs``` - не скачивать картинки
    * ```python tululu_parse.py --skip_imgs False```

* ```--skip_txt``` - не скачивать книги
    * ```python tululu_parse.py --skip_txt False```

* ```--json_path``` - имя файла JSON, для хранении информации о всех книгах, по умолчанию - 'description_of_books.json'
     * ```python tululu_parse.py --json_path 'Название_файла.json'```

## Запуск

Запустите на Linux(Python 3) или Windows:

``` bash python tululu_parse.py ```


### Вы увидите:

* ./parse_tululu/books
     * id. Название_книги.txt

* ./parse_tululu/images
     * id.jpg

* ./parse_tululu/comment
     * id.txt

* ./parse_tululu/books.json
