from django.db import models

# Create your models here.
class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class HomePage(SingletonModel):
    background_about = models.ImageField(null=True, blank=True, upload_to='images/staticpage')
    slogan = models.CharField(max_length= 50, default = 'Learn, Share, and Colleborate')
    short_about = models.TextField(default= 'Tentang Siti dikit')
    why_python = models.TextField(default= 'Karena Asyik')

class AboutPage(SingletonModel):
    intro = models.TextField(default= 'Intro')
    visi = models.TextField(default= 'Visi')
    misi = models.TextField(default= 'Misi')
    tujuan = models.TextField(default= 'Tujuan')
