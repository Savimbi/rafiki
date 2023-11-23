# Generated by Django 4.2.7 on 2023-11-23 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(blank=True, max_length=100, unique=True)),
                ('additional_info', models.TextField(blank=True)),
                ('rating', models.PositiveSmallIntegerField(default=50)),
                ('book_count', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
