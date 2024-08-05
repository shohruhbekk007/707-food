from django.db import models
from django.contrib.auth.models import User, Group



# Create your models here.

class Menyu(models.Model):
    taom_turi = models.CharField(max_length=30, verbose_name="taam turi")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taom_turi

    class Meta:
        verbose_name = 'Taom tur'
        verbose_name_plural = verbose_name + 'lari'

class Taomlar(models.Model):
    taom_tur = models.ForeignKey(to=Menyu, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=30, verbose_name="nomini kiriting: ")
    narxi = models.BigIntegerField(verbose_name="narxi: ")
    rasm = models.ImageField(verbose_name="taom rasmi: ", upload_to="taomlar/rasm")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = 'Taom'
        verbose_name_plural = verbose_name + 'lar'

class ComandStart(models.Model):
    title = models.CharField(max_length=255, verbose_name="dastlabki text: ")
    discreiption = models.TextField()
    image = models.ImageField(upload_to="Rasm")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Asosiy sahifa'

class Users(models.Model):
    title = models.CharField(verbose_name="Toliq ism: ", max_length=60)
    phone_number = models.CharField(verbose_name="Telfon nomr: ", max_length=20)
    telegram_id = models.CharField(max_length=20, verbose_name="telegram id: ")
    username = models.CharField(max_length=18, verbose_name="telegram username: ")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = verbose_name + 'lar'