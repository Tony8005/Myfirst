from django.contrib import admin
from sign.models import Event, Guest

# 在admin管理后台展示更多字段
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']
    search_fields = ['name']  # 在admin后台增加搜索栏
    list_filter = ['status']  # 在admin后台增加过滤器


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']
    search_fields = ['realname', 'phone']
    list_filter = ['sign']

# 在admin管理后台注册发布会表、嘉宾表
admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)

