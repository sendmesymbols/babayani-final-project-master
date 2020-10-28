# Generated by Django 3.0.8 on 2020-09-16 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0002_bag_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('discount_percentage', models.IntegerField(blank=True, default=0)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
