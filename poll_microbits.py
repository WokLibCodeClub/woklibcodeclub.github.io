# Add your Python code here. E.g.
from microbit import *
import radio
from random import getrandbits

######################################################
# THIS CODE WILL NOT WORK UNLESS THE MICROBIT IS
# CONNECTED TO A COMPUTER.
#
# IF THE MICROBIT IS NOT CONNECTED AND RUNNING ON A
# BATTERY PACK THE CODE WILL HANG AT THE input() LINE
######################################################

version = 'v1.1'
# correct spelling of protocol
protocol = 'v1.1'

#Init vars
radio.config(group=7,power=7)
radio.RATE_2MBIT
# generate random 32bit binary number (UUIDs are usually 128 bits)
UUID = getrandbits(32)
# make debug and autoFind Boolean variables
debug = True
autoFind = False
# turn on radio
radio.on()

#Handling Debuging
tempsend = 'MBIT: ' + str(UUID)
# This alternative version will give the UUID in binary
#tempsend = 'MBIT: ' + '{:034b}'.format(UUID)
if debug: # will run if debug == True
    print(protocol)
    print(tempsend)
display.scroll(tempsend)
tempsend = ''

#Nessiary init
UNAME = input('Please enter a username: ')

# forever loop
while True:
    message = radio.receive()
    
    if button_a.was_pressed():
        askContent = input('Type Something: ')
        radio.send(UNAME + ':' + askContent)
        display.scroll('MSG  sent')
        sleep(500)
        display.show(Image('99999:88888:66666:55555:44444'))
    
    if message:
        if message == 'Find_Detect':
            tempsend = 'MBIT: ' + str(UUID)
            display.scroll('sending UUID')
        else:
            display.scroll(message)
            if debug:
                print(message)
            sleep(500)
            display.show(Image('44444:55555:66666:88888:99999'))
    
    if button_b.is_pressed():
        display.scroll('Scanning for nearby compatible microbits')
        radio.send('Find_Detect')
        display.show(Image('99999:88888:66666:55555:44444'))
   
