from mongoengine import *


class Contacts(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    sent = BooleanField(required=True, default=False)
