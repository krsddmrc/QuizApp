# Generated by Django 4.0.5 on 2022-07-02 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0005_answer_question_quiz_remove_reservation_flight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Quiz name'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(max_length=64, verbose_name='Category'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.ManyToManyField(to='quizzes.question')),
            ],
        ),
    ]