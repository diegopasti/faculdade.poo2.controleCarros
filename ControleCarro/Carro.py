'''
Created on 10/07/2014

@author: Diego
'''
from Componentes import Freio, Acelerador, Ignicao
from Mediador import ControleComponentes
from Memento import Velocimetro

class Carro():
    
    Velocimetro = None

    Ignicao = None
    Acelerador = None
    Freio = None
    
    ControleComponente = None
    
    def __init__(self,*args):
        self.ControleComponente = ControleComponentes()
        self.Freio = Freio(self.ControleComponente)
        self.Acelerador = Acelerador(self.ControleComponente)
        self.Ignicao = Ignicao(self.ControleComponente)
        
        self.Velocimetro = Velocimetro()
        self.ControleComponente.registrarVelocimetro(self.Velocimetro)
        
    def frear(self):
        self.Freio.pressionar()

    def desfrear(self):
        self.Freio.despressionar()

    def acelerar(self):
        self.Acelerador.pressionar()

    def desacelerar(self):
        self.Acelerador.despressionar()        

    def ligar(self):
        self.ControleComponente.ignicaoLigada()

    def desligar(self):
        self.ControleComponente.ignicaoDesligada()
