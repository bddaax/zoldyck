# Generated by Django 5.1.1 on 2024-10-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='product_photos/'),
        ),
    ]
