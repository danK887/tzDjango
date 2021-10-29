from django.db import models
from django.urls import reverse



class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%d/%m/%Y/")
    tag = models.ForeignKey('Tags', on_delete=models.PROTECT, null=True )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Tags(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tags', kwargs={'tag_id': self.pk})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'