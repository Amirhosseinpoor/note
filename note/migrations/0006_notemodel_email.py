# Generated by Django 5.1.2 on 2024-10-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_alter_notemodel_options_notemodel_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notemodel',
            name='email',
            field=models.EmailField(default=1, max_length=255),
        ),
    ]
