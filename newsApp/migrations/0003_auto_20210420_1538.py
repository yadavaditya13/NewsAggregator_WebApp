# Generated by Django 3.1.2 on 2021-04-20 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0002_headline_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headline',
            name='id',
        ),
        migrations.AlterField(
            model_name='headline',
            name='title',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]