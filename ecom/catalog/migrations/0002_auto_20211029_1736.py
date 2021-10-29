# Generated by Django 3.2.8 on 2021-10-29 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='discount_price',
        ),
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(choices=[('xsmall', 'xs'), ('small', 's'), ('medium', 'm'), ('large', 'l'), ('xlarge', 'xl')], max_length=20),
        ),
    ]