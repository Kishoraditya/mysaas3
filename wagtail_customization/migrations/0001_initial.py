# Generated by Django 4.2.9 on 2024-01-10 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessibilitySettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contrast_ratios', models.TextField()),
                ('alt_tags_for_images', models.BooleanField(default=True)),
                ('keyboard_navigation', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SEOSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('structured_data_markup', models.TextField()),
                ('meta_tags', models.TextField()),
                ('social_media_tags', models.TextField()),
                ('lazy_loading', models.BooleanField(default=True)),
                ('ssl_certificates', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_color', models.CharField(default='#007BFF', max_length=7)),
                ('secondary_color', models.CharField(default='#6c757d', max_length=7)),
                ('accent_color', models.CharField(default='#FFD300', max_length=7)),
                ('background_color', models.CharField(default='#F8F9FA', max_length=7)),
                ('font_header', models.CharField(default='Roboto, Bold/Black', max_length=255)),
                ('font_body', models.CharField(default='Open Sans, Regular/Light', max_length=255)),
                ('logo', models.ImageField(upload_to='site_settings/')),
                ('favicon', models.ImageField(upload_to='site_settings/')),
            ],
        ),
        migrations.CreateModel(
            name='GlobalSEOSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
