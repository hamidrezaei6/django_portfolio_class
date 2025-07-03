from django.contrib import admin
from .models import HeroSection, SocialLink, FunFact, Service, PopUpService, Portfolio, PortfolioPopUp, \
    PortfolioGallery, Education, Experience, Skill


# Register your models here.

class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    inlines = [SocialLinkInline]


admin.site.register(FunFact)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'number')


@admin.register(PopUpService)
class PopUpServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    ordering = ['order']


admin.site.register(Portfolio)


class PortfolioGalleryInline(admin.TabularInline):
    model = PortfolioGallery
    extra = 1


class PortfolioPopUpAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'client']
    inlines = [PortfolioGalleryInline]


admin.site.register(PortfolioPopUp, PortfolioPopUpAdmin)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'period', 'order']
    list_editable = ['order']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institute', 'period', 'order']
    list_editable = ['order']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage', 'order']
    list_editable = ['order']
