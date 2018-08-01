from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author, Genre, Book, BookInstance


# Define the admin class
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


#admin.site.register(Book)
#admin.site.register(BookInstance)
# Register the Admin classes for Book using the decorator

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    Inline = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
