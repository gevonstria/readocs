# Generated by Django 4.2.9 on 2024-02-24 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='upload',
            field=models.FileField(default=2, upload_to='swaggerfiles/'),
            preserve_default=False,
        ),
    ]
