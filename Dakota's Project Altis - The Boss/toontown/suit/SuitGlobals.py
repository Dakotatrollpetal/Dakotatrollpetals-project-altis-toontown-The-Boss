# SuitGlobals are used to set the appearance of Cogs.
from toontown.suit import SuitDNA
from pandac.PandaModules import VBase4

SCALE_INDEX = 0 # The scale of the cog
HAND_COLOR_INDEX = 1 # The hand color
HEADS_INDEX = 2 # A list of heads
HEAD_TEXTURE_INDEX = 3 # The texture to use for the head
HEIGHT_INDEX = 4 # The height of the cog

aSize = 6.06 # Size of body type 'a'
bSize = 5.29 # Size of body type 'b'
cSize = 4.14 # Size of body type 'c'

ColdCallerHead = VBase4(0.25, 0.35, 1.0, 1.0) # Head used by Cold Caller

# Bossbots
suitProperties = {
        'f': (4.0 / cSize, SuitDNA.corpPolyColor, ['flunky', 'glasses'], '', 4.88),
      'p': (4.35 / bSize, SuitDNA.corpPolyColor, ['telemarketer'], 'telemarketer.jpg', 5.0),
      'ym': (4.125 / aSize, SuitDNA.corpPolyColor, ['legaleagle'], '', 5.28),
      'mm': (5.0 / cSize, SuitDNA.corpPolyColor, ['coldcaller'], '', 6.25),
      'ds': (5.5 / bSize, SuitDNA.corpPolyColor, ['movershaker'], '', 7.08),
      'hh': (6.5 / aSize, SuitDNA.corpPolyColor, ['middleman', 'downsizerHat'], '', 7.45),
      'cr': (6.75 / aSize, SuitDNA.corpPolyColor, ['pennypincher'], '', 8.23),
      'tbc': (7.0 / aSize, SuitDNA.corpPolyColor, ['headhoncho'], 'head-honcho.jpg', 9.34),

      # Lawbots
      'bf': (4.0 / cSize, VBase4(0.25, 0.25, 0.5, 1.0), ['moneybags'], '', 4.81),
      'b': (4.375 / bSize, VBase4(0.25, 0.25, 0.5, 1.0),['pencilpusher'], '', 6.17),
      'dt': (4.25 / aSize, VBase4(0.25, 0.25, 0.5, 1.0), ['twoface'], 'mingler.jpg', 5.63),
      'ac': (4.35 / bSize, VBase4(0.25, 0.25, 0.5, 1.0), ['downsizer', 'group1', 'group2'], '', 6.39),
      'bs': (4.5 / aSize, VBase4(0.25, 0.25, 0.5, 1.0), ['numbercruncher'], 'name-dropper.jpg', 6.71),
      'sd': (5.65 / bSize, VBase4(0.25, 0.25, 0.5, 1.0), ['movershaker'], '', 7.9),
      'le': (7.125 / aSize, VBase4(0.25, 0.25, 0.5, 1.0), ['headhunter'], '', 8.27),
      'bw': (7.0 / aSize, VBase4(0.25, 0.25, 0.5, 1.0), ['middleman'], '', 8.69),

      # Cashbots
      'sc': (3.6 / cSize, SuitDNA.moneyPolyColor, ['bigfish'], '', 4.77),
      'pp': (3.55 / aSize, SuitDNA.moneyPolyColor, ['bigwig'], '', 5.26),
      'tw': (4.5 / cSize, SuitDNA.moneyPolyColor, ['flunky'], 'corporate-raider.jpg', 5.41),
      'bc': (4.4 / bSize, SuitDNA.moneyPolyColor, ['ambulancechaser'], '', 5.95),
      'nc': (5.25 / aSize, SuitDNA.moneyPolyColor, ['backstabber'], '', 7.22),
      'mb': (5.3 / cSize, SuitDNA.moneyPolyColor, ['micromanager'], '', 6.97),
      'ls': (6.5 / bSize, SuitDNA.moneyPolyColor, ['telemarketer'], '', 8.58),
      'rb': (7.0 / aSize, SuitDNA.moneyPolyColor, ['pennypincher'], 'swindler.jpg', 8.95),

      # Sellbots
      'cc': (3.5 / cSize, VBase4(0.55, 0.65, 1.0, 1.0), ['conartist'], '', 4.63),
      'tm': (3.75 / bSize, SuitDNA.salesPolyColor, ['loanshark'], '', 5.24),
      'nd': (4.35 / aSize, SuitDNA.salesPolyColor, ['yesman'], '', 5.98),
      'gh': (4.75 / cSize, SuitDNA.salesPolyColor, ['toxicleader'], '', 6.4),
      'ms': (4.75 / bSize, SuitDNA.salesPolyColor, ['movershaker'], 'blood-sucker.jpg', 6.7),
      'tf': (5.25 / aSize, SuitDNA.salesPolyColor, ['bigcheese'], '', 6.95),
      'm': (5.75 / aSize, SuitDNA.salesPolyColor, ['yesman'], 'robber-baron.jpg', 7.61),
      'mh': (7.0 / aSize, VBase4(0, 0.00, 0.0, 0.0), ['legaleagle'], 'magnate.jpg', 8.95),

      # Boardbots
      'ca': (4.0 / cSize, SuitDNA.boardPolyColor, ['tightwad'], '', 4.88),
      'cn': (3.75 / bSize, SuitDNA.boardPolyColor, ['beancounter'], '', 5.24),
      'sw': (4.34 / aSize, SuitDNA.boardPolyColor, ['numbercruncher'], '', 5.45),
      'mdm': (5.0 / aSize, SuitDNA.boardPolyColor, ['backstabber'], '', 6.7),
      'txm': (5.25 / cSize, SuitDNA.boardPolyColor, ['tightwad'], 'bottom-feeder.jpg', 7.2),
      'mg': (6.5 / aSize, SuitDNA.boardPolyColor, ['yesman'], 'mingler.jpg', 7.26),
      'bfh': (7 / cSize, SuitDNA.boardPolyColor, ['gladhander'], '', 10.0),
      'hho': (7.0 / aSize, SuitDNA.boardPolyColor, ['twoface'], '', 8.23),
}