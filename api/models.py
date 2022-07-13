from django.db import models


class Patient(models.Model):
    name = models.CharField('Nome', max_length=255)
    age = models.IntegerField('Idade', blank=True, null=True)
    address = models.TextField('Endereço', blank=True, null=True)

    class Meta:
        db_table = 'patient'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return self.name


class Exam(models.Model):
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    doctor = models.CharField('Nome do profissional', max_length=255, blank=True, null=True)
    date = models.DateTimeField('Data', auto_now_add=True)
    weight = models.FloatField('Peso', blank=True, null=True)
    height = models.FloatField('Altura', blank=True, null=True)

    class Meta:
        db_table = 'exam'
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'

    def __str__(self):
        return self.date
