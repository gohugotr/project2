# Generated by Django 3.0.3 on 2020-05-02 22:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20200503_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
