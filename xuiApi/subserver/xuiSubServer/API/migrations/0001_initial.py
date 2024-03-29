# Generated by Django 4.1.7 on 2023-02-19 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientTraffics',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('inbound_id', models.TextField()),
                ('enable', models.TextField()),
                ('email', models.TextField()),
                ('up', models.TextField()),
                ('down', models.TextField()),
                ('expiry_time', models.TextField()),
                ('total', models.TextField()),
            ],
            options={
                'db_table': 'client_traffics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InboundClientIps',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client_email', models.TextField()),
                ('ips', models.TextField()),
            ],
            options={
                'db_table': 'inbound_client_ips',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inbounds',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('up', models.IntegerField()),
                ('down', models.IntegerField()),
                ('total', models.IntegerField()),
                ('remark', models.TextField()),
                ('enable', models.TextField()),
                ('expiry_time', models.IntegerField()),
                ('listen', models.TextField()),
                ('port', models.IntegerField()),
                ('protocol', models.TextField()),
                ('settings', models.TextField()),
                ('stream_settings', models.TextField()),
                ('tag', models.TextField()),
                ('sniffing', models.TextField()),
            ],
            options={
                'db_table': 'inbounds',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.TextField()),
                ('value', models.TextField()),
            ],
            options={
                'db_table': 'settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('password', models.TextField()),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
