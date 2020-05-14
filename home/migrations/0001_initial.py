# Generated by Django 3.0.4 on 2020-03-18 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=13)),
                ('desc', models.TextField(max_length=1000)),
            ],
        ),
    ]