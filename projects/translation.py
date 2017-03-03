from modeltranslation.translator import translator, TranslationOptions
from mezzanine.core.translation import TranslatedSlugged, TranslatedDisplayable, TranslatedRichText

from .models import Project


class TranslatedProject(TranslatedRichText,
                        TranslatedDisplayable,
                        TranslatedSlugged):
    fields = ()

translator.register(Project, TranslatedProject)
