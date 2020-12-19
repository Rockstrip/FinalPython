# Generated by Django 2.2.17 on 2020-12-19 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=30, verbose_name='Name of article')),
                ('article_text', models.TextField(verbose_name='Text of article')),
                ('pub_date', models.DateTimeField(verbose_name='Pulish date')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=30, verbose_name='Name of author')),
                ('comment_text', models.CharField(max_length=30, verbose_name='Text of comment')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
        ),
    ]