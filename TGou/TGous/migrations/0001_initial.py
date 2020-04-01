# Generated by Django 3.0.4 on 2020-03-31 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TGou_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordedr_number', models.CharField(default=None, max_length=200, unique=True)),
                ('order_info', models.CharField(max_length=200)),
                ('Quantity_of_Goods', models.CharField(max_length=10)),
                ('order_money', models.CharField(max_length=100)),
                ('order_type', models.CharField(max_length=15)),
                ('order_data', models.DateField()),
                ('order_state', models.CharField(max_length=10)),
                ('shipping_address', models.CharField(default=None, max_length=150)),
            ],
        ),
    ]