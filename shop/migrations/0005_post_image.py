# Generated by Django 3.0 on 2020-10-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201001_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=True, upload_to='images'),
            preserve_default=False,
        ),
    ]
