# 启动服务器
```shell
python ./suplerlists/manage.py runserver
```
# 测试
处于`suplerlists`目录下
## 功能测
```shell
python manage.py test functional_tests
```
单元测
```shell
python manage.py test
```
# 数据库
## 数据库迁移
```shell
python manage.py makemigrations
```
## 数据库建立
```shell
python manage.py migrate --noinput
```