# Librerias Standard
# Standard Libraries
import os

# Django Libraries
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class SobreEscribirImagen(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name
