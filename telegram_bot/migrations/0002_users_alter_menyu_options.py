# Generated by Django 4.2.13 on 2024-08-05 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Toliq ism: ')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Telfon nomr: ')),
                ('telegram_id', models.CharField(max_length=20, verbose_name='telegram id: ')),
                ('username', models.CharField(max_length=18, verbose_name='telegram username: ')),
            ],
            options={
                'verbose_name': 'Foydalanuvchilar royhati: ',
            },
        ),
        migrations.AlterModelOptions(
            name='menyu',
            options={'verbose_name': 'Taom tur', 'verbose_name_plural': 'Taom turlari'},
        ),
    ]