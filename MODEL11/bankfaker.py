import os
os.environ.setdefault('DJANGO_SETTING_MODULE', 'MODEL11.settings')
import django
django.setup()
from first.models import BankAccount
from faker import Faker
fake = Faker()
def populate(n):
    for i in range(n):
        ano = fake.random_int(min = 100, max = 999)
        name = fake.name()
        add = fake.address()
        bankaccount_record = BankAccount.objects.create(ano=ano,name=name,add=add)
populate(20)