# Generated by Django 4.1.7 on 2023-05-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_rename_description_blog_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="likes",
            field=models.IntegerField(null=True),
        ),
    ]
