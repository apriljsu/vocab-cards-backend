# No.2 start
from peewee import *
import datetime

# No. 4 starts : import usermixin for user model
from flask_login import UserMixin


#No.2 continue: set up vocabs model
DATABASE = SqliteDatabase('vocabs.sqlite')

#No. 5 start: set up user model
class User(UserMixin, Model):   
    email = CharField(unique = True)
    password = CharField()
    first_name = CharField()
    last_name = CharField()    
    class Meta:
        database = DATABASE

#No.2 continue
class Vocab(Model):
    vocab_chinese = CharField(unique=True)
    vocab_english = CharField(unique=True)
    category = CharField()
    english_to_chinese = BooleanField()
    user = ForeignKeyField(User, backref='vocabs')#7 link user to vocab
    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Vocab, User], safe=True)
    print('tables created')
    DATABASE.close()
