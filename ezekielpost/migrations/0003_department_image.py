# Generated by Django 4.2.5 on 2023-09-21 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezekielpost', '0002_remove_department_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='service/'),
        ),
    ]
