import pygame

WIDTH = 768
HEIGHT = 512
BACKGROUND = (0, 0, 0)

dico = []

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

    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False

        screen.fill(BACKGROUND)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()