import datetime

from mongoengine import Document, StringField, DateTimeField

class Slider(Document):
    title = StringField(max_length=100)
    link = StringField(max_length=255)
    image = StringField(max_length=255)
    createdAt = DateTimeField(default=datetime.datetime.now)
    UpdatedAt = DateTimeField(default=datetime.datetime.now)