# Generated by Django 2.0.5 on 2018-05-26 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180526_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attached',
            name='attached',
            field=models.FileField(blank=True, null=True, upload_to='notice/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='notice/'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='professor/'),
        ),
    ]
