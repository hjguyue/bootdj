from django.contrib import admin
from books.models import Author, Book, Publisher

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    filter_horizontal = ('authors',)

class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'city', 'website')
	search_fields = ('name', 'address',)

# Register your models here.
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)

