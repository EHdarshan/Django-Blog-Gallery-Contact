# Generated by Django 4.0.4 on 2022-06-04 14:38

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_knowme_your_fb_knowme_your_github_knowme_your_insta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Content',
            field=django_quill.fields.QuillField(),
        ),
    ]