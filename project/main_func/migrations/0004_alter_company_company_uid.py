# Generated by Django 3.2.13 on 2023-12-05 05:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main_func', '0003_company_company_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_uid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
