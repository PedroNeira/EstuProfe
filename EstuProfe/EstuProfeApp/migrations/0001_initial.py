# Generated by Django 4.0.6 on 2022-07-21 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicationDate', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(auto_now_add=True)),
                ('area', models.CharField(max_length=32)),
                ('description', models.TextField(max_length=100)),
                ('isAccepted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tutorship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userTutorId', models.IntegerField()),
                ('userStudentId', models.IntegerField()),
                ('tutorShipDate', models.DateTimeField()),
                ('hour', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=32)),
                ('lastName', models.CharField(max_length=32)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(max_length=30)),
                ('phoneNumber', models.IntegerField()),
                ('educationLevel', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]
