from colorama import Fore, init
from discord.ext import commands, tasks
import threading, os, random, pyfade
from playsound import playsound

print('\033[1;34mDigite 1 Para Abrir Iniciar o SelfBot\033[m')

opcao = int(input("\033[1;35mDigite Aqui\033[m "))

if opcao == 1:
 print ("Opcao A")
 
 if __name__ == '__main__':
    os.system('cls && title Caiu Na Net Self Bot Divulgação' if os.name == 'nt' else 'clear')
    print(pyfade.Fade.Horizontal(pyfade.Colors.red_to_purple, '''


░██╗░░░░░░░██╗░█████╗░░██████╗████████╗███████╗██████╗░░░░██╗░██╗░██████╗░░█████╗░░█████╗░██████╗░
░██║░░██╗░░██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗██████████╗╚════██╗██╔══██╗██╔══██╗╚════██╗
░╚██╗████╗██╔╝███████║╚█████╗░░░░██║░░░█████╗░░██║░░██║╚═██╔═██╔═╝░░███╔═╝██║░░██║██║░░██║░█████╔╝
░░████╔═████║░██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░██║░░██║██████████╗██╔══╝░░██║░░██║██║░░██║░╚═══██╗
░░╚██╔╝░╚██╔╝░██║░░██║██████╔╝░░░██║░░░███████╗██████╔╝╚██╔═██╔══╝███████╗╚█████╔╝╚█████╔╝██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═════╝░░╚═╝░╚═╝░░░╚══════╝░╚════╝░░╚════╝░╚═════╝░


Feito por Wasted#2003
 '''))

from asyncio import sleep
 
import discum, random, time
from rich import console, print
bot = discum.Client(token=input("\033[1;35mToken:\033[m "), log=False)
memberz = []
guildz = input("\033[1;35mId do Servidor:\033[m ")
channel = input("\033[1;35mID Do Chat Do Server:\033[m ")
messag = input("\033[1;35mMensagem que o bot vai enviar:\033[m ")
timez = input("\033[1;35mDelay Entre Mensagem:\033[m ")
@bot.gateway.command
def memberTest(resp):
    if resp.event.ready_supplemental:
        bot.gateway.fetchMembers(guildz, channel)
    if bot.gateway.finishedMemberFetching(guildz):
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()
bot.gateway.run()
print("\033[1;35mCapturando Ids:\033[m ")
for memberID in bot.gateway.session.guild(guildz).members:
    memberz.append(memberID)
print('\033[0;30;33mSelf Bot  Caiu na Net\033[m')
for x in memberz:
    try:
        rand = random.randint(0,20)
        if rand == 20:
            print(f'"\033[1;35mAguardando 45 Segundos para Enviar Dm\033[m "')
            time.sleep(45)
            print(f'"\033[1;35mParando Div\033[m "')
        print(f"\033[1;35mPreparando Dm\033[m  {x}.")
        time.sleep(int(timez))
        newDM = bot.createDM([f"{x}"]).json()["id"]
        bot.sendMessage(newDM, f"{messag}")
        print(f'Enviei mensagem com sucesso para {x}.')
        playsound("ding.mp3")
    except Exception as E:
        print(E)
        print(f'Erro {x}.')