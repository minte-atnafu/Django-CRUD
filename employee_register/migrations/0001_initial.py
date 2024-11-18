# Generated by Django 5.1.2 on 2024-11-18 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('emp_code', models.CharField(max_length=3)),
                ('phone_number', models.CharField(max_length=15)),
                ('postion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_register.postion')),
            ],
        ),
    ]