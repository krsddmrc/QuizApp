# Generated by Django 4.0.5 on 2022-07-02 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizzes', '0003_rename_quiz_name_quiz_quiz_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=20)),
                ('operation_airlines', models.CharField(max_length=15)),
                ('departure_city', models.CharField(max_length=30)),
                ('arrival_city', models.CharField(max_length=30)),
                ('date_of_departure', models.DateField()),
                ('etd', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='quizzes.flight')),
                ('passenger', models.ManyToManyField(related_name='reservations', to='quizzes.passenger')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
    ]