from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import BlockInfo #, ImageGallery


#class InlineImage(admin.TabularInline):
    #fk_name = 'block_info'
   # model = ImageGallery


class BlockInfoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100">')

    get_image.short_description = "Изображение"


   # inlines = [InlineImage]


admin.site.register(BlockInfo, BlockInfoAdmin)





