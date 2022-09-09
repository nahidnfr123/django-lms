from django.contrib import admin

# Register your models here.
from .models import Course, Section, Note, RecordedClass, LiveClass, Exam, Assignment, Mcq


# @admin.register(Course, Section, Note, RecordedClass, LiveClass, Exam, Assignment, Mcq)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'course_image', 'status', 'featured', 'price', 'discounted_price', 'available_at')
    list_display_links = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('status', 'featured', 'price', 'discounted_price')
    list_filter = ('title',)
    search_fields = ('title',)
    # fields = (('title', 'slug'), 'subtitle', 'image', 'description', 'price', 'discounted_price', 'status', 'featured', 'available_at')
    readonly_fields = ('course_image',)


admin.site.register(Course, CourseAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'status', 'available_at')
    list_display_links = ('title',)
    # list_editable = ('status')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('title',)
    search_fields = ('title',)


admin.site.register(Section, SectionAdmin)

admin.site.site_header = "Academic Performance Assessment and support"
