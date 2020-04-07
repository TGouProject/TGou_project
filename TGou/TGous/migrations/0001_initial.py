# Generated by Django 3.0.4 on 2020-04-07 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tgshoppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopping_name', models.CharField(max_length=100)),
                ('shopping_price', models.CharField(max_length=45)),
                ('shopping_info', models.CharField(max_length=500)),
                ('shopping_type', models.CharField(max_length=45)),
                ('shopping_sv', models.CharField(max_length=100)),
                ('shopping_photo', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TGou_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordedr_number', models.CharField(default=None, max_length=200, unique=True)),
                ('order_info', models.CharField(max_length=200)),
                ('Quantity_of_Goods', models.CharField(max_length=10)),
                ('order_money', models.CharField(max_length=100)),
                ('order_type', models.CharField(max_length=15)),
                ('order_data', models.DateField(auto_now=True)),
                ('order_state', models.CharField(max_length=10)),
                ('shipping_address', models.CharField(blank=True, max_length=150, null=True)),
                ('tgou_Order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Login.User')),
            ],
        ),
    ]
