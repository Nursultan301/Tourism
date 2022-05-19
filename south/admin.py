from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin

from south.models import Osh, Trips, DjalalAbad, Batken


class PostAdminForm(forms.ModelForm):
    description_ru = forms.CharField(widget=CKEditorUploadingWidget())
    description_en = forms.CharField(widget=CKEditorUploadingWidget())
    description_kg = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Osh
        fields = '__all__'


@admin.register(Osh)
class PostAdmin(TranslationAdmin):
    form = PostAdminForm


# @admin.register(Trips)
# class TripsAdmin(TranslationAdmin):
#     save_on_top = True
#     form = PostAdminForm
#

@admin.register(DjalalAbad)
class DjalalAbadAdmin(TranslationAdmin):
    pass


@admin.register(Batken)
class BatkenAdmin(TranslationAdmin):
    pass
