# Generated by Django 4.0.6 on 2022-11-30 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_lesson_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='Lesson_name',
            new_name='Lesson',
        ),
    ]
