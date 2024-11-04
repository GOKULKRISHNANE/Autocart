# Generated by Django 3.2.25 on 2024-05-18 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'cart',
                'managed': False,
            },
        ),
    ]
