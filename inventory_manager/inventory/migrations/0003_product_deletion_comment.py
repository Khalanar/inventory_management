# Generated by Django 3.2 on 2022-05-30 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='deletion_comment',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
