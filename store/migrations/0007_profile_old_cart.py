# Generated by Django 5.1.2 on 2024-10-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='old_cart',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
