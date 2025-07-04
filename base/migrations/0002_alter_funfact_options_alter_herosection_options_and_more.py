# Generated by Django 5.2 on 2025-05-04 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funfact',
            options={'verbose_name': 'آمار', 'verbose_name_plural': 'آمارها'},
        ),
        migrations.AlterModelOptions(
            name='herosection',
            options={'verbose_name': 'بخش معرفی', 'verbose_name_plural': 'بخش های معرفی'},
        ),
        migrations.AlterModelOptions(
            name='sociallink',
            options={'verbose_name': 'لینک شبکه های اجتماعی', 'verbose_name_plural': 'لینک های شبکه های اجتماعی'},
        ),
        migrations.AlterField(
            model_name='funfact',
            name='suffix',
            field=models.CharField(blank=True, max_length=50, verbose_name='پسوند (اختیاری)'),
        ),
        migrations.AlterField(
            model_name='funfact',
            name='title',
            field=models.CharField(max_length=200, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='funfact',
            name='value',
            field=models.CharField(max_length=10, verbose_name='عدد'),
        ),
        migrations.AlterField(
            model_name='herosection',
            name='description',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='herosection',
            name='image',
            field=models.ImageField(upload_to='media/hero/', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='herosection',
            name='resume_link',
            field=models.URLField(verbose_name='لینک رزومه'),
        ),
        migrations.AlterField(
            model_name='herosection',
            name='subtitle',
            field=models.CharField(max_length=200, verbose_name='زیر عنوان'),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='hero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_link', to='base.herosection', verbose_name='بخش معرفی'),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='icon_class',
            field=models.CharField(max_length=100, verbose_name='کلاس آیکون'),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='platform',
            field=models.CharField(max_length=50, verbose_name='نام شبکه'),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='url',
            field=models.URLField(verbose_name='آدرس شبکه'),
        ),
    ]
