'''
Created on 10/07/2014

@author: Diego
'''

class Componente():

    Mediador = None
    Ativo = None

    def __init__(self,*args):
        pass

    def desativar(self):
        print "Desativando: ",self
        self.Ativo = False

    def ativar(self):
        print "Ativando: ",self        
        self.Ativo = True

class Freio(Componente):

    def __init__(self,mediador):
        self.Mediador = mediador
        self.Mediador.registrarFreio(self)

    def despressionar(self):
        if(self.Ativo):
            self.Mediador.freioDespressionado()
        else:
            print "Freio desabilitado"

    def pressionar(self):
        if(self.Ativo):
            self.Mediador.freioPressionado()
        else:
            print "Freio desabilitado"

class Acelerador(Componente):

    def __init__(self,mediador):
        self.Mediador = mediador
        self.Mediador.registrarAcelerador(self)

    def despressionar(self):
        if(self.Ativo):
            self.Mediador.aceleradorDespressionado()
        else:
            print "Acelerador desabilitado"

    def pressionar(self):
        if(self.Ativo):
            self.Mediador.aceleradorPressionado()            
        else:
            print "Acelerador desabilitado"
    
class Ignicao(Componente):

    def __init__(self,mediador):
        self.Mediador = mediador
        self.Mediador.registrarIgnicao(self)

    def ligar(self):
        self.Mediador.ignicaoLigada()

    def desligar(self):
        self.Mediador.ignicaoDesligada()

