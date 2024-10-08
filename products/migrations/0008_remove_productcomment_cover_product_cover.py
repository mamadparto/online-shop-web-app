# Generated by Django 5.0.6 on 2024-07-30 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_productcomment_cover_alter_productcomment_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcomment',
            name='cover',
        ),
        migrations.AddField(
            model_name='product',
            name='cover',
            field=models.ImageField(blank=True, upload_to='product/product_cover/', verbose_name='product image'),
        ),
    ]
