# Описание проекта
  Это учебный проект на базе фреймворка **FastAPI**. 

  QRKot — приложение для Благотворительного фонда поддержки котиков.
  Фонд собирает пожертвования на различные целевые проекты: на медицинское 
  обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в 
  подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные 
  с поддержкой кошачьей популяции :)
  
 
# Запуск проекта
  1) Клонировать репозиторий:
    ```
    git clone https://github.com/mkmmcvrs68/cat_charity_fund
    ```
  2) Cоздать виртуальное окружение:

    ```
    python3 -m venv venv
    или 
    python -m venv venv (Windows)
    ```
  3) Активировать виртуальное окружение:
    ```
    source venv/bin/activate
    или
    source venv/scripts/activate (Windows)
    ```

  4) Установить зависимости из файла requirements.txt:
    ```
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
  5) Создать и заполнить файл .env по примеру из .env.example:
    ```
    touch .env
    ```
  6) Применение миграций:
    ```
    alembic upgrade head
    ```
  7) Запуск проекта:
    ```
    uvicorn app.main:app --reload
    ```

# Проект и документация
  Локальный доступ к API: http://127.0.0.1:8000
  Автоматически сгенерированная документация Swager: http://127.0.0.1:8000/docs


# Стек технологий:
  * Python 3.9.10
  * FastAPI 0.78.0
  * SQLAlchemy 1.4.36
  * Uvicorn[standart] 0.17.6
  * Alembic 1.7.7
  * Pydantic 1.9.1

> В проекте используется **Python** версии **3.9**
</details>

<details>
    <summary>
        <b>Установите зависимости из файла <code>requirements.txt</code></b>
    </summary>

```shell
pip install -r requirements.txt
```
</details>

<details>
    <summary><b>Примените миграции</b></summary>

```shell
alembic upgrade head
```
</details>

<details>
    <summary><b>Запустите программу</b></summary>

```shell
uvicorn app.main:app --reload
```
> По-умолчанию приложение запускается на 8000 порту, но вы можете изменить 
> порт: `--port 8001`
</details>

# Автор
  [Ермаков Владислав](https://github.com/Vladislav199912)
  vladermakov@mail.ru