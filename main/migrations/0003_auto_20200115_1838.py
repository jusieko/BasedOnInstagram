# Generated by Django 3.0.2 on 2020-01-15 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200115_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='desc',
            new_name='description',
        ),
    ]