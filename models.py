# No.2 start
from peewee import *
import datetime
DATABASE = SqliteDatabase('vocabs.sqlite')
class Vocab(Model):
    vocab_chinese = CharField(unique=True)
    vocab_english = CharField(unique=True)
    category = CharField()
    set = IntegerField()
    class Meta:
        database = DATABASE
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Vocab], safe=True)
    print('tables created')
    DATABASE.close()
