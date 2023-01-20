# Generated by Django 4.1.4 on 2023-01-18 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_name', models.CharField(max_length=100)),
                ('course_id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dept')),
            ],
        ),
    ]
