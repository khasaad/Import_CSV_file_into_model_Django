from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Norme (models.Model):
    numdos = models.CharField(_("NUMDOS"), max_length=255)
    numdosverling = models.CharField(_("NUMDOSVERLING"), max_length=255, blank=True)
    ancart = models.CharField(_("ANCART"), max_length=255, blank=True)
    filiere = models.CharField(_("FILIERE"), max_length=255, blank=True)
    etape = models.FloatField()(_("ETAPE"), max_length=255, blank=True)
    verling = models.TextField(_("VERLING"), max_length=255, blank=True)
    formats = models.TextField(_("FORMAT"), max_length=255, blank=True)

    def __str__(self):
        return f'{self.numdos} | {self.numdosverling} | {self.ancart} | {self.filiere} | {self.etape} | {self.verling} | {self.formats}'