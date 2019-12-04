#!python3
# coding=utf-8
# Escrito por Leonardo Guarnieri de Bastiani



import subprocess
import sys
import time
import os
import platform



class ShutdownW:


    '''Classe com as funções que serão utilizadas no programa'''




    unit = 'KB/s' # unidade
    command = 'shutdown -s -t 30 -hybrid' # comando padrao a ser executado
    sec_interval = 60 # segundoes de interval
    effetive_interval = 5 # intervalo de tempo efetivo, começa bem rápido para podermos ver as medidas
    veloc_min = 15 * 1024 # velocidade minima em bytes
    count_max = 60 # tempo em segundos que o computador deve ficar com a velocidade mínima de internet
    veloc = 0 # velocidade que será usada para exibir na tela
    debug = False # modo de depuração
    count = 0 # contador simples





    def __init__(self, args, unit='', name='ShutdownWhen'):


        '''unit é a unidade que se está medindo'''


        print('/************************\n'
             +(' * %-20s *\n' % name)
             +' ************************/')


        # mudando o comando padrão no caso de Windows 7
        windowsRelease = platform.uname().release
        if windowsRelease == '7':
            # no caso de um windows 7
            self.command = 'shutdown -s -t 30'

        self.setSettings(args)



        self.unit = unit
        print('Comando: '+self.command)






    def start(self):
        # quantidade de tempo passado desde o início
        # usado para alterar o tempo efetivo de espera
        # exemplo: de 5 para testes
        # vai para 60, pq n preciso ficar vendo o qnto tá a velocidade atual
        # a todo momento
        self.ticks = 0


        # é um contador que vai de zero até
        # count_max, que é o tempo máximo
        # que a condição não é feita
        # adiciona-se os segundos de um intervalo ao outro
        self.count = 0








        while 1:


            veloc = self.getVeloc()



            if veloc < self.veloc_min:
                self.count += self.effetive_interval
                print("Velocidade baixa "+self.strVeloc()+" em "+time.strftime('%H:%M:%S')+". Tempo restante: "+str(self.count_max - self.count)+"s")

                if self.count >= self.count_max:
                    # condição de parada
                    # meu contador ultrapassou o tempo máximo sem a condição
                    break

                # se a contagem não foi zerada ainda, continua o programa
                continue



            elif self.count != 0:
                # a condição não estava sendo feita
                # e de repente ela voltou
                print("Recomeçando a contagem. Velocidade atingida: "+self.strVeloc())
                self.count = 0 # recomeça a contage
                continue



            elif self.debug or self.ticks < 10:
                # se for debug, nunca saio dos ticks
                # se a contagem de ticks for menor do que 10, continuo contando os ticks para
                # que no décimo, eu pare de contar
                self.ticks += 1


            elif self.ticks == 10:
                # já se passaram 10 intervalos de tempos
                # e os primeiros intervalos são mais rápidos
                # agora começa o verdadeiro tempo de espera
                self.effetive_interval = self.sec_interval
                self.ticks += 1





            print('Velocidade atual: '+self.strVeloc())



        print('Contagem zerada.')
        os.system(self.command)




    def sleep(self, interval):
        try:
            time.sleep(interval)
        except:
            ShutdownW.close()









    #@abstractmethod
    # funções que devem ser implementadas conforme o arquivo



    def getState(self):
        '''obtém um número que será usado para comparar'''
        pass






    def strVeloc(self):
        '''informação da velocidade'''
        return str(self.veloc)+' '+self.unit






    def getVeloc(self):
        '''obtem a velocidade em self.veloc'''
        pass






    def setSettings(self, args):
        '''define as configurações do programa'''
        pass






    @staticmethod


    def cmd(command):
        return subprocess.check_output(command).decode('iso-8859-1')





    def usage():
        '''instruções de como usar o programa'''
        pass





    def close():
        '''fim do programa'''
        print('Tchau :)')
        sys.exit(0)