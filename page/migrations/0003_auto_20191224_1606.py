# Generated by Django 2.1.7 on 2019-12-24 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='cover_image',
            field=models.ImageField(null=True, upload_to='page'),
        ),
    ]
