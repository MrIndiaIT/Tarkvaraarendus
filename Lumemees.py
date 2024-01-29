import pygame
import sys

# Pygame'i initsialiseerimine
pygame.init()

# Ekraani seaded
screen = pygame.display.set_mode([300, 300])
pygame.display.set_caption("Erki Kütt")
screen.fill([0, 0, 0])  # Must taustavärv

# Lumememme kehaosad
pygame.draw.circle(screen, [255, 255, 255], [150, 80], 30)  # Pea
pygame.draw.circle(screen, [255, 255, 255], [150, 145], 40)  # Keha
pygame.draw.circle(screen, [255, 255, 255], [150, 230], 50)  # Jalgade alaosa

# Silmad
pygame.draw.circle(screen, [0, 0, 0], [140, 75], 5)  # Vasak silm
pygame.draw.circle(screen, [0, 0, 0], [160, 75], 5)  # Parem silm

# Nina (alla suunatud teravkolmnurk)
pygame.draw.polygon(screen, [255, 69, 0], [[145, 85], [150, 100], [155, 85]])  # Porgand

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
