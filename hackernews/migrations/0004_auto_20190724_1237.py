# Generated by Django 2.2.3 on 2019-07-24 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackernews', '0003_auto_20190724_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='profile.jpg', null=True, upload_to='static/images'),
        ),
    ]