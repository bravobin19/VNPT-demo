# Generated by Django 4.0.3 on 2022-04-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employees_avatar_employees_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='age',
            field=models.DateField(null=True),
        ),
    ]
