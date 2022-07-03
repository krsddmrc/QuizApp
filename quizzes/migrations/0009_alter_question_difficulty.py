# Generated by Django 4.0.5 on 2022-07-03 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0008_question_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[('E', 'EASY'), ('M', 'MIDDLE'), ('H', 'HARD'), ('VH', 'VERYHARD')], max_length=2),
        ),
    ]
