启动服务器
```shell
python ./suplerlists/manage.py runserver
```
功能测
```shell
python functional_tests.py
```
单元测
处于`suplerlists`目录下
```shell
python manager.py test
```
数据库迁移
```shell
python manage.py makemigrations
```
数据库建立
```shell
python manage.py migrate --noinput
```