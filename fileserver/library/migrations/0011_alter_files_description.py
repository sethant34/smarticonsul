# Generated by Django 4.2.6 on 2023-11-11 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_files_preview_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='description',
            field=models.CharField(blank=True, help_text='description', max_length=10000),
        ),
    ]
