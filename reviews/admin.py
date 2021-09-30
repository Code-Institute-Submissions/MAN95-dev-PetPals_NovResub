from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'item',
        'user',
        'date_created'
    )


admin.site.register(Review, ReviewAdmin)

