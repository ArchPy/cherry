
import os
os.system("cls")
import socket
import time
import threading
from queue import Queue
import pygame
import random
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import urllib 
import re
import binascii
import sys
from datetime import datetime
socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print("""
\u001b[32m   __.--~~.,-.__      
\u001b[32m   `~-._.-(`-.__`-.
\u001b[32m           \    `~~`
      \u001b[31m.--.\u001b[32m/ \                \u001b[36m/                  
     \u001b[31m/\u001b[37m#  \u001b[31m \  \u001b[32m \u001b[31m.--.    \u001b[36m   _. /_  _  __  __  __  ,      _   
     \u001b[31m\    /  /\u001b[37m# \u001b[31m  \    \u001b[36m (__/ /_</_/ (_/ (_/ (_/_  o  /_)_(_/_
      \u001b[31m'--'   \    /       \u001b[36m                   /      /     /  
              \u001b[31m'--'        \u001b[36m                  '      '     '   
    \u001b[33m[v1.0.0 , written by arch. <@arch.py on instagram>]
""")
print(""" \u001b[36m
            .-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-.
            |\u001b[37m Welcome To Cherry. Choose The Tool You Want To Use!\u001b[36m |
            | ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
            | [1] DNS Look Up Tool                                |
            |                                                     |
            | [2] Port Scanner Tool                               |
            |                                                     |
            | [3] Doxx Compiler Tool                              |
            |                                                     |
            | [4] Web Server Status Tool                          |
            |                                                     |
            | [5] Snake Game                                      |
            |                                                     |
            | [6] DDoS Panel (Hard Hitting)                       |
            |                                                     |
            | [7] Help / Contact Info                             |
            '-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-'         
""")
toolnum = int(input("\t\t\t\u001b[35mUser Input:\u001b[36m "))
print()
print()
print()
print()
print()
print()

if toolnum < 1:
    print("\t\t\u001b[31mOops! It looks like you chose an invalid option. Rerun Cherry and try again.")
if toolnum > 7: 
    print("\t\t\u001b[31mOops! It looks like you chose an invalid option. Rerun Cherry and try again.")

if toolnum == 1:
    addr = input('\n\n\t\t\tEnter the URL to get the IP of!\n\n\t\t\t\u001b[35mUser Input:\u001b[36m ')
    addr1 = socket.gethostbyname(addr)
    print ('\n\n\t\t\tThe IP address of', addr, 'is', addr1, '!')

if toolnum == 2:
      target = input('\n\n\t\t\tEnter the IP adress you would like to scan!\n\n\t\t\t\u001b[35mUser Input:\u001b[36m ')
      t_IP = socket.gethostbyname(target)
      print ('\n\n\t\t\tInitiating a scan on', t_IP, '!')
      print()
      def portscan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
          con = s.connect((t_IP, port))
          with print_lock:
            print('\t\t\tPort', port, 'is open!')
          con.close()
        except:
          pass


      def threader():
        while True:
          worker = q.get()
          portscan(worker)
          q.task_done()

      q = Queue()
      startTime = time.time()
   
      for x in range(100):
         t = threading.Thread(target = threader)
         t.daemon = True
         t.start()
   
      for worker in range(1, 1023):
         q.put(worker)
   
      q.join()
      print('\n\n\t\t\tTime scanned: ', time.time() - startTime)

