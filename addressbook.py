from PyQt5 import QtSql
from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase('testing.db')

class Addressbook(Model):
    name = CharField()

    class Meta:
        database = db








