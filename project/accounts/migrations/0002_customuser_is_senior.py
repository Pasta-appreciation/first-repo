# Generated by Django 3.2.13 on 2023-11-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_senior',
            field=models.BooleanField(default=False),
        ),
    ]