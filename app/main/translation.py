# Thirdparty Library
# Thirdparty Libraries
from modeltranslation.translator import TranslationOptions, register

# Local Folders Libraries
# Localfolder Library
from .models import Glosary, Sex


@register(Sex)
class SexTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Glosary)
class GlosaryTranslationOptions(TranslationOptions):
    fields = (
        "term",
        "description",
    )
