# Generated by Django 3.2 on 2021-04-26 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='password',
            old_name='password',
            new_name='Benutzer',
        ),
        migrations.RenameField(
            model_name='password',
            old_name='user',
            new_name='Passwort',
        ),
        migrations.RenameField(
            model_name='password',
            old_name='websiteName',
            new_name='WebsiteName',
        ),
        migrations.RenameField(
            model_name='password',
            old_name='websiteURL',
            new_name='WebsiteURL',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='EMail',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Password',
            new_name='Passwort',
        ),
    ]
