# Generated by Django 4.0.2 on 2022-02-27 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo_link',
            field=models.CharField(blank=True, max_length=2500, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='source_link',
            field=models.CharField(blank=True, max_length=2500, null=True),
        ),
    ]
