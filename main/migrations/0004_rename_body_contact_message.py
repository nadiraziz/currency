# Generated by Django 4.0.5 on 2022-06-14 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='body',
            new_name='message',
        ),
    ]