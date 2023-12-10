from django.contrib import admin

from .models import Category, Location, Post, Comment

admin.site.empty_value_display = 'Не задано'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'slug',
        'is_published'
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('title', 'description')
    list_filter = ('is_published',)
    list_display_links = ('title',)


class CategoryInline(admin.TabularInline):
    model = Category


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at',
        'is_published'
    )
    list_editable = (
        'is_published',
    )
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('is_published',)


class LocationInline(admin.TabularInline):
    model = Location


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'location',
        'category',
        'pub_date',
        'is_published',
    )
    list_editable = ('is_published',)
    list_display_links = ('title',)
    search_fields = ('title', 'text')
    list_filter = ('is_published',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'post',
        'created_at',
        'author'
    )
