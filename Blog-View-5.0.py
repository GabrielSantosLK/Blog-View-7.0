print('\n © 2017 Copyright TODOS OS DIREITOS RESERVADOS POR LOOCK UNDERWOOD') 
#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import webbrowser
import time
import os

print('''


 ██████╗ ██╗      ██████╗  ██████╗               ██╗   ██╗██╗███████╗██╗    ██╗    
 ██╔══██╗██║     ██╔═══██╗██╔════╝               ██║   ██║██║██╔════╝██║    ██║    
 ██████╔╝██║     ██║   ██║██║  ███╗    █████╗    ██║   ██║██║█████╗  ██║ █╗ ██║    
 ██╔══██╗██║     ██║   ██║██║   ██║    ╚════╝    ╚██╗ ██╔╝██║██╔══╝  ██║███╗██║    
 ██████╔╝███████╗╚██████╔╝╚██████╔╝               ╚████╔╝ ██║███████╗╚███╔███╔╝    
 ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝                 ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝    
     
                                                                                                                                        

 :================================================================:
 :  -  SCRIPT DE ESTUDO BASICO EM PYTHON // BY: Loock Underwood   :
 :================================================================:
 :  - TAMO JUNTO ° FELIPE MANDIOCA, ° DERICK e ° PEDRO BASTAO.    :
 :================================================================:                                                              
 :  - GRUPO : https://www.facebook.com/groups/fsocietybrasil/     :
 :================================================================:                                                            
                                                                 ''')


#=================================================================================#
print('\n #============================================================================================#')
#=================================================================================#
print("\n\n [!] Olá! Vamos dar início ao processo?\n")


print('\n #============================================================================================#')
#=================================================================================#

url = input("\n [!] Coloque a Url do Blog: ")

print('\n #============================================================================================#')
#=================================================================================#

refresh = eval(input("\n [!] Caso queira, coloque o tempo de refresh em segundos, se não quiser coloque 0: "))

print('\n #============================================================================================#')
#=================================================================================#

#brow = input("\n [!] Coloque o nome do seu Navegador (Respeitando A - a): ") #Função desabilitada por enquanto (USA Browser Default dos Sistema)
#print('\n #============================================================================================#')


vezes = int(input("\n [!] Coloque o Número de Views que desejas ganhar: "))

print('\n #============================================================================================#')

#=================================================================================#

print('\n [!] ESPERE 5 SEGUNDOS POR FAVOR.')
time.sleep(5) 

print('\n--------------------------------------')

def openurl():
        print("[!] !Views Adquiridas!")
        webbrowser.open(url)
	
print("\n")
for i in range(vezes):
        openurl()	
        time.sleep(refresh)

print('\n#========================================================================#')

print('''
KKK     KKK   III    SSSSSS     SSSSSS
KKK    KKK    III   SSSSSSS    SSSSSSS
KKK  KKKK     III   SSS        SSS
KKKKKK        III   SSSSSS     SSSSSS
KKKKKK        III   SSSSSSS    SSSSSSS
KKK  KKKK     III       SSS        SSS
KKK    KKK    III   SSSSSSS    SSSSSSS
KKK     KKK   III   SSSSSSS    SSSSSSS''')


time.sleep(5) #sleep 5 secs
