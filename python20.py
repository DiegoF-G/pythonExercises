import pygame

pygame.mixer.init()
pygame.mixer.music.load() #insira no argumento o nome do arquivo mp3 com a extensão para ser tocado
pygame.mixer.music.play()
pygame.event.wait()

