# Generated by Django 3.1.7 on 2021-02-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('V_Maven', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=False, upload_to='product'),
            preserve_default=False,
        ),
    ]
