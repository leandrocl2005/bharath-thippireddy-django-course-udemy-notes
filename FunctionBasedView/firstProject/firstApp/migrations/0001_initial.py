# Generated by Django 3.1.3 on 2020-11-21 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('sal', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
