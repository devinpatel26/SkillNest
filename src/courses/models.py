import helpers
from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Create your models here.

helpers.cloudinary_init()

class AccessChoices(models.TextChoices):
    ANYONE = 'any', 'Anyone'
    EMAIL_REQUIRED = 'email', 'Email Required'

class PublishedStatus(models.TextChoices):
    PUBLISHED = 'pub', 'Published'
    COMING_SOON = 'soon', 'Coming Soon'
    DRAFT = 'draft', 'Draft'

def handle_upload(instance, filename):
    return f'courses/images/{filename}'


def get_public_id_prefix(instance ,*args, **kwargs):
    print(args, kwargs)
    title = instance.title
    if title:
        slug = slugify(title)
        return f'course/{slug}'
    if instance.id:
        return f'course/{instance.id}'
    return 'course/unknown'

def get_public_id_prefix(instance ,*args, **kwargs):
    print(args, kwargs)
    title = instance.title
    if title:
        slug = slugify(title)
        return f'course/{slug}'
    if instance.id:
        return f'course/{instance.id}'
    return 'course/unknown'
    


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to=handle_upload, blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True , public_id_prefix=get_public_id_prefix)
    access = models.CharField(max_length=5, choices=AccessChoices.choices, default=AccessChoices.EMAIL_REQUIRED)
    status = models.CharField(max_length=20, choices=PublishedStatus.choices, default=PublishedStatus.DRAFT)
    timestamp = models.DateTimeField(auto_now_add=True)


    @property
    def is_published(self):
        return self.status == PublishedStatus.PUBLISHED
        
    @property
    def image_admin(self):
        if not self.image:
            return ''
        image_option = {
            'width': 150,
            'crop': 'pad'
        }
        url = self.image.build_url(**image_option)
        return url

    
    def get_image_thumbnail(self, as_html=False , width=150, height=150 , crop='pad'):
        if not self.image:
            return ''
        image_option = {
            'width': width,
            'height': height,
            'crop': crop
        }
        if as_html:
            # CloudinaryImage(str(obj.image)).image(width = 150, crop = "pad")  
            return self.image.image(**image_option) 
        url = self.image.build_url(**image_option)
        return url
"""
    Lessons
    #     - Title 
    #     - Description
    #     - Video 
    #     - Status 
    #         - Published
    #         - Coming Soon
    #         - Draft
"""

# Lesson.objects.all()
# Lesson.objects.first()
# course_obj = Course.objects.first()
# course_obj.lesson_set.all()
# course_obj.lesson_set.first()
# Lesson.objects.filter(course__id=course_obj.id)
# course_qs = Course.objects.filter(id=course_obj.id)
# lesson_obj = Lesson.objects.first()
# new_course_obj = lesson_obj.course 
# new_course_lesson = new_course_obj.lesson_set.all()

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    thumbnail = CloudinaryField('thumbnail', blank=True, null=True)
    video = CloudinaryField('video', blank=True, null=True , resource_type='video')
    order = models.IntegerField(default=0)
    can_preview = models.BooleanField(default=False , help_text='If user does not access to course can preview this lesson')
    status = models.CharField(max_length=20, choices=PublishedStatus.choices, default=PublishedStatus.PUBLISHED)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-updated']