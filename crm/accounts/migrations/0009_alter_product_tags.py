# Generated by Django 5.0.6 on 2024-07-18 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='products', to='accounts.tag'),
        ),
    ]
