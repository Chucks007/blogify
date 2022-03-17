# Generated by Django 4.0.3 on 2022-03-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_ipmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_likes', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ViewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_views', models.CharField(max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='IpModel',
        ),
    ]
