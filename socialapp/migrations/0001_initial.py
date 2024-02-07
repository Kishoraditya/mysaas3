# Generated by Django 4.2.9 on 2024-01-10 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram_access_token', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_access_token', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
