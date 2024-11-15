from django.db.models import Model, CharField, IntegerField


# Create your models here.

class Book(Model):
    title = CharField(max_length=64)
    rating = IntegerField()