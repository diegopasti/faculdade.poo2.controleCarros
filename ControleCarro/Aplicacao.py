'''
Created on 10/07/2014

@author: Diego
'''
from Carro import Carro


def RealizarTestDrive():
    print
    print "####################################"
    print "##           TEST DRIVE           ##"
    print "####################################"
    
    Veiculo = Carro()
    Veiculo.ligar()
    Veiculo.acelerar()
    Veiculo.desacelerar()
    Veiculo.frear()
    Veiculo.desligar()

def RealizarTesteTacografo():
    print
    print "####################################"
    print "##         TEST TACOGRAFO         ##"
    print "####################################"
    
    Veiculo = Carro()
    Veiculo.ligar()
    Veiculo.acelerar()
    Veiculo.acelerar()
    Veiculo.acelerar()
    Veiculo.acelerar()
    Veiculo.acelerar()
    Veiculo.ControleComponente.Tacografo.MarcarVelocimetro()
    Veiculo.acelerar()
    Veiculo.acelerar()
    Veiculo.frear()
    Veiculo.desligar()
    Veiculo.ControleComponente.Tacografo.restaurarVelocimetro()


RealizarTestDrive()
RealizarTesteTacografo()


