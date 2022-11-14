# No.2 start
from peewee import *
import datetime

# No. 4 starts
from flask_login import UserMixin


#No.2 continue
DATABASE = SqliteDatabase('vocabs.sqlite')
class User(UserMixin, Model):
    username = CharField(unique = True)
    email = CharField(unique = True)
    password = CharField()
    first_name = CharField()
    last_name = CharField()
    class Meta:
        database = DATABASE

class Vocab(Model):
    vocab_chinese = CharField(unique=True)
    vocab_english = CharField(unique=True)
    category = CharField()
    set = IntegerField()
    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Vocab, User], safe=True)
    print('tables created')
    DATABASE.close()
