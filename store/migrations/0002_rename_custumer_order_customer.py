# Generated by Django 5.1.1 on 2024-09-17 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='custumer',
            new_name='customer',
        ),
    ]