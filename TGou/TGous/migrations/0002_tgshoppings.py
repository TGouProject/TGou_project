# Generated by Django 3.0.4 on 2020-04-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TGous', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tgshoppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shapping_name', models.CharField(max_length=100)),
                ('shopping_monney', models.CharField(max_length=45)),
                ('shopping_info', models.CharField(max_length=500)),
                ('shopping_type', models.CharField(max_length=45)),
                ('shopping_sv', models.CharField(max_length=100)),
                ('shopping_photo', models.CharField(max_length=500)),
            ],
        ),
    ]
