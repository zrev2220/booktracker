# Generated by Django 3.0.7 on 2020-06-27 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20200528_2038'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='author',
            unique_together={('first_name', 'last_name')},
        ),
    ]