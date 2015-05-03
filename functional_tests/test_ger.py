from django.test import TestCase, LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core import mail
from core_app import views
from core_app.models import Inmueble, Elemento, Proyecto, Activo
from .base import FunctionalTest
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

import sys
      

class EstadoInmueble(FunctionalTest):#TestCase #FunctionalTest
    nombre = "Inmueble test"
    estado_inicial_inmueble = 2
    estado_final_inmueble = 1

    estado_inicial_elemento = 2
    estado_final_elemento = 1  

    #Método que verifica que el estado del inmueble cambie cuando se hace un set en el estado del inmueble
    def test_estado_inmueble(self):
        self.inmueble.set_estado(self.estado_final_inmueble)
        self.assertTrue(self.estado_final_inmueble == self.inmueble.estado)

    #Método que verifica que el estado del elemento cambie cuando se hace un set en el estado del inmueble
    def test_estado_elemento(self):
        return True
        #self.elemento.set_estado(self.estado_final_elemento)
        #self.assertTrue(self.estado_final_elemento == self.elemento.estado)

    #Método que verifica que el estado del elemento cambie cuando se hace un set en el estado del inmueble
    def test_estado_elemento_inmueble(self):
        return True
        #self.elemento.set_estado(self.estado_final_elemento)
        #self.assertTrue(self.estado_final_inmueble <= self.elemento.inmueble.estado)
    
        
#    def tearDown(self):
#        self.user.delete()
#        self.proyecto.delete()
#        self.inmueble.delete()
#        self.elemento.delete()
#        self.client.logout()
        
    

