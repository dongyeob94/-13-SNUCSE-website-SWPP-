# Generated by Django 2.0.5 on 2018-05-28 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_emeritus'),
    ]

    operations = [
        migrations.AddField(
            model_name='emeritus',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='emeritus/'),
        ),
    ]
