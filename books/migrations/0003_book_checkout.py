# Generated by Django 2.2.1 on 2019-05-07 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0001_initial"),
        ("books", "0002_auto_20190507_1721"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="checkout",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="people.Person",
            ),
        ),
    ]
