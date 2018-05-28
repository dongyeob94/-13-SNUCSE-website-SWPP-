# Generated by Django 2.0.5 on 2018-05-25 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180525_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='attacheds',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='images',
        ),
        migrations.AddField(
            model_name='notice',
            name='attached',
            field=models.ManyToManyField(blank=True, null=True, related_name='notice', to='api.Attached'),
        ),
        migrations.AddField(
            model_name='notice',
            name='image',
            field=models.ManyToManyField(blank=True, null=True, related_name='notice', to='api.Image'),
        ),
    ]
