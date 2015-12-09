# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *


class BBS_admin(admin.ModelAdmin):
    list_display = ('title', 'summery', 'signatrue', 'author',)
    list_filter = ('creat_at',)
    search_fields = ('title', 'author__user__username')

    def signatrue(self, obj):  #在BBS帖子列表中显示另外一个表，如BBS_user中的字段signature
        return obj.author.signature
    signatrue.short_description = 'Alias of signature'

admin.site.register(BBS, BBS_admin)
admin.site.register(Category)
admin.site.register(BBS_user)
