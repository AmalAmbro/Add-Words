# Generated by Django 4.0.4 on 2022-05-22 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0007_alter_words_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='words',
            options={'verbose_name_plural': 'Words'},
        ),
    ]
