import pygame
from pygame.locals import *
import sys
import random

pygame.init()

pygame.display.set_caption("Joyeux Nowel !")
screen = pygame.display.set_mode((1600, 900), RESIZABLE)

Icon = pygame.image.load("Icon.png")
pygame.display.set_icon(Icon)
BLACK = (0, 0, 0)

Hard = False

clockF = pygame.time.Clock()


def JoyeuxNoel():
    joyeuxNoel = pygame.image.load("JoyeuxNoel.png").convert()
    screen.blit(joyeuxNoel, (0, 0))
    pygame.display.flip()
    pygame.mixer.music.load("BBSChristmasOST.wav")
    pygame.mixer.music.play(loops=-1)

    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 700:
                Menu()
                return
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def Test():
    Menu()


def Menu():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("OSTBleachHollowed.wav")
    pygame.mixer.music.play(loops=-1)
    menu = pygame.image.load("Menu.png").convert()
    screen.blit(menu, (0, 0))
    pygame.display.flip()

    launch = True
    while launch:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 48 < event.pos[0] < 374 \
                    and 205 < event.pos[1] < 385:
                launch = False
                HardNormal = pygame.image.load("Game1/HardNormal.png")
                screen.blit(HardNormal, (0, 0))
                pygame.display.flip()
                HardOrNormalGame1()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 1106 < event.pos[0] < 1432 \
                    and 213 < event.pos[1] < 393:
                pygame.mixer.music.stop()
                InstructionsGame2 = pygame.image.load("Game2/InstructionsGame2.png")
                screen.blit(InstructionsGame2, (0, 0))
                pygame.display.flip()
                while launch:
                    for event2 in pygame.event.get():
                        if event2.type == KEYDOWN and event2.key == K_SPACE:
                            launch = False
                            Test()
                        if event2.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event2.type == MOUSEBUTTONDOWN and event2.button == 1:
                            launch = False
                            Game2()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 606 < event.pos[0] < 922 \
                    and 389 < event.pos[1] < 653:
                launch = False
                pygame.mixer.music.stop()
                FinalGameCode()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 85 < event.pos[0] < 433 \
                    and 539 < event.pos[1] < 677:
                launch = False
                pygame.mixer.music.stop()
                SummonSimulator()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 1121 < event.pos[0] < 1486 \
                    and 556 < event.pos[1] < 695:
                launch = False
                pygame.mixer.music.stop()
                SummonSimulator()


def HardOrNormalGame1():
    global Hard

    launch = True
    while launch:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                launch = False
                Menu()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 0 < event.pos[0] < 800 \
                    and 0 < event.pos[1] < 900:
                Hard = False
                InstructionsNormal = pygame.image.load("Game1/InstructionsNormal.png")
                screen.blit(InstructionsNormal, (0, 0))
                pygame.display.flip()
                pygame.mixer.music.stop()
                pygame.mixer.music.load("Game1/OSTBleachTreachery.wav")
                pygame.mixer.music.play(loops=-1)
                while launch:
                    for event2 in pygame.event.get():
                        if event2.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event2.type == KEYDOWN and event2.key == K_SPACE:
                            launch = False
                            Menu()
                        if event2.type == MOUSEBUTTONDOWN and event2.button == 1:
                            launch = False
                            Game1()

            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 801 < event.pos[0] < 1600 \
                    and 0 < event.pos[1] < 900:
                Hard = True
                InstructionsHard = pygame.image.load("Game1/InstructionsHard.png")
                screen.blit(InstructionsHard, (0, 0))
                pygame.display.flip()
                pygame.mixer.music.stop()
                pygame.mixer.music.load("Game1/OSTBleachTreachery.wav")
                pygame.mixer.music.play(loops=-1)
                while launch:
                    for event2 in pygame.event.get():
                        if event2.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event2.type == KEYDOWN and event2.key == K_SPACE:
                            launch = False
                            Menu()
                        if event2.type == MOUSEBUTTONDOWN and event2.button == 1:
                            launch = False
                            Game1()


