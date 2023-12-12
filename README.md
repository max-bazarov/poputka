# Poputka

https://poputka.app/api/docs/


## Установка и локальный запуск
Склонируйте репозиторий на свой компьютер
- Измените файл .env.example на .env и заполните его
- Установите poetry для установки зависимостей `pip3 intstall poetry`
- Создайте виртуальное окружение `poetry shell` или `python3 -m venv env`
- Установите зависимости `poetry install`
- Запустите тесты `pytest -v`
- Убедитесь, что у вас установлен Docker и Docker Compose последних версий
- Перейдите в папку deploy
- Запустите проект командамой `docker-compose up --build`
- Проект доступен по адресу http://localhost/ 
