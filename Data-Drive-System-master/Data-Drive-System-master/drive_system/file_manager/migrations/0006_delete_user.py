# Generated by Django 4.1.2 on 2023-10-11 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_manager', '0005_alter_folder_parent_folder'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
