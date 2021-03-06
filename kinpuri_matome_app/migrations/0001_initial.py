# Generated by Django 3.1.5 on 2021-02-01 13:17

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'King & Prince'), (2, '平野紫耀'), (3, '永瀬廉'), (4, '高橋海人'), (5, '岸優太'), (6, '神宮寺勇太'), (7, '岩橋玄樹')], max_length=13)),
                ('ogp_title', models.CharField(max_length=255, verbose_name='OGPタイトル')),
                ('ogp_description', models.TextField(blank=True, verbose_name='OGPディスクリプション')),
                ('ogp_site_name', models.URLField(verbose_name='サイト名')),
                ('ogp_url', models.URLField(verbose_name='記事URL')),
                ('ogp_image', models.URLField(verbose_name='OGP画像')),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'verbose_name': '記事取得データ',
            },
        ),
    ]
