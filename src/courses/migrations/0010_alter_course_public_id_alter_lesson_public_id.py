# Generated by Django 5.1.3 on 2024-12-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_lesson_public_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='public_id',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='public_id',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
    ]
