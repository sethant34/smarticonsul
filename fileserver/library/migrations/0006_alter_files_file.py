# Generated by Django 4.2 on 2023-05-03 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_files_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(blank=True, help_text='file', upload_to='files/'),
        ),
    ]
