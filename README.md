
# Пульт охраны банка

Настоящий репозиторий - это пример сайта охраны банка, подключаемого к удаленной базе данных (БД).

>Вы **не сможете** запустить данный репозиторий, т. к. у Вас нет доступа к БД, однако можете свободно использовать код верстки или ознакомиться с реализацией запросов к БД.

Сайт отображает число активных карт доступа в хранилище и список пользователей активных карт доступа в хранилище с указанием кодов карт пропуска и дат регистрации карт пропуска. 
При переходе по ссылке `Список пользователей в хранилище` отображается *список всех владельцев* пропусков, находящихся в хранилище в настоящий момент с указанием *длительности пребывания* в хранилище и *подозрительности* визита, определяемой исходя из длительности пребывания в хранилище.
При нажатии на имя владельца пропуска отображается *список всех посещений* хранилища данным пользователем с указанием *продолжительности* визита и *подозрительности* визита, определяемой в зависимости от проведенного в хранилище времени. 


### Как установить

Для запуска репозитория требуются переменные окружения в виде файла `project/login_data.env` с содержимым следующего вида:

- `DB_ENGINE` = движок БД (в данном случае `PostgreSQL` с драйвером `Psycopg2`);
- `DB_HOST` = хост БД;
- `DB_PORT` = порт БД. По умолчанию равно '' (пустая строка);
- `DB_NAME` = имя базы данных, для sqlite - путь к БД;
- `DB_USER` = имя пользователя По умолчанию равно ''(пустая строка);
- `DB_PASSWORD` = пароль. По умолчанию равно ''(пустая строка);
- `SECRET_KEY` = Секретный ключ Django. Используется для управления сеансами, подписи данных и хеширования паролей;
- `DEBUG` = Использование встроенного режима отладки Django;
- `ALLOWED_HOSTS` = Список строковых имен хостов/доменов, которые может обслуживать этот сайт.

Пример переменных окружения приведен в `example.txt`

Python3 должен быть уже установлен. 

Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
