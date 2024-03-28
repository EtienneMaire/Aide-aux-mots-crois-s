import pygame
from random import randint

lettres = "abcdefghijklmnopqrstuvwxyz*"

WIDTH = 970
HEIGHT = 768
SCROLL_SPEED = 30

dico = []
White = (255, 255, 255)
Blue = (46, 134, 193)
Black = (32,32,32)
Gray = (128, 128, 128)
LightGray = (220, 220, 220)

themes = []

Cursor_color=(66, 125, 130)
BGcolor=(0x81, 0xb7, 0xd2)
Outline_color=(0xda, 0xf2, 0xdc)
Box_color=(0xff, 0xcc, 0xe7)
BACKGROUND = (0x4d, 0x51, 0x98)
themes.append([Cursor_color, BGcolor, Outline_color, Box_color, BACKGROUND])

theme = randint(0, len(themes) - 1)

Cursor_color=(0, 0, 0)
BGcolor=(0, 0, 0)
Outline_color=(0, 0, 0)
Box_color=(0, 0, 0)
BACKGROUND = (0, 0, 0)

surface = 0
word = ""

pygame.font.init()
font = pygame.font.SysFont('Calibri', 50)

textSurface = 0
resultsTextSurface = 0

results = []
resultsText = ""

scroll = 0

def compareWords(word0, word1):
    if not (len(word0) == len(word1)):
        return False

    for i in range(len(word0)):
        if not (word0[i] == word1[i] or word0[i] == '*' or word1[i] == '*'):
            return False

    return True

def findWord(word):
    r = []

    for item in dico:
        if compareWords(item, word):
            r.append(item)

    return r

def drawBox(x, y):
    pygame.draw.rect(surface, themes[theme][3], pygame.Rect(x, y - scroll, 60, 60))
    pygame.draw.rect(surface, themes[theme][2], pygame.Rect(x, y - scroll, 60, 60), 3)

def drawResultsBG():
    pygame.draw.rect(surface, themes[theme][1], pygame.Rect(40, 100 - scroll, 880, max(650, 50 * len(resultsText.split('\n')))))

def drawCursor(x, y):
    if pygame.time.get_ticks() % 1000 >= 500:
        pygame.draw.rect(surface, themes[theme][0], pygame.Rect(x, y - scroll, 25, 2))

def renderWord(screen):
    global textSurface

    for i in range(len(word)):
        textSurface = font.render(word[i], False, (0, 0, 0))
        screen.blit(textSurface, (47 + 65 * i, 33 - scroll))

def renderResults(screen):
    global resultsTextSurface

    resultsText2 = resultsText.split('\n')
    for i in range(len(resultsText2)):
        resultsTextSurface = font.render(resultsText2[i], False, (0, 0, 0))
        screen.blit(resultsTextSurface, (65, 120 + 50 * i - scroll))

def main():
    global dico
    global surface
    global word
    global resultsText
    global scroll

    f = open("dico.txt", "r")
    dico = f.read().split('\n');
    f.close()

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Aide aux mots croisés")
    clock = pygame.time.Clock()

    gameRunning = True

    surface = screen

    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False

            if event.type == pygame.MOUSEWHEEL:
                scroll -= event.y * SCROLL_SPEED
                maxScroll = max(650, 120 + 50 * (len(resultsText.split('\n')) - 1)) - 650
                scroll = max(min(scroll, maxScroll), 0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    results = findWord(word.lower())
                    if len(results) > 1:
                        resultsText =  f"Les mots correspondants sont \n({len(results)} mots trouvés):\n"

                        for i in range(len(results)):
                            resultsText += (results[i] + "\n")

                    elif len(results) == 1:
                        resultsText =  f"Le mot correspondant est: \n"

                        resultsText += results[0]

                    else:
                        resultsText =  "Aucun mot ne correspond"

                elif event.key == pygame.K_BACKSPACE:
                    word = word[:-1]
                else:
                    if len(word) < 14 and event.unicode.lower() in lettres:
                        word += event.unicode

        screen.fill(themes[theme][4])

        for i in range(14):
            drawBox(30 + 65 * i, 30)

        renderWord(screen)
        if len(word) < 14:
            drawCursor(47 + 65 * len(word), 80)

        drawResultsBG()

        renderResults(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()