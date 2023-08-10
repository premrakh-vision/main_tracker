# Generated by Django 4.2.4 on 2023-08-09 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_screenshot_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventOff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pre_off_time', models.DateTimeField()),
                ('post_off_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]