# Generated by Django 2.0.5 on 2018-06-02 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20180603_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='website',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]