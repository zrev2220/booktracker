# Generated by Django 2.2.1 on 2019-05-07 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_book_checkout"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ManyToManyField(blank=True, to="books.Author"),
        ),
    ]
