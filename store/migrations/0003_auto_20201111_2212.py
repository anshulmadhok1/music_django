# Generated by Django 3.1.3 on 2020-11-11 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_auto_20201108_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='song',
            name='song',
            field=models.FileField(upload_to=store.models.upload_content_to),
        ),
    ]