def Game1():
    clock = pygame.time.Clock()
    if not Hard:
        Gauche = K_LEFT
        Droite = K_RIGHT
        Bas = K_DOWN
        Haut = K_UP
        nb = 0
    else:
        Gauche = K_RIGHT
        Droite = K_LEFT
        Bas = K_UP
        Haut = K_DOWN
        nb = 4

    Fond_Game1 = pygame.image.load("Game1/FondGame1.png")
    Loose = pygame.image.load("Game1/Loose.png")
    Gin = pygame.image.load("Game1/Gin.png")
    Gin_x = 82
    Gin_y = 93
    Rect_Gin = pygame.Rect(Gin_x, Gin_y, 96, 106)

    Hogyoku_x = 390
    Hogyoku1 = pygame.image.load("Game1/Hogyoku.png")
    Rect_Hogyoku1 = pygame.Rect(Hogyoku_x, 750, 75, 81)
    Hogyoku_x2 = 700
    Hogyoku2 = pygame.image.load("Game1/Hogyoku.png")
    Rect_Hogyoku2 = pygame.Rect(Hogyoku_x2, 590, 75, 81)
    Hogyoku_x3 = 1133
    Hogyoku3 = pygame.image.load("Game1/Hogyoku.png")
    Rect_Hogyoku3 = pygame.Rect(Hogyoku_x3, 280, 75, 81)
    Hogyoku_x4 = 513
    Hogyoku4 = pygame.image.load("Game1/Hogyoku.png")
    Rect_Hogyoku4 = pygame.Rect(Hogyoku_x4, 124, 75, 81)
    Hogyoku_x5 = 900
    Hogyoku5 = pygame.image.load("Game1/Hogyoku.png")
    Rect_Hogyoku5 = pygame.Rect(Hogyoku_x5, 410, 75, 81)
    Hogyoku_y6 = 80
    Hogyoku6 = pygame.image.load("Game1/Hogyoku.png")
    Rect_Hogyoku6 = pygame.Rect(733, Hogyoku_y6, 75, 81)
    Hogyoku_y7 = 450
    Hogyoku7 = pygame.image.load("Game1/Hogyoku.png")
    Rect_Hogyoku7 = pygame.Rect(1050, Hogyoku_y7, 75, 81)

    Mur_Droite = pygame.Rect(1300, 0, 52, 900)
    Mur_Gauche = pygame.Rect(235, 0, 52, 900)
    Mur_Gauche1_Gin = pygame.Rect(0, 58, 48, 842)
    Mur_Gauche2_Gin = pygame.Rect(209, 58, 50, 589)
    Mur_Droite1_Gin = pygame.Rect(1328, 216, 49, 684)
    Mur_Droite2_Gin = pygame.Rect(1551, 0, 49, 900)
    Mur_Haut1_Gin = pygame.Rect(0, 0, 258, 57)
    Mur_Haut2_Gin = pygame.Rect(0, 0, 1600, 47)
    Mur_Bas1_Gin = pygame.Rect(0, 874, 1600, 26)
    Mur_Bas2_Gin = pygame.Rect(1327, 855, 273, 45)
    Mur_DroiteHorizontal_Gin = pygame.Rect(1261, 215, 116, 49)

    Rect_Orbe = pygame.Rect(1421, 728, 93, 82)

    test1 = 0
    test2 = 0
    test3 = 0
    test4 = 0
    test5 = 0
    test6 = 0
    test7 = 0

    Mort = False
    while not Mort:
        clock.tick(30)
        screen.blit(Fond_Game1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                Menu()
            if event.type == KEYDOWN and event.key == Droite:
                Gin_x += 50
                Rect_Gin.x += 50
            if event.type == KEYDOWN and event.key == Gauche:
                Gin_x -= 50
                Rect_Gin.x -= 50
            if event.type == KEYDOWN and event.key == Bas:
                Gin_y += 50
                Rect_Gin.y += 50
            if event.type == KEYDOWN and event.key == Haut:
                Gin_y -= 50
                Rect_Gin.y -= 50

        if not Rect_Hogyoku1.colliderect(Mur_Droite) and test1 == 0:
            Hogyoku_x += 35 + nb
            Rect_Hogyoku1.x += 35 + nb
        elif not Rect_Hogyoku1.colliderect(Mur_Gauche):
            test1 = 1
            Hogyoku_x -= 35 + nb
            Rect_Hogyoku1.x -= 35 + nb
        else:
            test1 = 0

        if not Rect_Hogyoku2.colliderect(Mur_Droite) and test2 == 0:
            Hogyoku_x2 += 75 + nb
            Rect_Hogyoku2.x += 75 + nb
        elif not Rect_Hogyoku2.colliderect(Mur_Gauche):
            test2 = 1
            Hogyoku_x2 -= 75 + nb
            Rect_Hogyoku2.x -= 75 + nb
        else:
            test2 = 0

        if not Rect_Hogyoku3.colliderect(Mur_Droite) and test3 == 0:
            Hogyoku_x3 += 45 + nb
            Rect_Hogyoku3.x += 45 + nb
        elif not Rect_Hogyoku3.colliderect(Mur_Gauche):
            test3 = 1
            Hogyoku_x3 -= 45 + nb
            Rect_Hogyoku3.x -= 45 + nb
        else:
            test3 = 0

        if not Rect_Hogyoku4.colliderect(Mur_Droite) and test4 == 0:
            Hogyoku_x4 += 80 + nb
            Rect_Hogyoku4.x += 80 + nb
        elif not Rect_Hogyoku4.colliderect(Mur_Gauche):
            test4 = 1
            Hogyoku_x4 -= 80 + nb
            Rect_Hogyoku4.x -= 80 + nb
        else:
            test4 = 0

        if not Rect_Hogyoku5.colliderect(Mur_Droite) and test5 == 0:
            Hogyoku_x5 += 15 + nb
            Rect_Hogyoku5.x += 15 + nb
        elif not Rect_Hogyoku5.colliderect(Mur_Gauche):
            test5 = 1
            Hogyoku_x5 -= 15 + nb
            Rect_Hogyoku5.x -= 15 + nb
        else:
            test5 = 0

        if not Rect_Hogyoku6.colliderect(Mur_Bas1_Gin) and test6 == 0:
            Hogyoku_y6 += 25 + nb
            Rect_Hogyoku6.y += 25 + nb
        elif not Rect_Hogyoku6.colliderect(Mur_Haut2_Gin):
            test6 = 1
            Hogyoku_y6 -= 25 + nb
            Rect_Hogyoku6.y -= 25 + nb
        else:
            test6 = 0

        if not Rect_Hogyoku7.colliderect(Mur_Bas1_Gin) and test7 == 0:
            Hogyoku_y7 += 12 + nb
            Rect_Hogyoku7.y += 12 + nb
        elif not Rect_Hogyoku7.colliderect(Mur_Haut2_Gin):
            test7 = 1
            Hogyoku_y7 -= 12 + nb
            Rect_Hogyoku7.y -= 12 + nb
        else:
            test7 = 0

        screen.blit(Gin, (Gin_x, Gin_y))
        screen.blit(Hogyoku1, (Hogyoku_x, 750))
        screen.blit(Hogyoku2, (Hogyoku_x2, 590))
        screen.blit(Hogyoku3, (Hogyoku_x3, 280))
        screen.blit(Hogyoku4, (Hogyoku_x4, 124))
        screen.blit(Hogyoku5, (Hogyoku_x5, 410))
        screen.blit(Hogyoku6, (733, Hogyoku_y6))
        screen.blit(Hogyoku7, (1050, Hogyoku_y7))

        pygame.display.flip()
        # Gin Death
        if Rect_Gin.colliderect(Rect_Hogyoku7) \
                or Rect_Gin.colliderect(Rect_Hogyoku1) \
                or Rect_Gin.colliderect(Rect_Hogyoku2) \
                or Rect_Gin.colliderect(Rect_Hogyoku3) \
                or Rect_Gin.colliderect(Rect_Hogyoku4) \
                or Rect_Gin.colliderect(Rect_Hogyoku5) \
                or Rect_Gin.colliderect(Rect_Hogyoku6) \
                or Rect_Gin.colliderect(Mur_Gauche1_Gin) \
                or Rect_Gin.colliderect(Mur_Gauche2_Gin) \
                or Rect_Gin.colliderect(Mur_Droite1_Gin) \
                or Rect_Gin.colliderect(Mur_Droite2_Gin) \
                or Rect_Gin.colliderect(Mur_Haut1_Gin) \
                or Rect_Gin.colliderect(Mur_Haut2_Gin) \
                or Rect_Gin.colliderect(Mur_Bas1_Gin) \
                or Rect_Gin.colliderect(Mur_Bas2_Gin) \
                or Rect_Gin.colliderect(Mur_DroiteHorizontal_Gin):
            screen.fill(BLACK)
            screen.blit(Loose, (0, 0))
            Mort = True
            pygame.display.flip()
            RestartGame1()
        # Win
        if Rect_Gin.colliderect(Rect_Orbe):
            Mort = True
            screen.fill(BLACK)
            if not Hard:
                Win = pygame.image.load("Game1/Win.png")
            else:
                Win = pygame.image.load("Game1/WinHard.png")
            screen.blit(Win, (0, 0))
            pygame.display.flip()
            WinGame1()


def WinGame1():
    launched = True
    while launched:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                Menu()


def RestartGame1():
    launched = True
    while launched:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 541 < event.pos[0] < 990 \
                    and 327 < event.pos[1] < 463:
                Game1()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 541 < event.pos[0] < 990 \
                    and 560 < event.pos[1] < 700:
                Menu()


def Game2():
    points = 0
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    screen.fill(BLACK)
    Song = ["Game2/Endings/Ed01.wav", "Game2/Openings/Op02.wav", "Game2/Openings/Op06.wav", "Game2/Openings/Op08.wav",
            "Game2/Openings/Op09.wav", "Game2/Openings/Op11.wav", "Game2/Openings/Op13.wav", "Game2/Openings/Op15.wav",
            "Game2/Openings/Op16.wav", "Game2/Endings/Ed03.wav", "Game2/Endings/Ed05.wav", "Game2/Endings/Ed09.wav",
            "Game2/Endings/Ed10.wav", "Game2/Endings/Ed17.wav", "Game2/Endings/Ed20.wav", "Game2/Endings/Ed22.wav",
            "Game2/Endings/Ed25.wav", "Game2/Endings/Ed26.wav", "Game2/Endings/Ed27.wav", "Game2/Endings/Ed28.wav",
            "Game2/Endings/Ed30.wav", "Game2/OST/EncirclementBattle.wav", "Game2/OST/FadeToBlack.wav",
            "Game2/OST/Invasion.wav", "Game2/OST/Senna.wav", "Game2/OST/TornAppart.wav"]
    Vrai = pygame.image.load("Game2/Vrai.png")
    Faux = pygame.image.load("Game2/Faux.png")
    ChoiceOpening = pygame.image.load("Game2/ChoiceOpening.png")
    Choice = pygame.image.load("Game2/Choice.png")
    ChoiceOST = pygame.image.load("Game2/ChoiceOST.png")
    ChoiceEnding = pygame.image.load("Game2/ChoiceEnding.png")

    for n in range(0, 26):
        pygame.mixer.music.stop()
        ChoosedSong = random.choice(Song)
        Song.remove(ChoosedSong)
        pygame.mixer.music.load(ChoosedSong)
        pygame.mixer.music.play(loops=-1)
        screen.blit(Choice, (0, 0))
        pygame.display.flip()
        launch = True

        if ChoosedSong == "Game2/Openings/Op02.wav":
            x1 = 320
            x2 = 640
            y1 = 0
            y2 = 224

        if ChoosedSong == "Game2/Openings/Op06.wav":
            x1 = 0
            x2 = 320
            y1 = 220
            y2 = 451

        if ChoosedSong == "Game2/Openings/Op08.wav":
            x1 = 640
            x2 = 961
            y1 = 224
            y2 = 448

        if ChoosedSong == "Game2/Openings/Op09.wav":
            x1 = 963
            x2 = 1279
            y1 = 226
            y2 = 451

        if ChoosedSong == "Game2/Openings/Op11.wav":
            x1 = 0
            x2 = 321
            y1 = 450
            y2 = 677

        if ChoosedSong == "Game2/Openings/Op13.wav":
            x1 = 639
            x2 = 961
            y1 = 450
            y2 = 674

        if ChoosedSong == "Game2/Openings/Op15.wav":
            x1 = 1282
            x2 = 1600
            y1 = 452
            y2 = 673

        if ChoosedSong == "Game2/Openings/Op16.wav":
            x1 = 0
            x2 = 320
            y1 = 677
            y2 = 900

        if ChoosedSong == "Game2/Openings/Op02.wav" \
                or ChoosedSong == "Game2/Openings/Op06.wav" \
                or ChoosedSong == "Game2/Openings/Op08.wav" \
                or ChoosedSong == "Game2/Openings/Op09.wav" \
                or ChoosedSong == "Game2/Openings/Op11.wav" \
                or ChoosedSong == "Game2/Openings/Op13.wav" \
                or ChoosedSong == "Game2/Openings/Op15.wav" \
                or ChoosedSong == "Game2/Openings/Op16.wav":
            while launch:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN and event.key == K_SPACE:
                        Menu()
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and 0 < event.pos[0] < 533:
                        screen.blit(ChoiceOpening, (0, 0))
                        pygame.display.flip()
                        while launch:
                            for event2 in pygame.event.get():
                                if event2.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event2.type == KEYDOWN and event2.key == K_SPACE:
                                    Menu()
                                if event2.type == MOUSEBUTTONDOWN and event2.button == 1 \
                                        and x1 < event2.pos[0] < x2 and y1 < event2.pos[1] < y2:
                                    screen.blit(Vrai, (0, 0))
                                    pygame.display.flip()
                                    points += 1
                                    pygame.time.wait(1500)
                                    launch = False
                                elif event2.type == MOUSEBUTTONDOWN and event2.button == 1:
                                    screen.blit(Faux, (0, 0))
                                    pygame.display.flip()
                                    pygame.time.wait(1500)
                                    launch = False
                    elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                        screen.blit(Faux, (0, 0))
                        pygame.display.flip()
                        pygame.time.wait(1500)
                        launch = False

        if ChoosedSong == "Game2/Endings/Ed01.wav":
            x1 = 0
            x2 = 266
            y1 = 0
            y2 = 180

        if ChoosedSong == "Game2/Endings/Ed03.wav":
            x1 = 535
            x2 = 800
            y1 = 0
            y2 = 180

        if ChoosedSong == "Game2/Endings/Ed05.wav":
            x1 = 1070
            x2 = 1336
            y1 = 0
            y2 = 180

        if ChoosedSong == "Game2/Endings/Ed09.wav":
            x1 = 533
            x2 = 800
            y1 = 181
            y2 = 364

        if ChoosedSong == "Game2/Endings/Ed10.wav":
            x1 = 800
            x2 = 1064
            y1 = 181
            y2 = 364

        if ChoosedSong == "Game2/Endings/Ed17.wav":
            x1 = 1068
            x2 = 1337
            y1 = 366
            y2 = 543

        if ChoosedSong == "Game2/Endings/Ed20.wav":
            x1 = 268
            x2 = 535
            y1 = 543
            y2 = 723

        if ChoosedSong == "Game2/Endings/Ed22.wav":
            x1 = 802
            x2 = 1067
            y1 = 542
            y2 = 721

        if ChoosedSong == "Game2/Endings/Ed25.wav":
            x1 = 0
            x2 = 266
            y1 = 725
            y2 = 900

        if ChoosedSong == "Game2/Endings/Ed26.wav":
            x1 = 267
            x2 = 536
            y1 = 725
            y2 = 900

        if ChoosedSong == "Game2/Endings/Ed27.wav":
            x1 = 537
            x2 = 800
            y1 = 725
            y2 = 900

        if ChoosedSong == "Game2/Endings/Ed28.wav":
            x1 = 800
            x2 = 1066
            y1 = 725
            y2 = 900

        if ChoosedSong == "Game2/Endings/Ed30.wav":
            x1 = 1336
            x2 = 1600
            y1 = 725
            y2 = 900

        if ChoosedSong == "Game2/Endings/Ed01.wav" \
                or ChoosedSong == "Game2/Endings/Ed03.wav" \
                or ChoosedSong == "Game2/Endings/Ed05.wav" \
                or ChoosedSong == "Game2/Endings/Ed09.wav" \
                or ChoosedSong == "Game2/Endings/Ed10.wav" \
                or ChoosedSong == "Game2/Endings/Ed17.wav" \
                or ChoosedSong == "Game2/Endings/Ed20.wav" \
                or ChoosedSong == "Game2/Endings/Ed22.wav" \
                or ChoosedSong == "Game2/Endings/Ed25.wav" \
                or ChoosedSong == "Game2/Endings/Ed26.wav" \
                or ChoosedSong == "Game2/Endings/Ed27.wav" \
                or ChoosedSong == "Game2/Endings/Ed28.wav" \
                or ChoosedSong == "Game2/Endings/Ed30.wav":
            while launch:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN and event.key == K_SPACE:
                        Menu()
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and 534 < event.pos[0] < 1066:
                        screen.blit(ChoiceEnding, (0, 0))
                        pygame.display.flip()
                        while launch:
                            for event2 in pygame.event.get():
                                if event2.type == KEYDOWN and event2.key == K_SPACE:
                                    Menu()
                                if event2.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event2.type == MOUSEBUTTONDOWN and event2.button == 1 \
                                        and x1 < event2.pos[0] < x2 and y1 < event2.pos[1] < y2:
                                    screen.blit(Vrai, (0, 0))
                                    pygame.display.flip()
                                    points += 1
                                    pygame.time.wait(1500)
                                    launch = False
                                elif event2.type == MOUSEBUTTONDOWN and event2.button == 1:
                                    screen.blit(Faux, (0, 0))
                                    pygame.display.flip()
                                    pygame.time.wait(1500)
                                    launch = False
                    elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                        screen.blit(Faux, (0, 0))
                        pygame.display.flip()
                        pygame.time.wait(1500)
                        launch = False

        if ChoosedSong == "Game2/OST/EncirclementBattle.wav":
            y1 = 0
            y2 = 180

        if ChoosedSong == "Game2/OST/FadeToBlack.wav":
            y1 = 181
            y2 = 360

        if ChoosedSong == "Game2/OST/Invasion.wav":
            y1 = 361
            y2 = 540

        if ChoosedSong == "Game2/OST/Senna.wav":
            y1 = 541
            y2 = 720

        if ChoosedSong == "Game2/OST/TornAppart.wav":
            y1 = 721
            y2 = 900

        if ChoosedSong == "Game2/OST/EncirclementBattle.wav" \
                or ChoosedSong == "Game2/OST/FadeToBlack.wav" \
                or ChoosedSong == "Game2/OST/Invasion.wav" \
                or ChoosedSong == "Game2/OST/Senna.wav" \
                or ChoosedSong == "Game2/OST/TornAppart.wav":
            while launch:
                for event in pygame.event.get():
                    if event.type == KEYDOWN and event.key == K_SPACE:
                        Menu()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and 1067 < event.pos[0] < 1600:
                        screen.blit(ChoiceOST, (0, 0))
                        pygame.display.flip()
                        while launch:
                            for event2 in pygame.event.get():
                                if event2.type == KEYDOWN and event2.key == K_SPACE:
                                    Menu()
                                if event2.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event2.type == MOUSEBUTTONDOWN and event2.button == 1 and y1 < event2.pos[1] < y2:
                                    screen.blit(Vrai, (0, 0))
                                    pygame.display.flip()
                                    points += 1
                                    pygame.time.wait(1500)
                                    launch = False
                                elif event2.type == MOUSEBUTTONDOWN and event2.button == 1:
                                    screen.blit(Faux, (0, 0))
                                    pygame.display.flip()
                                    pygame.time.wait(1500)
                                    launch = False
                    elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                        screen.blit(Faux, (0, 0))
                        pygame.display.flip()
                        pygame.time.wait(1500)
                        launch = False

    if points < 26:
        ScoreLoose = pygame.image.load("Game2/ScoreLoose.png")
        screen.blit(ScoreLoose, (0, 0))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and 428 < event.pos[0] < 1104 and 285 < \
                        event.pos[1] < 485:
                    Game2()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and 428 < event.pos[0] < 1104 and 527 < \
                        event.pos[1] < 663:
                    Menu()

    if points == 26:
        Score = pygame.image.load("Game2/Score.png")
        screen.blit(Score, (0, 0))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and 443 < event.pos[0] < 1264 and 417 < \
                        event.pos[1] < 539:
                    Game2()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and 443 < event.pos[0] < 1104 and 641 < \
                        event.pos[1] < 765:
                    Menu()


def SummonSimulator():
    screen.fill(BLACK)
    Proba = pygame.image.load("SummonSimulator/Proba.png")
    screen.blit(Proba, (0, 0))
    pygame.display.flip()
    appuyer = True
    while appuyer:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                appuyer = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                appuyer = False
                Menu()
    pygame.mixer.music.load("SummonSimulator/WBToBBS.wav")
    pygame.mixer.music.play(loops=-1)
    SummonImage = pygame.image.load("SummonSimulator/Summon.png")
    screen.blit(SummonImage, (0, 0))
    pygame.display.flip()
    summon = True
    while summon:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 1090 < event.pos[0] < 1439 \
                    and 742 < event.pos[1] < 850:
                summon = False
                Summon()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                summon = False
                Menu()


def Summon():
    pygame.mixer.music.stop()
    screen.fill(BLACK)
    SummonFond = pygame.image.load("SummonSimulator/SummonFond.png")
    Gin3 = pygame.image.load("SummonSimulator/Gin3.png").convert()
    Gin4 = pygame.image.load("SummonSimulator/Gin4.png").convert()
    GinList = [pygame.image.load("SummonSimulator/GinCat.png").convert(),
               pygame.image.load("SummonSimulator/GinOrange.png").convert(),
               pygame.image.load("SummonSimulator/GinViolet.png").convert(),
               pygame.image.load("SummonSimulator/GinWD.png").convert()]
    LettreList = [pygame.image.load("SummonSimulator/A.png").convert(),
                  pygame.image.load("SummonSimulator/D.png").convert(),
                  pygame.image.load("SummonSimulator/E.png").convert(),
                  pygame.image.load("SummonSimulator/N.png").convert()]
    s1 = random.randrange(1, 201)
    s2 = random.randrange(1, 201)
    s3 = random.randrange(1, 201)
    s4 = random.randrange(1, 201)
    s5 = random.randrange(1, 201)
    s6 = random.randrange(1, 201)
    s7 = random.randrange(1, 201)
    s8 = random.randrange(1, 201)
    s9 = random.randrange(1, 201)
    s10 = random.randrange(1, 201)
    if s1 <= 7 or s2 <= 7 or s3 <= 7 or s4 <= 7 or s5 <= 7 or s6 <= 7 or s7 <= 7 or s8 <= 7 or s9 <= 7 or s10 <= 7:
        movie = pygame.movie.Movie("SummonSimulator/Star5.mpg")
        pygame.mixer.music.load("SummonSimulator/Star5.wav")
        movie.play()
        pygame.time.wait(1300)
        pygame.mixer.music.play()
        pygame.time.wait(6250)
        movie.stop()
        pygame.mixer.music.stop()
        STARFIVE = True
    else:
        movie = pygame.movie.Movie("SummonSimulator/Star4.mpg")
        pygame.mixer.music.load("SummonSimulator/Star4.wav")
        movie.play()
        pygame.time.wait(700)
        pygame.mixer.music.play()
        pygame.time.wait(3700)
        movie.stop()
        pygame.mixer.music.stop()
        STARFIVE = False
    screen.blit(SummonFond, (0, 0))
    if s1 == 1:
        x = random.choice(LettreList)
        screen.blit(x, (132, 84))
    elif s1 <= 7:
        x = random.choice(GinList)
        screen.blit(x, (132, 84))
    elif s1 <= 67:
        screen.blit(Gin4, (132, 84))
    else:
        screen.blit(Gin3, (132, 84))
    if s2 == 1:
        x = random.choice(LettreList)
        screen.blit(x, (416, 84))
    elif s2 <= 7:
        x = random.choice(GinList)
        screen.blit(x, (416, 84))
    elif s2 <= 67:
        screen.blit(Gin4, (416, 84))
    else:
        screen.blit(Gin3, (416, 84))
    if s3 == 1:
        x = random.choice(LettreList)
        screen.blit(x, (710, 84))
    elif s3 <= 7:
        x = random.choice(GinList)
        screen.blit(x, (710, 84))
    elif s3 <= 67:
        screen.blit(Gin4, (710, 84))
    else:
        screen.blit(Gin3, (710, 84))
    if s4 == 1:
        x = random.choice(LettreList)
        screen.blit(x, (996, 84))
    elif s4 <= 7:
        x = random.choice(GinList)
        screen.blit(x, (996, 84))
    elif s4 <= 67:
        screen.blit(Gin4, (996, 84))
    else:
        screen.blit(Gin3, (996, 84))
    if s5 == 1:
        x = random.choice(LettreList)
        screen.blit(x, (1282, 84))
    elif s5 <= 7:
        x = random.choice(GinList)
        screen.blit(x, (1282, 84))
    elif s5 <= 67:
        screen.blit(Gin4, (1282, 84))
    else:
        screen.blit(Gin3, (1282, 84))
    if s6 == 1:
        x = random.choice(LettreList)
        screen.blit(x, (132, 423))
    elif s6 <= 7:
        x = random.choice(GinList)
        screen.blit(x, (132, 423))
    elif s6 <= 67:
        screen.blit(Gin4, (132, 423))
    else:
        screen.blit(Gin3, (132, 423))
    if s7 == 1:
        x = random.choice(LettreList)
        screen.blit(x, (416, 423))
    elif s7 <= 7:
        x = random.choice(GinList)
        screen.blit(x, (416, 423))
    elif s7 <= 67:
        screen.blit(Gin4, (416, 423))
    else:
        screen.blit(Gin3, (416, 423))
    if s8 == 1:
        x = random.choice(LettreList)
        screen.blit(x, (710, 423))
    elif s8 <= 7:
        x = random.choice(GinList)
        screen.blit(x, (710, 423))
    elif s8 <= 67:
        screen.blit(Gin4, (710, 423))
    else:
        screen.blit(Gin3, (710, 423))
    if s9 == 1:
        x = random.choice(LettreList)
        screen.blit(x, (996, 423))
    elif s9 <= 7:
        x = random.choice(GinList)
        screen.blit(x, (996, 423))
    elif s9 <= 67:
        screen.blit(Gin4, (996, 423))
    else:
        screen.blit(Gin3, (996, 423))
    if s10 == 1:
        x = random.choice(LettreList)
        screen.blit(x, (1282, 423))
    elif s10 <= 7:
        x = random.choice(GinList)
        screen.blit(x, (1282, 423))
    elif s10 <= 67:
        screen.blit(Gin4, (1282, 423))
    else:
        screen.blit(Gin3, (1282, 423))
    pygame.display.flip()
    if STARFIVE:
        pygame.mixer.music.load("SummonSimulator/Yeah.wav")
        pygame.mixer.music.play(loops=-1)
    if not STARFIVE:
        pygame.mixer.music.load("SummonSimulator/Triste.wav")
        pygame.mixer.music.play(loops=-1)
    refaireop = True
    while refaireop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                refaireop = False
                Menu()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 662 < event.pos[0] < 871 \
                    and 790 < event.pos[1] < 845:
                refaireop = False
                Summon()


def FinalGameCode():
    Code = pygame.image.load("FinalGame/Code.png")
    screen.blit(Code, (0, 0))
    pygame.display.flip()
    code = input("Code : ")
    if code == "G1NDEAD":
        print("Oui")
        FinalGame()
    else:
        print("Non")
        Menu()


def FinalGame():
    global clockF
    clockF.tick(60)
    Ginx = 30
    FondFinalGame = pygame.image.load("FinalGame/FondFinalGame.png")
    Aizen1 = pygame.image.load("FinalGame/Aizen1.png")
    Aizen2 = pygame.image.load("FinalGame/Aizen2.png")
    Aizen3 = pygame.image.load("FinalGame/Aizen3.png")
    Aizen4 = pygame.image.load("FinalGame/Aizen4.png")
    Aizen5 = pygame.image.load("FinalGame/Aizen5.png")
    Power1 = pygame.image.load("FinalGame/Power1.png")
    Power2 = pygame.image.load("FinalGame/Power2.png")
    Power3 = pygame.image.load("FinalGame/Power3.png")
    Power4 = pygame.image.load("FinalGame/Power4.png")
    Power5 = pygame.image.load("FinalGame/Power5.png")
    Gin = pygame.image.load("FinalGame/Gin.png")
    Komamura = pygame.image.load("FinalGame/Komamura.png")
    Gin_Rect = pygame.Rect(Ginx, 745, 79, 106)
    Aizen_Rect = pygame.Rect(1275, 740, 910, 113)
    screen.blit(FondFinalGame, (0, 0))
    screen.blit(Gin, (Ginx, 745))
    pygame.display.flip()
    pygame.mixer.music.load("FinalGame/AizenHado90.wav")
    pygame.mixer.music.play(loops=-1)
    Animation = True
    while Animation:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                Menu()
            if event.type == KEYDOWN and event.key == K_RIGHT:
                clockF.tick(60)
                Ginx += 15
                Gin_Rect.x += 15
                clockF.tick(60)
                screen.blit(Gin, (Ginx, 745))
                pygame.display.flip()
            if event.type == KEYDOWN and event.key == K_LEFT:
                clockF.tick(60)
                Ginx -= 15
                Gin_Rect.x -= 15
                clockF.tick(60)
                screen.blit(Gin, (Ginx, 745))
                pygame.display.flip()

        if Gin_Rect.colliderect(Aizen_Rect):
            Animation = False
            OuiOuNon()

        clockF.tick(2)
        screen.blit(FondFinalGame, (0, 0))
        pygame.display.flip()
        screen.blit(Gin, (Ginx, 745))
        pygame.display.flip()
        screen.blit(Aizen1, (1275, 740))
        screen.blit(Komamura, (1435, 710))
        screen.blit(Power1, (1422, 787))
        pygame.display.flip()
        clockF.tick(2)
        screen.blit(Aizen2, (1275, 740))
        screen.blit(Power2, (1422, 663))
        pygame.display.flip()
        clockF.tick(2)
        screen.blit(Aizen3, (1275, 737))
        screen.blit(Power3, (1376, 660))
        pygame.display.flip()
        clockF.tick(2)
        screen.blit(Aizen4, (1275, 737))
        screen.blit(Power4, (1378, 655))
        pygame.display.flip()
        clockF.tick(2)
        screen.blit(Aizen5, (1277.5, 737))
        screen.blit(Power5, (1382.5, 660))
        pygame.display.flip()


def OuiOuNon():
    clockF.tick(60)
    pygame.mixer.music.stop()
    Combattre = pygame.image.load("FinalGame/Combattre.png")
    screen.blit(Combattre, (0, 0))
    pygame.display.flip()
    choisir = True
    while choisir:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 242 < event.pos[0] < 500 \
                    and 345 < event.pos[1] < 520:
                choisir = False
                GinMovie()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 1015 < event.pos[0] < 1282 \
                    and 379 < event.pos[1] < 517:
                choisir = False
                FinalGame()


def GinMovie():
    global screen
    Lag = pygame.image.load("FinalGame/Lag.png")
    screen.blit(Lag, (0, 0))
    pygame.display.flip()
    pygame.time.wait(2500)
    screen.fill(BLACK)
    clockF.tick(120)
    screen = pygame.display.set_mode((1600, 900), RESIZABLE)
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    movie = pygame.movie.Movie("FinalGame/GinDeath.mpg")
    movie.play()
    while True:
        if movie.get_time() >= 456:
            movie.stop()
            screen = pygame.display.set_mode((1600, 900), RESIZABLE)
            GG = pygame.image.load("FinalGame/GG.png")
            screen.blit(GG, (0, 0))
            pygame.display.flip()
            pygame.time.wait(10000)
            pygame.quit()
            sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                movie.stop()
                pygame.quit()
                sys.exit()


JoyeuxNoel()
