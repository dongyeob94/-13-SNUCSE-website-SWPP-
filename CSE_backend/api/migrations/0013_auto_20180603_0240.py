# Generated by Django 2.0.5 on 2018-06-02 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0012_auto_20180603_0153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(blank=True, max_length=20)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('abbreviation', models.CharField(max_length=20)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='professor',
            name='location',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='website',
        ),
        migrations.AlterField(
            model_name='professor',
            name='lab',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='professor', to='api.Lab'),
        ),
    ]
