# Generated by Django 3.0.3 on 2020-04-30 19:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_setting_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='aboutus',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
