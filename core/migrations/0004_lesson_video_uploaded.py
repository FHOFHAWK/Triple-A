# Generated by Django 3.2.6 on 2021-08-05 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_lesson_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='video_uploaded',
            field=models.BooleanField(default=False),
        ),
    ]
