# Generated by Django 2.2.8 on 2020-07-29 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_studentresult'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentresult',
            old_name='bord',
            new_name='board',
        ),
    ]
