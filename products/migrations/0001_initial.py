# Generated by Django 5.0.6 on 2024-07-10 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_modified', models.DateTimeField(auto_created=True)),
                ('datetime_created', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=150)),
                ('discription', models.TextField()),
                ('price', models.PositiveIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable'), ('coming_soon', 'comming soon')], max_length=12)),
            ],
        ),
    ]
