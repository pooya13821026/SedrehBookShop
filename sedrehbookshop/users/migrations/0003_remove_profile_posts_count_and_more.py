# Generated by Django 4.0.7 on 2024-03-11 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='posts_count',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='subscriber_count',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='subscription_count',
        ),
    ]