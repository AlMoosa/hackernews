# Generated by Django 2.2.3 on 2019-07-24 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackernews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
    ]
