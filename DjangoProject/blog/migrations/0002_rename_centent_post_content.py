# Generated by Django 5.1.4 on 2024-12-20 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='centent',
            new_name='content',
        ),
    ]
