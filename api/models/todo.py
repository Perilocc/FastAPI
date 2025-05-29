from tortoise.models import Model
from tortoise.fields import IntField, BooleanField, CharField


class Todo(Model):
    id = IntField(pk=True)
    task = CharField(max_lentgh=100, null= False)
    done = BooleanField(default=False)