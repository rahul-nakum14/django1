# Generated by Django 4.1.4 on 2023-02-20 16:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_userprofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Userprofile',
            new_name='user_profile',
        ),
    ]
