# Generated by Django 3.1.7 on 2021-02-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('V_Maven', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
