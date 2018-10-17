from django.contrib import admin

# Register your models here.
from books.models import BookInfo, HeroInfo

from django.contrib import admin

admin.site.site_header = '传智书城'
admin.site.site_title = '传智书城MIS'
admin.site.index_title = '欢迎使用传智书城MIS'

# 关联对象
class HeroInfoStackInline(admin.StackedInline):
    model = HeroInfo  # 要编辑的对象
    extra = 1  # 附加编辑的数量

# 可以用表格的形式嵌入。
class HeroInfoTabularInline(admin.TabularInline):
    model = HeroInfo
    extra = 1


# Django提供的Admin站点的展示效果可以通过自定义ModelAdmin类来进行控制
# 定义管理类  需要继承自admin.ModelAdmin类
class BookInfoAdmin(admin.ModelAdmin):
    #  页大小
    list_per_page = 2

    # "操作选项"的位置
    actions_on_top = True
    actions_on_bottom = True

    # 列表中的列
    list_display = ['id', 'btitle',  'pub_date']
    # 显示字段
    # fields = ['btitle', 'bpub_date']
    # 分组显示
    fieldsets = (
        ('基本', {'fields': ['btitle', 'bpub_date','image']}),
        ('高级', {
            'fields': ['bread', 'bcomment'],
            'classes': ('collapse',)  # 是否折叠显示
        })
    )
    # inlines = [HeroInfoStackInline]
    inlines = [HeroInfoTabularInline]

class HeroInfoAdmin(admin.ModelAdmin):
    #  页大小
    list_per_page = 5

    # "操作选项"的位置
    actions_on_top = True
    actions_on_bottom = True

    # 列表中的列
    list_display = ['id', 'hname', 'hbook', 'read']
    # 右侧栏过滤器
    list_filter = ['hbook', 'hgender']
    # 搜索框
    search_fields = ['hname']

# 使用管理类  注册参数
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)




# # 装饰器
# @admin.register(BookInfo)
# class BookInfoAdmin(admin.ModelAdmin):
#     pass
