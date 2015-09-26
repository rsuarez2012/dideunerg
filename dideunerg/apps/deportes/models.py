from django.db import models

'''class Nucleos(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Nucleos'

    def __unicode__(self):
        return self.nombre

class Carreras(models.Model):
    codigo = models.CharField(max_length=6)
    nombre_carrera = models.CharField(max_length=30)
    nucleo = models.ForeignKey('Nucleos')

    class Meta:
        verbose_name_plural = 'Carreras'

    def __unicode__(self):
        return u'%s %s %s'%(self.codigo,self.nombre_carrera,self.nucleo)

class Disciplina(models.Model):
    disciplina = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Disciplinas'

    def __unicode__(self):
        return self.disciplina'''

class Entrenadores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    #disciplina = models.ForeignKey('Disciplina')
    telefono = models.CharField(max_length=13)
    #horas = models.DecimalField(max_digits=4,decimal_places=2)
    lugar_de_entrenamiento = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'Entrenadores'

    def __unicode__(self):
        return self.nombre


'''class Recor_Del_Atleta(models.Model):
    fecha = models.DateTimeField(auto_now=False)
    lugar = models.CharField(max_length=50)
    lugar_obtenido = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = ('Recor del Atleta')

    def __unicode__(self):
        return self.lugar_obtenido'''

class Atletas(models.Model):
    def url(self,filename):
        ruta = "MultimediaData/Atletas/%s/%s"%(self.apellido,str(filename))
        return ruta

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.IntegerField()
    telefono = models.IntegerField()
    direccion = models.TextField()
    cohorte = models.IntegerField()
    foto = models.ImageField(upload_to=url)
    carrera = models.CharField(choices=(('Derecho','Derecho'),('Medicina','Medicina'),('Odontologia','Odontologia'),('Informatica','Informatica'),('Civil','Ing. Civil'),('Contaduria','Contaduria'),('Economia','Economia'),('Agronomia','Agronomia'),('Administracion','Administracion')),null=True, blank=True, max_length=100)
    #disciplina = models.ForeignKey('Disciplina',null=True, blank=True)
    #recor = models.ForeignKey('Recor_Del_Atleta',null=True, blank=True)
    egreso = models.BooleanField()

    class Meta:
        verbose_name_plural = ('Atletas')
        ordering = ["carrera"]

    def __unicode__(self):
        return u"%s %s" %(self.nombre, self.apellido)

