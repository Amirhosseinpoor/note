# Generated by Django 5.1.2 on 2024-10-16 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_alter_notemodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notemodel',
            name='date',
            field=models.DateField(),
        ),
    ]
