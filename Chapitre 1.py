#https://www.ascii-art-generator.org/
import random
import time
import sys
import textRPG

stats_heros = []

textRPG.dialogue('\u001b[31m-Tavernier: \u001b[0mJeune aventurier, comment vous appelez vous ?\n')
stats_heros[0] = str(input('->  '))
textRPG.dialogue('-Tavernier: enchanté, ' + stats_heros[0] + ' !\n')
time.sleep(2)
textRPG.dialogue("-Tavernier: vous m'avez l'air vigoureux, jeune homme. Nous aurions besoin de vos services !\n")
time.sleep(0.5)
textRPG.dialogue("-Client: en effet, des brigands vont venir d'un moment à l'autre pour nous soutirer notre argent...\n")
time.sleep(0.5)
textRPG.dialogue("-Tavernier: ces salauds viennent nous piller tous les mois !\n")
time.sleep(0.5)
textRPG.dialogue("-Tavernier: pourriez vous nous aider à nous defendre ? (ce travail serait evidemment rémunéré)\n")
time.sleep(0.5)
textRPG.dialogue('Narateur: acceptez vous cette quete ? (oui/non)\n')
quete1_acceptee = input('->  ')
time.sleep(0.5)
if quete1_acceptee == 'oui':
    textRPG.dialogue("-Tavernier: c'est un homme brave que nous avons là !\n")
elif quete1_acceptee == 'non':
    textRPG.dialogue("-Client: c'est donc un pleutre que nous avons en face de nous!\n")
else:
    textRPG.dialogue("Narateur: vous venez d'avoir une absence et n'avez rien compris à la conversation\n")
time.sleep(0.5)
textRPG.dialogue('*vous sortez de la taverne\n')
time.sleep(0.2)
textRPG.dialogue('-Passant: ils arrivent\n')

