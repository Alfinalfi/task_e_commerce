# Generated by Django 4.2.3 on 2023-07-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapi', '0002_alter_customer_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]