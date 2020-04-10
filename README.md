# Парсер сайта - tululu.org

Программа скачивает книги с сайта - [tululu](https://tululu.org).
Жанр - фантастика.

## Требования

Должен быть установлен Python3 на Linux или Windows.

#### Установка

##### На Linux

1.Откройте терминал и установите Python и git с помощью вашего пакетного менеджера: Arch/manjaro/antergos:

```pacman -S git python --needed```

Ubuntu/Debian/Deepin/any_apt_based:

 ```apt install git python```

Fedora:

 ```yum install git python```
 
2.Склонируйте репозиторий при помощи git и перейдите в папку:
```
git clone https://github.com/emez3siu/b0mb3r.github.io
cd b0mb3r
```

3.Установите зависимости:

```python -m pip install -r requirements.txt```

4.Запустите ПО:

```python main.py```

5.Если в вашем браузере не открылся веб-интерфейс, перейдите по ссылке в терминале.

##### На Windows

1.Установите Python версии не ниже 3.6, скачав установщик с официального сайта.

2.Установите git для Windows, скачав его отсюда.

3.Откройте командную строку и склонируйте репозиторий при помощи git и перейдите в папку:
```
git clone https://github.com/emez3siu/b0mb3r.github.io
cd b0mb3r
```

4.Установите все необходимые библиотеки и запустите скрипт:
```
python -m pip install -r requirements.txt
python main.py
```

5.Если в вашем браузере не открылся веб-интерфейс, перейдите по ссылке в консоли.

## Запуск

###### Аргументы для запуска в консоле:

* ```--start_page``` - начальная страница
    * ```python main.py --start_page 10```

* ```--end_page``` - последняя страница
    * ```python main.py --end_page 20```

* ```--dest_folder``` - основная папка хранения данных, по умолчанию - 'static'
    * ```python main.py --dest_folder 'Название_папки'```

* ```--skip_imgs``` - не скачивать картинки
    * ```python main.py --skip_imgs False```

* ```--skip_txt``` - не скачивать книги
    * ```python main.py --skip_txt False```

* ```--json_path``` - имя файла JSON, для хранении информации о всех книгах, по умолчанию - 'description_of_books.json'
     * ```python main.py --json_path 'Название_файла.json'```

###### Команда для запуска парсера в консоле:

``` bash python main.py ```


### После запуска

Итогом работы парсера мы получим каталог - ```/static```

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
