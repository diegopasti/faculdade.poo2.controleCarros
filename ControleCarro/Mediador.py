from Memento import Memento


class ControleComponentes():

    Velocimetro = None
    Tacografo = None

    Acelerador = None
    Ignicao = None
    Freio = None

    def __init__(self,*args):
        pass
    
    def ignicaoLigada(self):
        print "Ligando o veiculo"
        self.Acelerador.ativar()
        self.Freio.ativar()

    def ignicaoDesligada(self):
        self.Acelerador.desativar()
        self.Freio.desativar()
        print "Desligando o veiculo"

    def aceleradorPressionado(self):
        print "O Acelerador foi pressionado"
        self.Velocimetro.aumentarVelocidade()
        self.Freio.desativar()

    def aceleradorDespressionado(self):
        print "O Acelerador foi despressionado"
        self.Freio.ativar()

    def freioPressionado(self):
        print "O Freio foi pressionado"
        self.Velocimetro.diminuirVelocidade()
        self.Acelerador.desativar()

    def freioDespressionado(self):
        print "O Freio foi despressionado"
        self.Acelerador.ativar()
        
    def registrarVelocimetro(self, velocimetro):
        self.Velocimetro = velocimetro
        self.Tacografo = Memento(self.Velocimetro)

    def registrarIgnicao(self,ignicao):
        self.Ignicao = ignicao

    def registrarAcelerador(self,acelerador):
        self.Acelerador = acelerador

    def registrarFreio(self,freio):
        self.Freio = freio

