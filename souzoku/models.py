from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.

class StatusType(models.Model):
    name = models.CharField(max_length=10)

class LetterType(models.Model):
    name = models.CharField(max_length=10)

class Client(models.Model):
    name = models.CharField(max_length=30)

class Decedent(models.Model):
    name = models.CharField(max_length=100, help_text="被相続人名")
    name_kana = models.CharField(max_length=100, help_text="被相続人名カナ")
    manage_number = models.CharField(max_length=8, help_text="管理番号")
    store_number = models.CharField(max_length=3, help_text="部店コード")
    account_number = models.CharField(max_length=7, help_text="口座番号")
    post_code = models.CharField(max_length=8, help_text="郵便番号")
    address = models.CharField(max_length=100, help_text="住所")
    death_date = models.DateField(help_text="死亡日")
    recognition_date = models.DateField(help_text="死亡認知日")

class Successor(models.Model):
    decedent = models.ForeignKey(Decedent, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)

class RepresentSuccessor(models.Model):
    decedent = models.OneToOneField(Decedent,on_delete=models.CASCADE)
    successor = models.OneToOneField(Successor, on_delete=models.CASCADE)

class Status(models.Model):
    decedent = models.ManyToManyField(Decedent)
    status_type = models.ManyToManyField(StatusType)
    last_date = models.DateField()

class Letter(models.Model):
    decedent = models.ForeignKey(Decedent, on_delete=models.PROTECT)
    addressee_name = models.CharField(max_length=100)
    post_code = models.CharField(max_length=8)
    address = models.CharField(max_length=100)
    is_deficiency = models.BooleanField()
    letter_type = models.ManyToManyField(LetterType)
    output_date = models.DateField()
    send_date = models.DateField(null=True)

class ReturnInLetter(models.Model):
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

class DeficiencyInLetter(models.Model):
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)