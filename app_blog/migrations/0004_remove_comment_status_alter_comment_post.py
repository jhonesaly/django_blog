# Generated by Django 4.2.3 on 2023-07-11 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='status',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app_blog.post'),
        ),
    ]
