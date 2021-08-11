from django.db import models

# Create your models here.
class Post(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 20, verbose_name="제목")
    description = models.TextField(default='', verbose_name="내용")
    # category = models.ForeignKey(Category_t, on_delete=models.CASCADE, verbose_name='카테고리')
    thumbnail = models.ImageField(upload_to='./test/', default='', verbose_name="사진")

    def __str__(self):
            """A string representation of the model."""
            return self.title