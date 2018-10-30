from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


class Usuario(AbstractBaseUser):
    username = models.CharField(_('usuario'), max_length=15, unique=True, help_text =_('Requer 15 caracteres ou menos'))
    password = models.CharField(_('senha'), max_length=15, help_text=('Digite uma senha com 15 caracteres ou menos'))
    email = models.EmailField(_('email'), max_length=255,unique=True)
    funcao = models.CharField(max_length=40)
    matricula = models.IntegerField()

    def __str__(self):
        return self.username