import pywhatkit
import keyboard
import time
from datetime import datetime

contatos = ['+5516988099240']

while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0], 'EU TE AMO AMOR ', datetime.now().hour,datetime.now().minute + 2)
