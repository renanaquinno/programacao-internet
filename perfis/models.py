from django.db import models

# Create your models here.

class Perfil(models.Model):
        nome = models.CharField(max_length=20)
        email = models.EmailField(max_length=30)
        telefone = models.CharField(max_length=11)
        nome_empresa = models.CharField(max_length=255)
        contatos = models.ManyToManyField('self')

        def convidar(self, perfil_convidado):
                Convite(solicitante=self, convidado=perfil_convidado).save()

class Convite(models.Model):
        solicitante = models.ForeignKey(Perfil, related_name='convites_feitos', on_delete = models.CASCADE)
        convidado = models.ForeignKey(Perfil, related_name='convites_recebidos', on_delete = models.CASCADE)

        def aceitar(self):
                self.convidado.contatos.add(self.solicitante)
                self.solicitante.contatos.add(self.convidado)
                self.delete()