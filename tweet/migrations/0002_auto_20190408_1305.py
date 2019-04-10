# Generated by Django 2.1.8 on 2019-04-08 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='who_follows', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]