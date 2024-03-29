# 0x0F. Python - Object-relational mapping
## 'Python' 'OOP' 'SQL' 'MYSQL' 'ORM' 'SQLAlchemy'

# Before you start…
Please make sure your MySQL server is in 8.0 -> [https://intranet.alxswe.com/rltoken/paGukker_0KoG3D9FqymNQ]

## Background Context
* In this project, you will link two amazing worlds: Databases and Python!

* In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

* In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

* The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
* Why Python programming is awesome
* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table
* How to create a Python Virtual Environment
## Resources
Read or watch:

* Object-relational mappers [https://intranet.alxswe.com/rltoken/a8DUOWhXpNX3TEwgyT-U8A]
* mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql) [https://intranet.alxswe.com/rltoken/JtFaKjnqxudr6Hi05Us1Lw]
* MySQLdb tutorial [https://intranet.alxswe.com/rltoken/TdUSYFNGbXJG1WjCEoq5FA]
* SQLAlchemy tutorial [https://intranet.alxswe.com/rltoken/YyL5hsscviNH04XGW-XpfA]
* SQLAlchemy [https://intranet.alxswe.com/rltoken/j9azWF2Db_2rNolTxOF3SA]
* mysqlclient/MySQLdb [https://intranet.alxswe.com/rltoken/0zLhY9KqKjn-zmdb7X598Q]
* Introduction to SQLAlchemy [https://intranet.alxswe.com/rltoken/pw50Bl1Bj84wksxm018dwA]
* Flask SQLAlchemy [https://intranet.alxswe.com/rltoken/B-xIdMtGvpus8vHxAIRrPg]
* 10 common stumbling blocks for SQLAlchemy newbies[https://intranet.alxswe.com/rltoken/deIzPMrfK8Ixqm-AboFHWg]
* Python SQLAlchemy Cheatsheet [https://intranet.alxswe.com/rltoken/dZfUNK3lJicGMK5PU0bE7Q]
* SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL) [https://intranet.alxswe.com/rltoken/hNxBKC8lHge5XjsRO8ksHQ]
* SQLAlchemy Tutorial[https://intranet.alxswe.com/rltoken/5G_R2NmQRFqiZb84qxYERQ]
* Python Virtual Environments: A primer [https://intranet.alxswe.com/rltoken/OXle6kXpmD88D0WbgbTWqg]

# More Info
## Install and activate venv
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate

## Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04

$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)

## Install SQLAlchemy module version 1.4.x
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
