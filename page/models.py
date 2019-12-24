from django.db import models

STATUS = [
  ('draft', 'Taslak'),
  ('published', 'Yayinlandi'),
  ('deleted', 'Silindi'),
]

# Create your models here.
class Page(models.Model):
  title = models.CharField(max_length=200)
  slug = models.SlugField(max_length=200, default="")
  content = models.TextField()
  cover_image = models.ImageField(upload_to='page', null=True, blank=True)
  status = models.CharField(
    default="draft",
    choices=STATUS,
    max_length=10,
  )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
