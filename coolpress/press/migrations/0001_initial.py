# Generated by Django 3.2.8 on 2021-10-19 16:41
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
            name='CoolUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_profile', models.CharField(blank=True, max_length=150, null=True)),
                ('gh_repositories', models.IntegerField(blank=True, null=True)),
                ('gravatar_link', models.CharField(blank=True, max_length=400, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]