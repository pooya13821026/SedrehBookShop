# Generated by Django 4.0.7 on 2024-03-13 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0014_remove_order_book_order_book_remove_order_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='book',
        ),
        migrations.AddField(
            model_name='order',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.book'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
