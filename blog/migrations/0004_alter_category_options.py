# Generated by Django 4.2.4 on 2023-08-25 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]
