# Generated by Django 4.2.4 on 2023-09-01 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refview', '0002_alter_imagepost_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagepost',
            name='preview',
            field=models.ImageField(blank=True, editable=False, upload_to=''),
        ),
    ]
