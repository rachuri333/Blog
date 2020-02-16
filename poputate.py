import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Realtime.settings')
import django
django.setup()
from Blog.models import *
from faker import Faker
fake = Faker()
def populate(n):
    for i in range(n):
        fAuthor=fake.name()
        fContent = fake.text()
        fTitle=fake.name()
        blog=post.objects.get_or_create(Author=fAuthor,Title=fTitle,Content=fContent)
populate(81)
