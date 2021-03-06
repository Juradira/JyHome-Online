# Generated by Django 3.0.8 on 2020-07-21 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('proverb', models.CharField(max_length=200)),
                ('email_link', models.EmailField(max_length=200)),
                ('github_link', models.URLField()),
                ('facebook_link', models.CharField(max_length=200)),
            ],
        ),
    ]
