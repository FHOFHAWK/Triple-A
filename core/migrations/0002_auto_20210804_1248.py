# Generated by Django 3.2.6 on 2021-08-04 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='endTime',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='startTime',
            new_name='start_time',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='utlLesson',
            new_name='url_lesson',
        ),
    ]