# Generated by Django 4.2.4 on 2023-08-09 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_screenshot_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshot',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]