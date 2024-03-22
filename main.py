import pygame

WIDTH = 1024
HEIGHT = 768
BACKGROUND = (200, 200, 200)

dico = []
White = (255, 255, 255)
Gray = (128, 128, 128)

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

def main():
    global dico

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

        screen.fill(BACKGROUND)

        pygame.draw.rect(surface, White, pygame.Rect(30, 30, 60, 60))
        pygame.draw.rect(surface, Gray, pygame.Rect(30, 30, 60, 60), 3)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()