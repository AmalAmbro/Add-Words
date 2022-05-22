# Generated by Django 4.0.4 on 2022-05-21 12:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WordMeaning',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('meaning', models.CharField(max_length=100)),
                ('priority', models.IntegerField()),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.words')),
            ],
        ),
    ]