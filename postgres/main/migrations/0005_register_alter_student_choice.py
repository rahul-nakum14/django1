# Generated by Django 4.1.4 on 2023-01-19 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_course_dept_id_delete_dept'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('address', models.TextField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phonw', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='choice',
            field=models.CharField(choices=[('Subject 1', 'Data Science'), ('Subject 2', 'AI/ML'), ('Subject 3', 'Python')], default='Subject 2', max_length=100),
        ),
    ]
