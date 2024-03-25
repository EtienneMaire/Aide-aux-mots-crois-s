import pygame

WIDTH = 970
HEIGHT = 768
BACKGROUND = (200, 200, 200)

dico = []
White = (255, 255, 255)
Gray = (128, 128, 128)

surface = 0
word = ""

pygame.font.init()
font = pygame.font.SysFont('Calibri', 50)

textSurface = 0

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

def drawCase(x, y):
    pygame.draw.rect(surface, White, pygame.Rect(x, y, 60, 60))
    pygame.draw.rect(surface, Gray, pygame.Rect(x, y, 60, 60), 3)

def renderWord(screen):
    global textSurface

    for i in range(len(word)):
        textSurface = font.render(word[i], False, (0, 0, 0))
        screen.blit(textSurface, (47 + 65 * i, 33))

def main():
    global dico
    global surface
    global word

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(word)
                elif event.key == pygame.K_BACKSPACE:
                    word = word[:-1]
                else:
                    if len(word) < 14:
                        word += event.unicode

        screen.fill(BACKGROUND)

        for i in range(14):
            drawCase(30 + 65 * i, 30)

        renderWord(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()