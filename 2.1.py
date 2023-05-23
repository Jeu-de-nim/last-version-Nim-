't'
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Thomas
#
# Created:     18/02/2023
# Copyright:   (c) Thomas 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import pygame

pygame.init()

# Générer la fenêtre de notre jeu
#titre de la fenêtre
pygame.display.set_caption("Jeu de nim")
#taille largeur sur longeur
screen = pygame.display.set_mode((1080,720))

#importer carre
carre = pygame.image.load("image_jeu/carre.jpg")

carre1 = carre

carre2 = carre

# arrière plan
carre2 = pygame.transform.scale(carre2,(1080,720))
# pour cacher les allumettes
carre1 = pygame.transform.scale(carre1,(200,210))
# pour alterner entre 1 et 2
#changer taille carre
carre = pygame.transform.scale(carre,(25,40))

running = True


class Allumette(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("image_jeu/allumette.png")
        self.image = pygame.transform.scale(self.image,(200,300))
        self.rect = self.image.get_rect()

allumette1 = Allumette()

#définir le style et la taille de la police
police = pygame.font.SysFont("monospace" ,45)

image_texte = police.render ( "Appuyer sur 1,2 ou 3", 1 , (255,0,255) )

texte_j = police.render ("Joueur   à ton tour", 1 , (255,0,255))

j1 = police.render ("1", 1 , (255,0,255))

j2 = police.render ("2", 1 , (255,0,255))

jia = police.render ("ia", 1 , (255,0,255))

win_j1 = police.render ("Bravo joueur 1 ! Tu as gagné !", 1 , (255,0,255))

win_j2 = police.render ("Bravo joueur 2 ! Tu as gagné !", 1 , (255,0,255))

win_ia = police.render ("Bravo l'ia ! Tu as gagné !", 1 , (255,0,255))

relancer = police.render ("Cliquer sur 1 pour relancer", 1 , (255,0,255))

mode = police.render ("Appuyer a pour j vs j ou b pour j vs ia", 1 , (255,0,255))

qui_commence = police.render ("Appuyer j pour commencer sinon i", 1 , [255,0,255])

while running :
    #appliquer l'arrière plan de notre jeu
    screen.blit(carre2,(0,0))

    #appliquer l'allumette
    o = -50
    for i in range(21):
        screen.blit(allumette1.image,(o,150))
        o+=50

    screen.blit(mode, (10,25))

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        #que l'événement est fermeture de fenêtre
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                joueurs()
            if event.key == pygame.K_b:
                ia()


    def checkageVictoire(J,N):
        if(N>0):
            print("Tour ",J,": il reste :",N)
        else:
            if J == "J2":
                screen.blit(win_j2, (100,240))
                screen.blit(relancer, (150,350))
                pygame.display.flip()
            elif J == "ia":
                screen.blit(win_ia, (100,240))
                screen.blit(relancer, (150,350))
                pygame.display.flip()
            else :
                screen.blit(win_j1,(100,240))
                screen.blit(relancer,(150,350))
                pygame.display.flip()

    def joueurs():
        #appliquer image_texte
        screen.blit(image_texte, (300,150))

        #appliquer texte_j
        screen.blit(texte_j,(350,200))

        N = 21 #c'est le nombre d'allumettes
        a = 0 #cette variable me sert juste à alterner entre le joueur 1 et 2
        b = 1065 #coordonnée en x de départ de carre1
        while N >= 0 :
            if a % 2 == 0 :
                # afficher carre
                screen.blit(carre, (540,200))
                #afficher 1
                screen.blit(j1, (540,200))
                #mettre à jour l'affichage
                pygame.display.flip()
                for event in pygame.event.get():
                #détecter touche enfoncée
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            b -= 50
                            screen.blit(carre1,(b,240))
                            pygame.display.flip()
                            N -= 1
                            checkageVictoire("J2",N)
                            a += 1
                        elif event.key == pygame.K_2:
                            if N-2 >= 0 :
                                b -= 100
                                screen.blit(carre1,(b,240))
                                pygame.display.flip()
                                N -= 2
                                checkageVictoire("J2",N)
                                a += 1
                            else :
                                print("Il n'y a plus assez d'allumettes")
                        elif event.key == pygame.K_3:
                            if N-3 >= 0 :
                                b -= 150
                                screen.blit(carre1,(b,240))
                                pygame.display.flip()
                                N -= 3
                                checkageVictoire("J2",N)
                                a += 1
                            else :
                                print("Il n'y a plus assez d'allumettes")
                    if event.type == pygame.QUIT :
                        running = False
                        pygame.quit()
                        print("Fermeture du jeu")
                        sys.exit()

            else :
                # afficher carre
                screen.blit(carre, (540,200))
                #afficher 2
                screen.blit(j2, (540,200))
                #mettre à jour l'affichage
                pygame.display.flip()
                for event in pygame.event.get():
                #détecter touche enfoncée
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            b -= 50
                            screen.blit(carre1,(b,240))
                            pygame.display.flip()
                            N -= 1
                            checkageVictoire("J1",N)
                            a += 1
                        elif event.key == pygame.K_2:
                            if N-2 >= 0 :
                                b -= 100
                                screen.blit(carre1,(b,240))
                                pygame.display.flip()
                                N -= 2
                                checkageVictoire("J1",N)
                                a += 1
                            else :
                                print("Il n'y a plus assez d'allumettes")
                        elif event.key == pygame.K_3:
                            if N-3 >= 0 :
                                b -= 150
                                screen.blit(carre1,(b,240))
                                pygame.display.flip()
                                N -= 3
                                checkageVictoire("J1",N)
                                a += 1
                            else :
                                print("Il n'y a plus assez d'allumettes")
                    if event.type == pygame.QUIT :
                        running = False
                        pygame.quit()
                        print("Fermeture du jeu")
                        sys.exit()

    def ia():
        #demender si le joueur veut commencer
        screen.blit(qui_commence,(25,60))
        pygame.display.flip()

        #appliquer image_texte
        screen.blit(image_texte, (300,150))

        #appliquer texte_j
        screen.blit(texte_j,(350,200))

        # choisir si le joueur commence ou pas
        c = 0
        while c == 0 :
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j:
                        a=0
                        c+=2
                    if event.key == pygame.K_i:
                        a=1
                        c+=1

        N = 21 #c'est le nombre d'allumettes
        b = 1065 #cordonée en x de départ de carre1
        valeur = 0 #permet de savoir ce que le joueur à jouer
        while N >= 0 :
            if a % 2 == 0 :
                # afficher carre
                screen.blit(carre, (540,200))
                #afficher 1
                screen.blit(j1, (540,200))
                #mettre à jour l'affichage
                pygame.display.flip()
                for event in pygame.event.get():
                #détecter touche enfoncée
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            b -= 50
                            screen.blit(carre1,(b,240))
                            pygame.display.flip()
                            N -= 1
                            checkageVictoire("ia",N)
                            a += 1
                            valeur = 1
                        elif event.key == pygame.K_2:
                            if N-2 >= 0 :
                                b -= 100
                                screen.blit(carre1,(b,240))
                                pygame.display.flip()
                                N -= 2
                                checkageVictoire("ia",N)
                                a += 1
                                valeur = 2
                            else :
                                print("Il n'y a plus assez d'allumettes")
                        elif event.key == pygame.K_3:
                            if N-3 >= 0 :
                                b -= 150
                                screen.blit(carre1,(b,240))
                                pygame.display.flip()
                                N -= 3
                                checkageVictoire("ia",N)
                                a += 1
                                valeur = 3
                            else :
                                print("Il n'y a plus assez d'allumettes")
                    if event.type == pygame.QUIT :
                        running = False
                        pygame.quit()
                        print("Fermeture du jeu")
                        sys.exit()

            else :
                if c == 1:
                    if valeur == 0 :
                        b -= 50
                        screen.blit(carre1,(b,240))
                        pygame.display.flip()
                        N -= 1
                        checkageVictoire("J1",N)
                        a += 1
                    elif valeur == 1 :
                        b -= 100
                        screen.blit(carre1,(b,240))
                        pygame.display.flip()
                        N -= 2
                        checkageVictoire("J1",N)
                        a += 1
                        c = 2
                    elif valeur == 2 :
                        b -= 50
                        screen.blit(carre1,(b,240))
                        pygame.display.flip()
                        N -= 1
                        checkageVictoire("J1",N)
                        a += 1
                        c = 2
                    elif valeur == 3 :
                        b -= 50
                        screen.blit(carre1,(b,240))
                        pygame.display.flip()
                        N -= 1
                        checkageVictoire("J1",N)
                        a += 1
                elif c == 2 :
                    if valeur == 1 :
                        if N-3 >= 0 :
                            b -= 150
                            screen.blit(carre1,(b,240))
                            pygame.display.flip()
                            N -= 3
                            checkageVictoire("J1",N)
                            a += 1
                        else :
                            a += 1
                    elif valeur == 2 :
                        if N-2 >= 0 :
                            b -= 100
                            screen.blit(carre1,(b,240))
                            pygame.display.flip()
                            N -= 2
                            checkageVictoire("J1",N)
                            a += 1
                        else :
                            a += 1
                    elif valeur == 3 :
                        if N-1 >= 0 :
                            b -= 50
                            screen.blit(carre1,(b,240))
                            pygame.display.flip()
                            N -= 1
                            checkageVictoire("J1",N)
                            a += 1
                        else :
                            a += 1