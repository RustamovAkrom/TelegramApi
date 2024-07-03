from modeltranslation.translator import register, TranslationOptions
from .models import Channel, Group


@register(Channel)
class ChannelTransaltionOptions(TranslationOptions):
    fields = ("name", "description")


@register(Group)
class GroupTranslationOptions(TranslationOptions):
    fields = ("name", "description")
