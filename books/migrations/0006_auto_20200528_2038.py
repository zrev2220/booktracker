# Generated by Django 3.0.6 on 2020-05-29 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0005_auto_20190509_2210"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]
