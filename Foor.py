import pygame
import sys

# Pygame'i initsialiseerimine
pygame.init()

# Ekraani seaded
screen = pygame.display.set_mode([300, 300])
pygame.display.set_caption("Erki Kütt")
screen.fill([0, 0, 0])  # Must taustavärv

# Ümbritsev halli värviga täitmata ristkülik
pygame.draw.rect(screen, [130, 130, 130], [100, 10, 100, 275], 2)

# Foori tuled
pygame.draw.circle(screen, [255, 0, 0], [150, 65], 40)  # Punane tuli
pygame.draw.circle(screen, [255, 255, 0], [150, 150], 40)  # Kollane tuli
pygame.draw.circle(screen, [0, 255, 0], [150, 235], 40)  # Roheline tuli

# Ekraanivärskendus
pygame.display.flip()

# Sündmuste käitlemine
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Pygame'i sulgemine
pygame.quit()
sys.exit()
