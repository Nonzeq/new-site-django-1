# Generated by Django 3.2.8 on 2021-11-15 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_comment_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='autor',
        ),
    ]
