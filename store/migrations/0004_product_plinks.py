# Generated by Django 4.0.2 on 2022-04-22 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='plinks',
            field=models.URLField(max_length=300, null=True),
        ),
    ]