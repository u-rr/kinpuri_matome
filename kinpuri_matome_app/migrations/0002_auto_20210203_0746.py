# Generated by Django 3.1.5 on 2021-02-02 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinpuri_matome_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='ogp_site_name',
            field=models.CharField(max_length=255, verbose_name='サイト名'),
        ),
    ]
