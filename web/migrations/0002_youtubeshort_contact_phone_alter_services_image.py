# Generated by Django 4.2.21 on 2025-05-09 13:53

from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YouTubeShort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video_url', models.URLField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='youtube_shorts/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True, validators=[web.models.validate_phone]),
        ),
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='services/'),
        ),
    ]
