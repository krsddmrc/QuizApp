# Generated by Django 4.0.5 on 2022-07-03 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0006_alter_quiz_name_alter_quiz_slug_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='questions',
        ),
        migrations.AddField(
            model_name='category',
            name='quiz',
            field=models.ManyToManyField(to='quizzes.quiz'),
        ),
    ]