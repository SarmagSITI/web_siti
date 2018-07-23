# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-29 04:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('wanita', 'Wanita'), ('pria', 'Pria')], default='pria', max_length=10)),
                ('instagram', models.CharField(blank=True, max_length=50, null=True)),
                ('facebook', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('hide_phone', models.BooleanField(default=False)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('hide_email', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/userprofile')),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]