# Generated by Django 5.1.2 on 2024-12-26 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtwapa_branch', '0010_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
