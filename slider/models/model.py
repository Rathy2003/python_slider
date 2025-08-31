import datetime

from mongoengine import Document, StringField, DateTimeField, IntField
class Slider(Document):
    title = StringField()
    link = StringField()
    image = StringField()
    description = StringField()
    order = IntField()
    createdAt = DateTimeField(default=datetime.datetime.now)
    updatedAt = DateTimeField(default=datetime.datetime.now)