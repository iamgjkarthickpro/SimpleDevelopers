# Generated by Django 3.2 on 2022-06-30 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wearedevelopersapp', '0002_rename_blog_blogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='context',
            field=models.TextField(blank=True, null=True),
        ),
    ]
