# Generated by Django 4.0.3 on 2022-04-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_rename_name_sliderimage_slider_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slider_id', models.IntegerField(default=0)),
                ('slider_image1', models.ImageField(default='', upload_to='slider_gallery/')),
                ('slider_image2', models.ImageField(default='', upload_to='slider_gallery/')),
                ('slider_image3', models.ImageField(default='', upload_to='slider_gallery/')),
                ('slider_image4', models.ImageField(default='', upload_to='slider_gallery/')),
            ],
        ),
        migrations.DeleteModel(
            name='SliderImage',
        ),
    ]
