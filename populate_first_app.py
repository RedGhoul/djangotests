# Need to do the following so that we can use the Django ORM
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','tutorialSite.settings')

import django

django.setup()

## Fake Pop Script

import random
from first_app.models import AccessRecord,Webpage,Topic,User
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace', 'News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

        new_user = User.objects.get_or_create(
            last_name=fakegen.name(), first_name=fakegen.name(), email=fakegen.company_email())

if __name__ == '__main__':
    print("Populate Running")
    populate(200)
    print("Populate Finished")