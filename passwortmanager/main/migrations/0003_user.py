# Generated by Django 3.2 on 2021-04-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210420_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('EMail', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
