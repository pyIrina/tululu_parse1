# Парсер сайта - tululu.org

Программа скачивает книги с сайта - tululu.org.

Жанр - фантастика.

## Требования

Должен быть установлен Python3 на Linux или Windows.

## Запуск

###### Аргументы для запуска в консоле:

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

###### Команда для запуска парсера в консоле:

``` bash python tululu_parse.py ```


### После запуска

Итогом работы парсера мы получим каталог - ```/parse_tululu```

Структура каталога:

* ```/books``` - Каталог с книгами
  * ``` 1.Взгляд из сердца.txt```
  * ``` 2.Звездный зверь ( Звездное чудовище).txt```
  * ``` 3.Сборник рассказов и повестей.txt```

* ```/images``` - Каталог с обложками книг
  * ```1.jpg```
  * ```2.jpg```
  * ```3.jpg```

* ```/comments``` - Каталог с комментариями книг
  * ```1.txt```
  * ```2.txt```
  * ```3.txt```
  
* ```books.json``` - Файл описания книг  
