# Generated by Django 4.2 on 2023-05-01 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('univeristy', '0004_subcategory_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='logo',
        ),
    ]