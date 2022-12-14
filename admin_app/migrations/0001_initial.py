# Generated by Django 4.0.6 on 2022-10-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='edu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('board', models.CharField(max_length=100)),
                ('yop', models.CharField(max_length=100)),
                ('mark', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'education',
            },
        ),
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'home_content',
            },
        ),
        migrations.CreateModel(
            name='intern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com', models.CharField(max_length=150)),
                ('period', models.CharField(max_length=150)),
                ('inn', models.TextField()),
            ],
            options={
                'db_table': 'intern',
            },
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ski', models.TextField()),
            ],
            options={
                'db_table': 'skill',
            },
        ),
    ]
