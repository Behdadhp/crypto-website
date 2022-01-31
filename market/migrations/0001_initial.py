# Generated by Django 3.2.5 on 2022-01-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin', models.CharField(max_length=32)),
                ('label', models.CharField(max_length=8)),
                ('price', models.FloatField(max_length=16)),
            ],
        ),
    ]
