# Generated by Django 4.0.7 on 2024-03-13 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_alter_otp_code_alter_otp_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='code',
            field=models.IntegerField(default=916430),
        ),
    ]
