from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from osh.models import Post, Trips, Food


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


@admin.register(Trips)
class TripsAdmin(admin.ModelAdmin):
    save_on_top = True
    form = PostAdminForm


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    form = PostAdminForm
