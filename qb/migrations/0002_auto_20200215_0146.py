# Generated by Django 3.0.3 on 2020-02-15 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qb', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('question_id', 'lang')},
        ),
    ]