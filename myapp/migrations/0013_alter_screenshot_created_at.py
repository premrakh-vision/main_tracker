# Generated by Django 4.2.4 on 2023-08-07 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_screenshot_screen_name_alter_user_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshot',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
    ]
