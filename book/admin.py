from django.contrib import admin
from .models import Author, Genre, Language, Publisher, Book
# Register your models here.


class BookModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'language', 'genre')
    # prepopulated_fields = {"slug": ("title",)}


admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Book, BookModelAdmin)
