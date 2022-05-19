from modeltranslation.translator import register, TranslationOptions
from south.models import Osh, Trips, DjalalAbad, Batken


@register(Osh)
class OshTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(DjalalAbad)
class DjalalAbadTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Batken)
class BatkenTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
