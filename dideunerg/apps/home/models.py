from django.db import models

from django.contrib.auth.models import User

class perfilUsuario(models.Model):
    def url(self,filename):
        ruta = "MultimediaData/Usuarios/%s/%s"%(self.usuario.username,filename)
        return ruta


    usuario = models.OneToOneField(User)
    foto = models.ImageField(upload_to=url)

    def __unicode__(self):
        return self.usuario.username
