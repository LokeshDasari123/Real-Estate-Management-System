# Generated by Django 4.1 on 2023-08-27 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RApp', '0003_remove_seprofile_sellcerti'),
    ]

    operations = [
        migrations.AddField(
            model_name='seprofile',
            name='sellcerti',
            field=models.FileField(blank=True, null=True, upload_to='Certificates/'),
        ),
    ]