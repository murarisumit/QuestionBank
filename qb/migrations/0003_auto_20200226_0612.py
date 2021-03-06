# Generated by Django 3.0.3 on 2020-02-26 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qb", "0002_question_difficulty"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question", old_name="Difficulty", new_name="difficulty",
        ),
        migrations.AlterField(
            model_name="question",
            name="pub_date",
            field=models.DateTimeField(auto_now=True, verbose_name="date_published"),
        ),
    ]
