# Generated by Django 4.0.4 on 2022-05-22 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0005_alter_wordmeaning_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordmeaning',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]