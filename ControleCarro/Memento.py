'''
Created on 10/07/2014

@author: Diego
'''

class Velocimetro():
    
    VelocidadeAtual = None
    VelocidadeAnterior = None
    
    def __init__(self):
        self.VelocidadeAnterior = 0
        self.VelocidadeAtual = 0
        
    def aumentarVelocidade(self):
        self.VelocidadeAnterior = self.VelocidadeAtual
        self.VelocidadeAtual = self.VelocidadeAtual + 10
    
    def diminuirVelocidade(self):
        self.VelocidadeAnterior = self.VelocidadeAtual
        self.VelocidadeAtual = self.VelocidadeAtual - 10
    
    def setVelocidadeAtual(self, velocidade):
        self.VelocidadeAtual = velocidade
        
    def getVelocidadeAtual(self):
        return self.VelocidadeAtual
    
    def setVelocidadeAnterior(self, velocidade):
        self.VelocidadeAnterior = velocidade
        
    def getVelocidadeAnterior(self):
        return self.VelocidadeAnterior
    
class Memento():
    
    Velocimetro = None
    UltimaVelocidadeAtual = None
    UltimaVelocidadeAnterior = None
    
    def __init__(self, velocimetro):
        self.Velocimetro = velocimetro
        
    def MarcarVelocimetro(self):
        print "Marcar Velocidade Atual: ",self.Velocimetro.getVelocidadeAtual()
        self.UltimaVelocidadeAnterior = self.Velocimetro.getVelocidadeAnterior()
        self.UltimaVelocidadeAtual = self.Velocimetro.getVelocidadeAtual()
        
    
    def restaurarVelocimetro(self):
        print "Restaurando o Velocimetro"
        print "Velocidade Atual: ",self.UltimaVelocidadeAtual
        print "Velocidade Anterior: ",self.UltimaVelocidadeAnterior
        self.Velocimetro.setVelocidadeAtual(self.UltimaVelocidadeAtual)
        self.Velocimetro.setVelocidadeAnterior(self.UltimaVelocidadeAnterior)
        