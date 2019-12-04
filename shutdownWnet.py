#!python3
# coding=utf-8
# Escrito por Leonardo Guarnieri de Bastiani






import sys
import re
from ShutdownW import ShutdownW






class ShutdownWnet(ShutdownW):




    download = True # considerar a velocidade de download
    upload = False # considerar a velocidade de upload


        

    def getState(self):
        '''obtém um número que será usado para comparar'''



        output = self.cmd('netstat -e')


        # tratando output
        matches = re.findall('\d+', output)
        download = int(matches[0])
        upload = int(matches[1])

        return download, upload







    def strVeloc(self):
        '''informação da velocidade'''
        return str(round(self.veloc/1024, 2))+' '+self.unit







    def getVeloc(self):
        '''obtem a velocidade em self.veloc'''


        download_ini, upload_ini = self.getState()
        self.sleep(self.effetive_interval)
        download_fin, upload_fin = self.getState()


        download = download_fin - download_ini
        upload = upload_fin - upload_ini



        result = -1



        if self.download:
            result = max(result, download)


        if self.upload:
            result = max(result, upload)


        if result < 0: # as vezes, a contagem do netstat -e zera e o resultado é um valor negativo
            return self.getVeloc();



        # existe um fator que devo dividir em result,
        # não sei porque, mas se eu fizer essa conta, vai bater
        result /= 5.425
        self.veloc = result / self.effetive_interval
        return self.veloc








    def setSettings(self, args):
        '''define as configurações do programa'''
        lengthargs = len(args)
        i = 1
        while i < lengthargs:
            if args[i] == '--command' or args[i] == '-c':
                i += 1 # o proximo argumento eh o comando
                self.command = args[i];
            elif args[i] == '--upload' or args[i] == '-u':
                print('Upload habilitado.')
                self.upload = True
            elif args[i] == '--nodownload' or args[i] == '-nd':
                print('Download desabilitado.')
                self.download = False
            elif args[i] == '--velocmin' or args[i] == '-v':
                i += 1 # o proximo argumento eh a velocidade
                self.veloc = int(args[i])
                print('Velocidade mínima: '+self.strVeloc())
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
        print('\t --upload ou -u \t Leva a velocidade do upload em consideração')
        print('\t --nodownload ou -nd \t Descarta a velocidade de download')
        print('\t --velocmin ou -v \t Define a velocidade mínima em bytes')
        print('\t --tempo_max ou -t \t Define o tempo máximo de espera em segundos')
        print('\t --debug \t\t Entra em modo de depuração')
        print('\t --help ou -? \t\t Exibe o modo ajuda')










def main():
    s = ShutdownWnet(sys.argv, 'KB/s', 'shutdownWnet')
    s.start()








if __name__ == '__main__':
    main()