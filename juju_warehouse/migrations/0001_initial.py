# Generated by Django 5.0.2 on 2024-08-29 13:47

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
                ('product_name', models.CharField(max_length=200)),
                ('product_description', models.CharField(max_length=600)),
                ('product_price', models.IntegerField(default=0)),
                ('product_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
