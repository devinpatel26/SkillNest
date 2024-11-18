from django.contrib import admin
from cloudinary import CloudinaryImage
from .models import Course
from django.utils.html import mark_safe, format_html


# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'access']
    fields = ['title', 'description', 'status', 'image', 'access', 'display_image', 'is_published']
    list_filter = ['status', 'access']
    readonly_fields = ['display_image', 'is_published']

    def display_image(self, obj, *args, **kwargs):
        # Accessing the image attribute of the Course instance
        url = obj.image_admin
        return format_html(f'<img src="{url}"/>')

