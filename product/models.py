from django.db import models
from django.utils.safestring import mark_safe


class Category(models.Model) :
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(blank=True,unique=True, max_length=150)
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta :
        # enforcing that there can not be two categories under a parent with same slug
        # Aynı slug alanına sahip 2 kategori bir ebeveyn kategori altında olamamay zorlar.
        unique_together = ('slug', 'parent',)
        verbose_name_plural = 'categories'

    def __str__(self) :
        full_path = [self.title]

        k = self.parent
        while k is not None :
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1]) # Alt kategori gösterim biçimi Elektrnik -> Elektro Gitar gibi

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="50px"/>'.format(self.image.url))
        return self.image
    image_tag.short_description = 'Resim'

# 9. video
# https://www.youtube.com/watch?v=iHOTC96fvOY&list=PLIUezwWmVtFUq0RcsaBn8LR_o9R5psLPh&index=2

class Product(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )
    category        = models.ForeignKey(Category,on_delete=models.CASCADE)
    title           = models.CharField(max_length=150)
    keywords        = models.CharField(blank=True, max_length=255)
    description     = models.CharField(blank=True, max_length=255)
    image           = models.ImageField(blank=True, upload_to='images/')
    price           = models.FloatField()
    amount          = models.IntegerField(default=0)
    detail          = models.TextField()
    slug            = models.SlugField(blank=True,unique=True, max_length=150)
    status          = models.CharField(max_length=10, choices=STATUS)
    create_at       = models.DateTimeField(auto_now_add=True)
    update_at       = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-amount']
    
    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="50px"/>'.format(self.image.url))
        return self.image
    image_tag.short_description = 'Resim'

class Images(models.Model):
    product     = models.ForeignKey(Product,on_delete=models.CASCADE)
    title       = models.CharField(max_length=50)
    image       = models.ImageField(blank=True,upload_to='images/')

    class Meta: # Bu sınıf ilk tanımla
        verbose_name = 'Images'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="50px"/>'.format(self.image.url))
        return self.image
    image_tag.short_description = 'Resim'



