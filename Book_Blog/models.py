from django.db import models

class Category(models.Model):

    name = models.CharField('name',max_length=16)
    def __unicode__(self):
        return self.name

class Tag(models.Model):

    name = models.CharField('name',max_length=16)
    def __unicode__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField('title',max_length=32)
    author = models.CharField('author',max_length=16)
    content = models.TextField('content')
    created= models.DateTimeField('pubdate',auto_now_add=True)

    category = models.ForeignKey(Category,verbose_name='category')
    tags = models.ManyToManyField(Tag,verbose_name='tag')

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog,verbose_name='blog')

    name = models.CharField('Name',max_length=16)
    email = models.EmailField('Email')
    content = models.CharField('Content',max_length=140)

    created = models.DateTimeField('PubDate',auto_now_add=True)