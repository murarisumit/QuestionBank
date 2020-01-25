# Generated by Django 3.0.2 on 2020-01-21 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qb', '0003_auto_20200116_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='qb.Question'),
        ),
        migrations.CreateModel(
            name='QuestionsInMultipleLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=264)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='qb.Question')),
                ('question_language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='qb.Language')),
            ],
        ),
    ]
