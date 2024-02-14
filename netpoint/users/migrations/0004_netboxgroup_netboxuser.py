# Generated by Django 4.1.9 on 2023-06-06 18:15

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0003_token_allowed_ips_last_used'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetPointGroup',
            fields=[],
            options={
                'verbose_name': 'Group',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='NetPointUser',
            fields=[],
            options={
                'verbose_name': 'User',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='netpointgroup',
            options={'ordering': ('name',), 'verbose_name': 'Group'},
        ),
        migrations.AlterModelOptions(
            name='netpointuser',
            options={'ordering': ('username',), 'verbose_name': 'User'},
        ),
    ]
