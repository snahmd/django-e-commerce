# Generated by Django 2.1.7 on 2019-12-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_auto_20191224_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='page'),
        ),
    ]
