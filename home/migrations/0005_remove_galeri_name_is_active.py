# Generated by Django 4.2 on 2023-04-19 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_galeri_name_alter_about_about_image_galeri'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galeri_name',
            name='is_active',
        ),
    ]