if toolnum == 3:
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("""\u001b[36m
    .-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-.
    | Welcome to the Cherry.py Doxx Compiler tool. Please note  |
    | that this tool won't give you anyone's information. This  |
    | tool is simply to format all of the information you have  |
    | on an individual, so it looks pretty in screenshots. If   |
    | you do not have the piece of information that the AI is   |
    | asking for, you can simply put in a random input, like    |
    | "?" or "null," to show you do not have that information.  |
    | The author of this script does not take any responsibility|
    | for crimes commited or damage done while using this tool. |
    | If you have any suggestions, DM the author on Instagram at|
    | @arch.py - Stay safe, and be smart.                       |
    '-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-'
    """)
    print("\n\n\t\t\tBeginning stage ONE of TWO: Collecting Data.")
    fname = input("\n\n\t\t\tTarget FIRST NAME: ")
    midint = input("\n\n\t\t\tTarget MIDDLE INITIAL: ")
    lname = input("\n\n\t\t\tTarget LAST NAME: ")
    targage = input("\n\n\t\t\tTarget AGE: ")
    sex = input("\n\n\t\t\tTarget SEX: ")
    email = input("\n\n\t\t\tTarget EMAIL: ")
    phonenum = input("\n\n\t\t\tTarget PHONE NUMBER: ")
    instagram = input("\n\n\t\t\tTarget INSTAGRAM: ")
    ipaddr = input("\n\n\t\t\tTarget IP ADDRESS: ")
    country = input("\n\n\t\t\tTarget COUNTRY: ")
    state = input("\n\n\t\t\tTarget STATE: ")
    city = input("\n\n\t\t\tTarget CITY: ")
    streetaddr = input("\n\n\t\t\tTarget STREET ADDRESS: ")
    tarzip = input("\n\n\t\t\tTarget ZIP CODE: ")
    creds = input("\n\n\t\t\tDOXXED BY: ")
    print("\n\n\t\t\tInformation received, compiling doxx.........................................................................")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print("""
\t\t\u001b[32m   __.--~~.,-.__      
\t\t\u001b[32m   `~-._.-(`-.__`-.
\t\t\u001b[32m           \    `~~`
\t\t      \u001b[31m.--.\u001b[32m/ \                \u001b[36m/                  
\t\t     \u001b[31m/\u001b[37m#  \u001b[31m \  \u001b[32m \u001b[31m.--.    \u001b[36m   _. /_  _  __  __  __  ,      _   
\t\t     \u001b[31m\    /  /\u001b[37m# \u001b[31m  \    \u001b[36m (__/ /_</_/ (_/ (_/ (_/_  o  /_)_(_/_
\t\t      \u001b[31m'--'   \    /       \u001b[36m                   /      /     /  
\t\t              \u001b[31m'--'        \u001b[36m                  '      '     '   
\t\t    \u001b[33m[v1.0.0 , written by arch. <@arch.py on instagram>]
""")
    print("\t\t\t\u001b[36mA Doxx By", creds,"Using cherry.py !!")
    print()
    print("\t\t\u001b[33m.-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-.")
    print()
    print("\t\t \u001b[36mTarget Name:        \u001b[33m", fname, midint, lname)
    print()
    print()
    print("\t\t \u001b[36mTarget Age:         \u001b[33m", targage)
    print()
    print()
    print("\t\t \u001b[36mTarget Sex:         \u001b[33m", sex)
    print()
    print()
    print("\t\t \u001b[36mTarget Email:       \u001b[33m", email)
    print()
    print()
    print("\t\t \u001b[36mTarget Phone:       \u001b[33m", phonenum)
    print()
    print()
    print("\t\t \u001b[36mTarget Instagram:   \u001b[33m", instagram)
    print()
    print()
    print("\t\t \u001b[36mTarget IP:          \u001b[33m", ipaddr)
    print()
    print()
    print("\t\t \u001b[36mTarget Home Address:\u001b[33m", streetaddr, ";", city, ",", state, tarzip)
    print()
    print()
    print("\t\t \u001b[36mTarget Country:     \u001b[33m", country)
    print()
    print("\t\t\u001b[33m'-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-'")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")

if toolnum == 4:
    req = Request(input('\n\n\t\t\t\u001b[36mEnter the webserver to check status of:\u001b[31m '))
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('\n\n\t\t\t\u001b[36mThe site is offline!!')
        print('\n\n\t\t\t\u001b[36mError code:\u001b[31m ', e.code)
    except URLError as e:
        print('\n\n\t\t\t\u001b[36mFailed to reach the server.\u001b[31m :(')
        print('\n\n\t\t\t\u001b[36mReason:\u001b[31m ', e.reason)
    else:
        print ('\n\n\t\t\t\u001b[36mThe site is online!!')

