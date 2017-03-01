from django.contrib import admin
from .models import Articles,Author,Category,Language,ContentImage

admin.site.register(Articles)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(ContentImage)
# Register your models here.
