from django.contrib import admin
from .models import Articles,Author,Category,Language,ContentImage

class ContentImageInline(admin.TabularInline):
    model=ContentImage

class ArticlesAdmin(admin.ModelAdmin):
    list_display=('article_id','title','submit_date','author',)
    list_display_links=('article_id',)
    readonly_fields=('article_id',)
    inlines=[ContentImageInline]

class LanguageAdmin(admin.ModelAdmin):
    list_display=('name','color')
    list_display_links=('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('category_id','model_cate_to_chinese','article_num')
    list_display_links=('category_id',)
    readonly_fields=('category_id','article_num')

class AuthorAdmin(admin.ModelAdmin):
    list_display=('author_id','name','description')
    list_display_links=('author_id',)
    readonly_fields=('author_id',)

class ContentImageAdmin(admin.ModelAdmin):
    list_display=('content_image','__str__')
    list_display_links=('content_image',)


admin.site.register(Articles,ArticlesAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Language,LanguageAdmin)
admin.site.register(ContentImage,ContentImageAdmin)
# Register your models here.
