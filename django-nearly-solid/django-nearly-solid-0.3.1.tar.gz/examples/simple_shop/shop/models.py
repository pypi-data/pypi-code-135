from django.db.models import Model, CharField, TextField, FloatField


class Product(Model):
    name = CharField(unique=True, max_length=128)
    description = TextField()
    price = FloatField()
