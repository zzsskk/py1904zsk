from django.contrib import admin
from .models import *
# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    #搜索字段 搜索框会出现在右侧
    search_fields = ['title']
    # 过滤字段 过滤框会出现在上侧
    list_filter = ['title']
    # 分页 分页框会出现在下侧
    list_per_page = 1
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)