if toolnum == 5:
  pygame.init()
 
  white = (255, 255, 255)
  yellow = (255, 255, 102)
  black = (0, 0, 0)
  red = (213, 50, 80)
  green = (0, 255, 0)
  blue = (50, 153, 213)
 
  dis_width = 600
  dis_height = 400
 
  dis = pygame.display.set_mode((dis_width, dis_height))
  pygame.display.set_caption("Cherry.py Snake Game")
 
  clock = pygame.time.Clock()
 
  snake_block = 10
  snake_speed = 15
 
  font_style = pygame.font.SysFont("bahnschrift", 25)
  score_font = pygame.font.SysFont("bahnschrift", 35)
 
 
  def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0, 0])
 
 
 
  def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])
 
 
  def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
  def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(black)
            message("You lost!! Q to quit, C to play again!!", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
  gameLoop()

if toolnum == 6:
    print("""\u001b[34m
#########################%%%%%&%%##(##%%%#%%%%%%%%%%%###(##((##%%##((((######%#%%%%%%######%%%%###(((((((##%%%#%%%%%%%%%%#%%&&%%###########(((########
#######################%%%%%%&%####%%%%%%#%%%%%%&%%%####(((((***,,,,,*,/(#%%%%%%%%%%%%%###%%#%###((#((((##%%#%%%%%%%&%&%%#%%%&&%%%#######((((#########
###################%%%#####%%%%###%%%%%%%%%%&%%#######(((*,,,,,,,,,,,*,,**(%%%#%%%%%%##(######((((##((((((##%%%%%%%%&&&&%%####%%&%%%%#(((((((#########
################%%%%%%%%%########%%%%%%%%##########%((/,,,,,,,,,,,,,,,,.,*(%%%%%%%%%####%%%###((##%(#((####(#((#%%%%%&&&&&%###%%&%##((###((((#########
###############%%%%%%%%%%#######%%%%&&%###########%/*,,,,,,,,,******//**/####%%%%#####%%&%%%%%%#((#((((##%%#(((###(##%%%%%%%##########%%%%############
###########%%%%%%&%%%&%%%%%%###%&&%%######%%%%%%##(*,,,,,,,,,*/(((((((((((%%######%%&%%&%%%%%%%%##(((((##%%######%#((##%&&&&&%%###((%%%%%%%%##########
###########%%%%%&%%%%%%%%%%%%############%%%%%%%##/,,,,,,,,,**///(((((((((%%%%###%%%%%%%%%%%%%%%%###((((#%#(##%%%%%(#####%%&&#####%%%%%%%%%%&%%%######
###########%%%%&&&%%%%%%%%%########%%%%%###%%%%###*,,,,,,,,,*///////(///(/########%%%%%%%%%%%%%%%##(((##((#%(#####%####(######(###%%%%%%%%%&&%&&&%####
#####%&###%&%%%%&%%%%%&%%%%%###%%%###%%##%%####%%%/,,*///****///(((((((((#####%#######%%%%%%%%%%%##(#((###%%%#######(#%%%%####(###%%%%%%%%%&&%&&&%%%%#
###%%%%%###%%%%&%%%&%%%%%%%####%%%%#####%%%&%%#%&%%/,*//*/////////(((((//(#%%%%%%%%(#####%%%%%%##(###(#(#%%%%%###(%####%#(##%%###%%%%%%&&&&&&&%&&%%%%%
#%%%###########%%%%%%%%#########%%%%%###%%%%&&##%%%%/,*////////////((((((##%%%%%%%%###(((#%%#((#####((#(#%%%%%##%%%%%#((##%%%%##(#%%%%%%&&&%&&&&&%%%%&
################%%%%######################%%%&%#%&%%%(/////////////(////(##%%%%%%%%#%##%#(#####((((##(((##%#%##%%&&%%####%%%##########%&&&&%&%##%%%%&&
###%%%%%%%%%%%%%#####%%%%%%%%%%%%%####%####%%&&##%%#%(/////////*////((((###%%%%%%%%%%##%##%%%%%%##((((((#%%%%##%%&&%#######(((#(#####%%%%&%%%%%%%%%%%#
###%%%%%%%%%%%%######%%%%%%%%%%%%##(#%%##((##%%##/*(/////////////*/////(((###%%%%%%##########%%%%%###((##%%##(%%%&%##%%%###%%%%%%%%&&&%##%%##%&&&%%%&&
####%%%%%%&%%%%######%%%%%#%%%#%%#((#%##((((((/*,,.,(/////////(((((#%%%(((((##%%%#((((#%%%#####%#%%#(((((((###(#%%##%%%&####%%&%%%%&&&&&%###%&&%&&&&&&
###%%%%%%%%#%%%%###%%#%%%##%%%##%#(((((((/,,,,....../(#////(///((/(#*,////((((((((((#%#%%%%%##(###(((((((#%%#%#########%%####%%%&%%&%%&%#####%&%&&&&&%
###########%%%%%###%%%%%###%#%#((((/*,,,............./##(//((//(*/##(,****/(.,,*(#%#%%%%%%%%%##((((#(((((#%%#%%######%###((##%%%%%%&&%%%%%##%&&&&&&&&&
%%######(#(########%##((((((((/*,,...................(((##((((/*/####*****//,,.,,,,,#%#%%%%%###(##(((((((#%##%##(#####%%%#((#(###%##%%%%%%##%&&&&&&%%%
#%%#(#%%%#%##(((((((((#######*........................(##(((((#####(,*****//,,,,,,,,,###%%%##(((#%%#(((((#%###(##%%#(##%%%&%%########(##%%##%%%%%#####
#%#(##%%%%#%%###(((##%######*,........................,.,/(#(/*,,,,.,,****/*,,.,,,,.,/#####(((((####(((((##%#(((#%%#(##%%&%&&&###%%%%%#(########%%%&%%
((###%%#%%#%%%##((#########(,............................,,*/(#(/*,.,..*//*,.,.,.....,###((##(((##(((((((###((((#%%%#(#%%%%&%####%%%%%%%######%&%&&%&&
(#####%%%%####((((((#######/..............................,..*(##(*.,,,/((*,........,,(######((((((((((((##((%#(((#%%###%%%%####%%##%%%%%%%###&%%%&&&&
%#####(#%%###((##((((#####*,..............................,*,,*/(#/,,.,(((*,..........(####(((##((###(((((((((((((((####%%%######%%%%%%%#####(#%%%&&&%
%%%%##(###((#######(((((((.................................**,,,/(*.,..**/,..........,/###((######(((((((((((##%%%#((#(####%&&&%%###%&%######(###%&&%#
########(########(####((#,................................../*,,*/,..,,,*,...........,,#############(((((((##%%#%%%%######%%&&&&&%######%%%%%%%%######
#%#%%%%####%%%########((*,..................................,/*,,*,.,,.,*,...........,,##############((((((##(##################################%####%
#%#%%%%((##%%%#######(((..............   ....................,/**//*,..,*,...........,./(##########((((((((((####%%%%####%&&&&&%&%%%###%%%%%%%%&&%%#%%
#%%%%%##((#%#%#######(((...............    . ....    .. ..,**////*****,,*,.............,##########((#(((((((((##%%%######%%&&&&&&&&&###%&%%%%%%&&%###%
#%%%%%###(#%#########(#/..............       ..... ... .,*****//////*..,*,..............(##(##########(((((##(((#(#(#%####%%%%%%%%%&###%%%%%%##%%%###%
#%#%#%#(#(###########((/,.................  .. .........,*****//////,..,*,.............,(##############((((#####(##%%%####%%%%&&&&&&####%%%%%%%&&%###%
((((((((((((#((((((((((.................................,*****/////,...,*,.............../##############(((####(((#%%%%###%%%%%%&%%%####%%%%%#%&&%####
########(#####((((###((,............................... ..,,...  ......,*......... ....... ...,/###(///###(###((((###%####%########%####%#%####%%%####
######(((#########(##((#,............................,...  ..... ......,*.................    ...,***///////(((####(######%#%#%##%###(((#######%%#####
(#####(((############(((#*........................       .. .... ......,*........              .,,,********//(##((/((((((########%##((((##%####%%%####
((((##((((((((((((((((((###########(*,..........             ... .  ...,*....,,......         ...,*****//***/#/**(####((((########(##(((#########%####
(((((((((((((((((((((((((########((#*,,....................  ..  .  ...,*........*####/*.... .    ..,*****/((*/(#(#//##(((#(((((#(((((((((############
(((((((((((((((((((((((((((((((##((#,*,...................       .,*,..,*........*############((/*,..../##((###((######(((##########((((((##########(#
(((((((((((((((((((((((((((######(((,*,.................         .*,,..,*........,####################################(########(#(((((((((##########((
((((((((((((((((((((((((((((((((((((*,..................         .***,.,*..... ...(#############################################################((((((
(((((((((((((((((((((((((((((((((((//..................           ****,,*.........(############################################(#######(########((((((
                    
                    \u001b[31mGET RICK ROLLED LOL, but seriously, don't be a little bitch! Booting innocent sites is for skids.
                    
                    
                    
                    Hope you enjoyed the script, let me know if you have any suggestions.""")
if toolnum == 7:

    print("""
    \u001b[36m
            .-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-.
            | Having trouble? Don't sweat it. Here's a rundown of all the included tools, what |
            | they do, how to use them, the update logs, and the author's contact information. |
            '-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-'

            .-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-.
            | [1] DNS Look Up Tool: This tool is designed to give you the IP address of a web  |
            | site. To use it, input a website name, like "google.com". The program will then  |
            | tell you the IP of the web server. Pretty simple.                                |
            |                                                                                  |
            | [2] Port Scanner Tool: This tool is designed to list all the open ports of an IP |
            | address. Simply give it an IP address to scan, and it will tell you which ports  |
            | (in range 1-1023) are open.                                                      |
            |                                                                                  |
            | [3] Doxx Compiler Tool: This tool uses the input function to organize info. The  |
            | script asks the user to input sets of data until it forms a full profile of the  |
            | target. Afterwards, it prints it all nice and pretty.                            |
            |                                                                                  |
            | [4] Web Server Status Tool: This tool checks the status of a webserver. Simply   |
            | input an URL like "discord.com" and it will tell you if it is up or not. If it is|
            | down, it'll show you the error code!                                             |
            |                                                                                  |
            | [5] Snake Game: What can I say? It's a good ol' fashioned snake game. Hackers    |
            | get restless too!                                                                |
            |                                                                                  |
            | [6] DDoS Panel: A very real and very hard-hitting DDoS panel for you to hack the |
            | government with. Put your haxxor skills to use and boot random people off the    |
            | internet, because why not, right?                                                |
            |                                                                                  |
            | [7] Help: Displays this message right here!                                      |
            '-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-'

            .-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-.
            | Update Log:                                                                      |
            | 11/04/2021: Woah, looks like you're on v1.0.0! What an OG!                       |
            '-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-'

            .-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-.
            | Contact Info:                                                                    |
            |                                                                                  |
            | Email: havoc.arch@protonmail.ch                                                  |
            |                                                                                  |
            | Instagram: @arch.py                                                              |
            |                                                                                  |
            | Discord: https://discord.gg/nptdnSf6dn                                           |
            '-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-'

    
    
    
    
    """)