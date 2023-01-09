import random
import time
import sys

stats_heros = []
stats_ennemi = []

def dialogue(texte):
    for x in texte:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.05)

def mort():
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⣠⣔⡿⠛⠒⠒⡕⢄⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⣀⣴⣳⠃⠀⠀⠀⠀⠘⢎⡦⣄⠀⠀⠀⠀\n⠀⠀⠀⣜⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⣳⠀⠀⠀\n⠀⠀⢸⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡆⠀⠀\n⠀⠀⠘⡏⢀⢴⠶⣤⢄⢲⣲⠦⣦⣤⡤⡀⡇⠇⠀⠀\n⠀⠀⠀⣧⠀⣾⢀⣸⡸⠘⢸⠀⣿⠀⣸⡏⣧⠀⠀⠀\n⠀⠀⠀⢹⠀⣿⠿⡯⡀⢀⣼⢀⣿⠛⠉⠀⢻⠀⠀⠀\n⠀⠀⠀⣿⠐⠛⠂⠘⠛⠒⠛⠊⠛⠂⠀⢸⢸⠀⠀⠀\n⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡼⠀⠀⠀\n⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀\n⠀⠀⢀⢾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⡀⠀⠀\n⠀⣠⠃⠘⠊⠉⠛⠛⠋⠩⠩⠭⠍⠛⠛⠛⠃⠐⡄⠀\n⠀⣯⡉⠉⢉⡉⠉⠉⠉⠉⠉⠉⣉⣉⣉⣉⣉⣉⣹⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⡴⡤⡤⣤⡤⡤⣤⣤⢠⣤⣤⠀⢰⡄⣤⣶⡴⢶⣶⡴')
    exit()


'''
données stockées sous forme de liste
def combat(stats_heros,stats_adversaire):

'''
#nom,hp,hp_max,atk,def,speed,dmg_rndm,dmg_fixe

def combat(nom_heros,hp_heros,hp_max_heros,attaque_heros,defense_heros,vitesse_heros,attaque_random_heros,attaque_fixe_heros,nom_ennemi,hp_ennemi,hp_max_ennemi,attaque_ennemi,defense_ennemi,vitesse_ennemi,attaque_random_ennemi,attaque_fixe_ennemi):
    if random.randint(20)+vitesse_heros > random.randint(20)+vitesse_ennemi:
        #heros attaque en premier
    else :
        #ennemi attaque en premier
