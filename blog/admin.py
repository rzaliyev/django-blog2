from django.contrib import admin
from .models import Post, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}   # auto-fills slug as you type the name


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status', 'created_at']
    list_filter = ['status', 'category', 'created_at']
    search_fields = ['title', 'content', 'author__username']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']       # better than a dropdown when you have many users
    filter_horizontal = ['tags']     # nice two-panel widget for ManyToMany
    date_hierarchy = 'created_at'    # date drill-down at the top of the list
    ordering = ['-created_at']

    # Group fields visually in the edit form
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'author', 'cover_image', 'excerpt', 'content')
        }),
        ('Classification', {
            'fields': ('category', 'tags')
        }),
        ('Publishing', {
            'fields': ('status',)
        }),
    )
