from django.contrib import admin
from models import Blog,Tag,Category

admin.site.register([Category,Tag,Blog])