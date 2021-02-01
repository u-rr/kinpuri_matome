from django.db import models
from multiselectfield import MultiSelectField

# from django.conf import settings

PEOPLES = (
    (1, "King & Prince"),
    (2, "平野紫耀"),
    (3, "永瀬廉"),
    (4, "高橋海人"),
    (5, "岸優太"),
    (6, "神宮寺勇太"),
    (7, "岩橋玄樹"),
)


class Article(models.Model):
    class Meta:
        verbose_name = "記事取得データ"

    people = MultiSelectField(choices=PEOPLES)
    ogp_title = models.CharField(verbose_name="OGPタイトル", max_length=255)
    ogp_description = models.TextField(verbose_name="OGPディスクリプション", blank=True)
    ogp_site_name = models.URLField(verbose_name="サイト名")
    ogp_url = models.URLField(verbose_name="記事URL")
    ogp_image = models.URLField(verbose_name="OGP画像")
    last_update = models.DateTimeField()

    def __str__(self):
        return self.ogp_title
