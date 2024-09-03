# Generated by Django 4.1 on 2023-09-08 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RApp', '0020_alter_property_propsoldto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role_type',
            field=models.CharField(choices=[('0', 'Guest'), ('1', 'Buyer'), ('2', 'Seller'), ('3', 'Deny')], default='0', max_length=5),
        ),
        migrations.AlterField(
            model_name='user',
            name='role_type_appl',
            field=models.CharField(choices=[('0', 'Guest'), ('1', 'Buyer'), ('2', 'Seller'), ('3', 'Deny')], default='0', max_length=5),
        ),
    ]
