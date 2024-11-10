from django.db import models

# Create your models here.


"""
- COURSES
    - Title
    - Description
    - Thumbnail
    - Access
        - Anyone
        - Email Required 
        - Purschase Required 
        - User Required 
    - Status 
        - Published
        - Coming Soon 
        - Draft 
"""

class AccessChoices(models.TextChoices):
    ANYONE = 'anyone', 'Anyone'
    EMAIL_REQUIRED = 'email_required', 'Email Required'

class PublishedStatus(models.TextChoices):
    PUBLISHED = 'pub', 'Published'
    COMING_SOON = 'soon', 'Coming Soon'
    DRAFT = 'draft', 'Draft'

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # thumbnail = 
    access = models.CharField(max_length=20, choices=AccessChoices.choices, default=AccessChoices.ANYONE)
    status = models.CharField(max_length=20, choices=PublishedStatus.choices, default=PublishedStatus.DRAFT)


    @property
    def is_published(self):
        return self.status == PublishedStatus.PUBLISHED