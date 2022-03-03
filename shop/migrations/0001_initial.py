# Generated by Django 4.0.2 on 2022-03-03 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('display_name', models.CharField(max_length=200)),
                ('parent_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='')),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('display_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('creation_time', models.DateTimeField()),
                ('category', models.ManyToManyField(to='shop.Category')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.provider')),
                ('tag', models.ManyToManyField(to='shop.Tag')),
            ],
        ),
    ]
