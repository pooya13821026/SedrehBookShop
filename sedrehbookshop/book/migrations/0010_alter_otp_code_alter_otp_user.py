# Generated by Django 4.0.7 on 2024-03-13 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0009_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='code',
            field=models.IntegerField(default=408190),
        ),
        migrations.AlterField(
            model_name='otp',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]