# Generated by Django 2.2.1 on 2019-05-29 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, default='static/img/default_blog.jpg', null=True, upload_to='static/img/%Y/%m/%d'),
        ),
    ]