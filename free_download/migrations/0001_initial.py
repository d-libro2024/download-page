# Generated by Django 4.1.7 on 2024-11-19 04:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DownloadableFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='downloads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='free_download.book')),
            ],
        ),
        migrations.CreateModel(
            name='EmailRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('confirmation_token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='free_download.book')),
            ],
            options={
                'unique_together': {('email', 'book')},
            },
        ),
    ]
