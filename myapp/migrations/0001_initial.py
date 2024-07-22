# Generated by Django 5.0.7 on 2024-07-19 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Phonenumber', models.IntegerField()),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity', models.CharField(max_length=50)),
                ('Priority', models.CharField(max_length=50)),
                ('Image', models.ImageField(upload_to='static/images')),
                ('Date', models.CharField(max_length=30)),
                ('Time', models.CharField(max_length=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='myapp.users')),
            ],
        ),
    ]