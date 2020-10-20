# Generated by Django 3.1.2 on 2020-10-20 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer_text', models.CharField(max_length=255)),
                ('inner_text', models.CharField(max_length=255)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('card_color', models.CharField(choices=[(0, 'White'), (1, 'Red'), (2, 'Orange'), (3, 'Yellow'), (4, 'Green'), (5, 'Blue'), (6, 'Indigo'), (7, 'Violet'), (8, 'Black')], default=0, max_length=1)),
                ('border_style', models.CharField(choices=[(0, 'tbd'), (1, 'tbd'), (2, 'etc')], default=0, max_length=1)),
                ('favorited_by', models.ManyToManyField(blank=True, related_name='favorited_posts', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=255)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('favorited_by', models.ManyToManyField(blank=True, related_name='favorited_comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='instaky.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
