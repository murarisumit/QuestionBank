# Generated by Django 3.0.3 on 2020-02-25 11:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_name', models.CharField(max_length=64)),
                ('lang_code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('question_name', models.CharField(max_length=264)),
                ('pub_date', models.DateTimeField(verbose_name='date_published')),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='qb.Language')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='qb.Subject')),
            ],
            options={
                'unique_together': {('question_id', 'lang')},
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=64)),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='qb.Language')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qb.Question')),
            ],
        ),
    ]
