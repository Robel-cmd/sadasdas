import bs
import bsGame
from terminal import Colors
from datetime import datetime
date = datetime.now().strftime('%d')


# Add New Prefix Commands:
prefixComand = ('/', '.', '-', '*', ',', '#', '!', '?', ';')
cmdlogs = True

enableTop5effects = True
enableTop5commands = False
enableCoinSystem = True

enableStats = True

# More Settings On setchat.py
spamProtection = True
shieldBomb = False
shieldBomb = False  # shield on bomb
bombLights = False
bombLights = False  # light on bomb

bombName = False # name on bomb

bigBomb = False  # hehe extra

k_msg = False  # Killing Message

k_pop = False  # Killing Message PopUp
nightMode = False
nightMode = False

enableChatFilter = True

showTextsInBottom = False

gameTexts = ['Welcome To Blitz Server', 'Use "/shop commands" to see commands available to buy.', 'Use "/shop effects" to see effects available and their price.', 'Use "/me" or "/stats" to see your '+bs.getSpecialChar(
    'ticket')+' and your stats in this server', 'Use "/buy" to buy effects that you like', 'Use "/donate" to give some of your tickets to other players', 'Use "/scoretocash" to convert some of your score to '+bs.getSpecialChar('ticket')+'\nCurrent Rate: 5scores = '+bs.getSpecialChar('ticket')+'1']

questionDelay = 90  # 60 #seconds
questionsList = {u'\u00bfCuantos dias tiene un a\u00f1o bisiesto?': '366',
        u'\u00bfUna vieja con un diente que llama a toda la gente?': 'campana',
        u'\u00bfIba una vaca de lado, luego result\u00f3 ser pescado?': 'bacalao',
        u'\u00bfTiene dientes y no come, tiene cabeza y no es una persona?': 'ajo',
        u'\u00bf videojuego  de acci\u00f3n de pepsi?': 'pepsiman',
                 'add': None,
                 'multiply': None}

availableCommands = {'nv': 10,
                     'ooh': 1,
                     'playSound': 10,
                     'box': 30,
                     'boxall': 200,
                     'spaz': 50,
                     'spazall': 100,
                     'inv': 400,
                     'invall': 800,
                     'tex': 10,
                     'texall': 40,
                     'freeze': 500,
                     'freezeall': 1000,
                     'sleep': 400,
                     'sleepall': 800,
                     'thaw': 50,
                     'thawall': 70,
                     'kill': 500,
                     'killall': 1050,
                     'end': 500,
                     'hug': 60,
                     'hugall': 100,
                     'tint': 800,
                     'md': 600,
                     'fly': 500,
                     'flyall': 1000,
                     'heal': 50,
                     'healall': 70,
                     'spawn': 250,
                     'dbomb': 5,
                     'zoe': 10,
                     'gp': 20}

availableEffects = {'ice': 500,
                    'sweat': 500,
                    'scorch': 500,
                    'glow': 400,
                    'distortion': 500,
                    'slime': 500,
                    'metal': 500,
                    'surrounder': 500,
                    'tag': 0,
                    'footprint': 550,
                    'glitchname': 1000}

nameOnPowerUps = False  # Whether or not to show the powerup's name on top of powerups

shieldOnPowerUps = False  # Whether or not to add shield on powerups

# Whether or not to show disco lights on powerup's location
discoLightsOnPowerUps = False

FlyMaps = False  # Whether or not to enable the 3D flying maps in games playlist


# Powerup distribution
dist = (('tripleBombs', 2),
        ('iceBombs', 0),
        ('punch', 0),
        ('impactBombs', 2),
        ('landMines', 2),
        ('stickyBombs', 2),
        ('shield', 0),
        ('health', 2),
        ('curse', 0),
        ('Troll', 1),
        ('Bot', 0),
        ('Rchar', 0),
        ('Bunny', 0),
        ('Tunner', 0))


def return_yielded_game_texts():
    for text in gameTexts:
        yield text


def return_players_yielded(bs):
    for player in bs.getSession().players:
        yield player

# ** TERMINAL **

# STATS
print Colors.LIGHT_CYAN+ 'Enable Stats : '+ Colors.END+ Colors.LIGHT_GREEN+ 'ON'+ Colors.END if enableStats else Colors.RED+ 'OFF'+ Colors.END
# COIN SYSTEM
print Colors.LIGHT_CYAN+ 'CoinSystem : '+ Colors.END+ Colors.LIGHT_GREEN+ 'ON'+ Colors.END if enableCoinSystem else Colors.RED+ 'OFF'+ Colors.END
# NIGHT MODE
print Colors.LIGHT_CYAN+ 'Modo Noche Activado!'+ Colors.END if nightMode else 'Modo Noche Desactivado'
# TOPS
print Colors.LIGHT_CYAN+ 'Top Effects : '+ Colors.END+ Colors.LIGHT_GREEN+ 'ON'+ Colors.END if enableTop5effects else Colors.RED+ 'OFF'+ Colors.END
