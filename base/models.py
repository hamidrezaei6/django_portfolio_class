from django.db import models


class HeroSection(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    subtitle = models.CharField(max_length=200, verbose_name='زیر عنوان')
    description = models.TextField(verbose_name='توضیحات')
    resume_link = models.URLField(verbose_name='لینک رزومه')
    image = models.ImageField(upload_to='hero/', verbose_name='تصویر')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بخش معرفی'
        verbose_name_plural = 'بخش های معرفی'


class SocialLink(models.Model):
    hero = models.ForeignKey(HeroSection, on_delete=models.CASCADE, related_name='social_link',
                             verbose_name='بخش معرفی')
    platform = models.CharField(max_length=50, verbose_name='نام شبکه')
    icon_class = models.CharField(max_length=100, verbose_name='کلاس آیکون')  # fa-brands , fa-instagram , fa-twitter
    url = models.URLField(verbose_name='آدرس شبکه')

    def __str__(self):
        return self.icon_class

    class Meta:
        verbose_name = 'لینک شبکه های اجتماعی'
        verbose_name_plural = 'لینک های شبکه های اجتماعی'


class FunFact(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    value = models.CharField(max_length=10, verbose_name='عدد')
    suffix = models.CharField(max_length=50, blank=True, verbose_name='پسوند (اختیاری)')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'آمار'
        verbose_name_plural = 'آمارها'


class Service(models.Model):
    number = models.PositiveIntegerField(verbose_name='شماره')
    title = models.CharField(max_length=100, verbose_name='عنوان خدمت')
    description = models.TextField(verbose_name='توضیحات')
    delay = models.CharField(
        max_length=10, default='.5s', verbose_name='تاخیر در نمایش انیمیشن'
    )

    class Meta:
        verbose_name = 'خدمت'
        verbose_name_plural = 'لیست خدمات'

    def __str__(self):
        return self.title


class PopUpService(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان خدمت')
    short_description = models.TextField(verbose_name='توضیح کوتاه')
    full_description = models.TextField(verbose_name='توضیحات کامل')
    process = models.TextField(verbose_name='فرایند خدمت')
    image = models.ImageField(upload_to='services/', verbose_name='تصویر')
    order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'خدمت(پاپ آپ)'
        verbose_name_plural = 'لیست خدمات(پاپ آپ)'


class Portfolio(models.Model):
    CATEGORY_CHOICES = [
        ('uxui' , 'UX/UI'),
        ('branding' , 'BRANDING'),
        ('web-app' , 'WEB APP'),
        ('mobile-app' , 'MOBILE APP')
    ]
    title = models.CharField(max_length=100,verbose_name='عنوان پورتفولیو')
    description = models.TextField(verbose_name='توضیحات بیشتر')
    image = models.ImageField(upload_to='portfolio/')
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES,verbose_name='دسته بندی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پروژه های اخیر'
        verbose_name_plural = 'لیست پروژه های اخیر'


class PortfolioPopUp(models.Model):
    CATEGORY_CHOICES = [
        ('uxui' , 'UX/UI'),
        ('branding' , 'BRANDING'),
        ('web-app' , 'WEB APP'),
        ('mobile-app' , 'MOBILE APP')
    ]

    title = models.CharField(max_length=100,verbose_name='عنوان')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    full_description = models.TextField(verbose_name='توضیحات کامل')
    summary = models.TextField()
    our_approach = models.TextField()
    client = models.CharField(max_length=100)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES,verbose_name='دسته بندی')
    start_date = models.CharField(max_length=100)
    designer = models.CharField(max_length=100)
    preview_url = models.URLField(blank=True,null=True)
    thumbnail = models.ImageField(upload_to='portfolio/thumbnail/')
    modal_image = models.ImageField(upload_to='portfolio/modal/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پروژه های اخیر(بخش پاپ آپ)'
        verbose_name_plural = 'لیست پروژه های اخیر(بخش پاپ آپ)'


class PortfolioGallery(models.Model):
    portfolio = models.ForeignKey(PortfolioPopUp,related_name='gallery',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/gallery/')

    def __str__(self):
        return f'Gallery Image for {self.portfolio.title}'

class Experience(models.Model):
    title = models.CharField('عنوان شغلی',max_length=100)
    company = models.CharField('محل/شرکت',max_length=100)
    period = models.CharField('مدت زمان',max_length=100)
    order = models.PositiveIntegerField('ترتیب نمایش',default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'سابقه کاری'
        verbose_name_plural = 'سوابق کاری'

    def __str__(self):
        return f'{self.title} - {self.company}'


class Education(models.Model):
    degree = models.CharField('نام دوره',max_length=100)
    institute = models.CharField('نام موسسه',max_length=100)
    period = models.CharField('مدت زمان',max_length=100)
    order = models.PositiveIntegerField('ترتیب نمایش',default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'تحصیلات'
        verbose_name_plural = 'سوابق تحصیلی'

    def __str__(self):
        return f'{self.degree} - {self.institute}'


class Skill(models.Model):
    name = models.CharField('عنوان مهارت',max_length=100)
    percentage = models.PositiveIntegerField('درصد مهارت')
    icon = models.ImageField('آیکون مهارت',upload_to='skills/icons/')
    order = models.PositiveIntegerField('ترتیب نمایش',default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت ها'

    def __str__(self):
        return f'{self.name} - {self.percentage}'