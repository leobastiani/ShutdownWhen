#!python3
# coding=utf-8
# Escrito por Leonardo Guarnieri de Bastiani






import sys
import psutil
from ShutdownW import ShutdownW






class ShutdownWnet(ShutdownW):



    veloc_min = 15 # %

        

    def getState(self):
        '''obtém um número que será usado para comparar'''



        return psutil.cpu_percent()







    def strVeloc(self):


        '''informação da velocidade'''
        return str(self.veloc)+self.unit







    def getVeloc(self):
        '''obtem a velocidade em self.veloc'''


        self.sleep(self.effetive_interval)
        self.veloc = self.getState()






        return self.veloc








    def setSettings(self, args):
        '''define as configurações do programa'''
        lengthargs = len(args)
        i = 1
        while i < lengthargs:
            if args[i] == '--command' or args[i] == '-c':
                i += 1 # o proximo argumento eh o comando
                self.command = args[i];
            elif args[i] == '--velocmin' or args[i] == '-v':
                i += 1 # o proximo argumento eh a velocidade
                print('Velocidade mínima: '+self.strVeloc(int(args[i])))
                self.veloc_min = int(args[i])
            elif args[i] == '--secinterval' or args == '-i':
                i += 1
                print('Intervalo de tempo entre as medições: '+args[i]+'s')
                self.sec_interval = int(args[i])
            elif args[i] == '--tempo_max' or args == '-t':
                i += 1
                print('Tempo máximo: '+args[i]+'s')
                self.count_max = int(args[i])
            elif args[i] == '--debug':
                print('Modo de depuração')
                self.debug = True
                self.sec_interval = 5
                self.count_max = 30
                self.command = 'echo Teste realizado com sucesso!'
            elif args[i] == '--help' or args[i] == '-?':
                self.usage()
                sys.exit(0)
            i += 1








    @staticmethod


    def usage():
        '''instruções de como usar o programa'''
        print('Usage: shutdownWnet [options]')
        print('\t --command ou -c \t Comando que será executado')
        print('\t --velocmin ou -v \t Define a velocidade mínima em bytes')
        print('\t --tempo_max ou -t \t Define o tempo máximo de espera em segundos')
        print('\t --debug \t\t Entra em modo de depuração')
        print('\t --help ou -? \t\t Exibe o modo ajuda')










def main():
    s = ShutdownWnet(sys.argv, '%', 'shutdownWcpu')
    s.start()








if __name__ == '__main__':
    main()