# Generated by Django 4.2.7 on 2023-11-23 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
        ('publishers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publishers.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(blank=True, max_length=24)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.booktitle')),
            ],
            options={
                'db_table': 'books.book',
            },
        ),
    ]