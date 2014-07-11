class ControleComponentes():

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
        print "Desligando o veiculo"
        self.Acelerador.desativar()
        self.Freio.desativar()

    def aceleradorPressionado(self):
        print "O Acelerador foi pressionado"
        self.Freio.desativar()

    def aceleradorDespressionado(self):
        print "O Acelerador foi despressionado"
        self.Freio.ativar()

    def freioPressionado(self):
        print "O Freio foi pressionado"
        self.Acelerador.desativar()

    def freioDespressionado(self):
        print "O Freio foi despressionado"
        self.Acelerador.ativar()

    def registrarIgnicao(self,ignicao):
        self.Ignicao = ignicao

    def registrarAcelerador(self,acelerador):
        self.Acelerador = acelerador

    def registrarFreio(self,freio):
        self.Freio = freio

