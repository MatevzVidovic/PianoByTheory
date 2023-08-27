import pygame
import piano_lists as pl
from pygame import mixer

from datetime import datetime
now = datetime.now()

import ast

pygame.init()
pygame.mixer.set_num_channels(50)

font = pygame.font.Font('assets/Terserah.ttf', 48)
medium_font = pygame.font.Font('assets/Terserah.ttf', 28)
small_font = pygame.font.Font('assets/Terserah.ttf', 16)
real_small_font = pygame.font.Font('assets/Terserah.ttf', 10)
fps = 60
timer = pygame.time.Clock()
WIDTH = 52 * 35
HEIGHT = 400
screen = pygame.display.set_mode([WIDTH, HEIGHT])
white_sounds = []
black_sounds = []
active_whites = []
active_blacks = []
left_oct = 4
right_oct = 5

left_hand = pl.left_hand
right_hand = pl.right_hand
piano_notes = pl.piano_notes
white_notes = pl.white_notes
black_notes = pl.black_notes
black_labels = pl.black_labels




all_sounds = list()

def listWithAdd(list, num):
    newList = list.copy()
    for i in range(len(list)):
        newList[i] = list[i] + num
    return newList

def listWithAddInPlace(list, num):
    for i in range(len(list)):
        list[i] = list[i] + num
    return

isMajor = True
tonicArray = [12, 24, 36, 48]
majorMantis = [0, 2, 4, 5, 7, 9, 11]
minorMantis = [0, 2, 3, 5, 7, 8, 10]

octaves = list()
octaves.append(listWithAdd(majorMantis, tonicArray[0]))
octaves.append(listWithAdd(majorMantis, tonicArray[1]))
octaves.append(listWithAdd(majorMantis, tonicArray[2]))
octaves.append(listWithAdd(majorMantis, tonicArray[3]))












for i in range(len(piano_notes)):
    all_sounds.append(mixer.Sound(f'assets\\notes\\{piano_notes[i]}.wav'))

for i in range(len(white_notes)):
    white_sounds.append(mixer.Sound(f'assets\\originalNotes\\{white_notes[i]}.wav'))

for i in range(len(black_notes)):
    black_sounds.append(mixer.Sound(f'assets\\originalNotes\\{black_notes[i]}.wav'))

pygame.display.set_caption("Eua's Python Piano")


def draw_piano(whites, blacks):
    
    white_rects = []
    for i in range(52):
        rect = pygame.draw.rect(screen, 'white', [i * 35, HEIGHT - 300, 35, 300], 0, 2)
        white_rects.append(rect)
        pygame.draw.rect(screen, 'black', [i * 35, HEIGHT - 300, 35, 300], 2, 2)
        key_label = small_font.render(white_notes[i], True, 'black')
        screen.blit(key_label, (i * 35 + 3, HEIGHT - 20))

    skip_count = 0
    last_skip = 2
    skip_track = 2
    black_rects = []
    for i in range(36):
        rect = pygame.draw.rect(screen, 'black', [23 + (i * 35) + (skip_count * 35), HEIGHT - 300, 24, 200], 0, 2)
        for q in range(len(blacks)):
            if blacks[q][0] == i:
                if blacks[q][1] > 0:
                    pygame.draw.rect(screen, 'green', [23 + (i * 35) + (skip_count * 35), HEIGHT - 300, 24, 200], 2, 2)
                    blacks[q][1] -= 1

        key_label = real_small_font.render(black_labels[i], True, 'white')
        screen.blit(key_label, (25 + (i * 35) + (skip_count * 35), HEIGHT - 120))
        black_rects.append(rect)
        skip_track += 1
        if last_skip == 2 and skip_track == 3:
            last_skip = 3
            skip_track = 0
            skip_count += 1
        elif last_skip == 3 and skip_track == 2:
            last_skip = 2
            skip_track = 0
            skip_count += 1

    for i in range(len(whites)):
        if whites[i][1] > 0:
            j = whites[i][0]
            pygame.draw.rect(screen, 'green', [j * 35, HEIGHT - 100, 35, 100], 2, 2)
            whites[i][1] -= 1



    return white_rects, black_rects, whites, blacks




def draw_title_bar():
    instruction_text = medium_font.render('Up/Down Arrows Change Left Hand', True, 'black')
    screen.blit(instruction_text, (WIDTH - 500, 10))
    instruction_text2 = medium_font.render('Left/Right Arrows Change Right Hand', True, 'black')
    screen.blit(instruction_text2, (WIDTH - 500, 50))
    img = pygame.transform.scale(pygame.image.load('assets/logo.png'), [150, 150])
    screen.blit(img, (-20, -30))
    title_text = font.render('Python Programmable Piano!', True, 'white')
    screen.blit(title_text, (298, 18))
    title_text = font.render('Python Programmable Piano!', True, 'black')
    screen.blit(title_text, (300, 20))





# Preslika index iz piano_notes v [white_keys index, True] oziroma [black_keys index, False]
piano_notes_2_colour_keys = dict()
# tole pa ga konstruira
A_whites_and_blacks_sequence = [True, False, True, True, False, True, False, True, True, False, True, False]
chromatic_len = len(A_whites_and_blacks_sequence)
whiteIx = 0
blackIx = 0
for i in range(8):
    for j in range(len(A_whites_and_blacks_sequence)):
        if(A_whites_and_blacks_sequence[j]):
            piano_notes_2_colour_keys[ i * chromatic_len + j] = [whiteIx, True]
            whiteIx += 1
        else:
            piano_notes_2_colour_keys[ i * chromatic_len + j] = [blackIx, False]
            blackIx += 1

def setActive(piano_notes_ix, activeLen=30):
    currNote = piano_notes_2_colour_keys[piano_notes_ix]
    if (currNote[1]):
        active_whites.append([currNote[0], activeLen])
    else:
        active_blacks.append([currNote[0], activeLen])
    return active_whites, active_blacks






















# This is supposed to stop the KEYUP event happening repededly while you're actually still just holding the key.
# It's also intendend to make the UP arrow key for sharps work as it's supposed to.
pygame.key.set_repeat()

fileName = input("Name of file to play  (end it with .txt): ")
f = open(fileName, "r")
inputStr = f.read()
fps, score = inputStr.split('\n')

fps = int(fps)



offsetBetweenRepetitions = fps * int(input("Time between repetitions in seconds: "))

screen.fill('gray')
white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks)
draw_title_bar()


run = True
while run:

    timeCounter = -offsetBetweenRepetitions
    scoreToPlay = ast.literal_eval(score)

    playRun = True
    while playRun:

        timeCounter += 1

        
        timer.tick(fps)
        screen.fill('gray')
        white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks)
        draw_title_bar()

        
        if len(scoreToPlay) != 0:
            while scoreToPlay[0][1] == timeCounter:
                index = scoreToPlay[0][0]
                all_sounds[index].play(0, 1000)
                setActive(index)
                del scoreToPlay[0]
                if len(scoreToPlay) == 0:
                    playRun = False
                    break



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playRun = False
                run = False
            



            


    pygame.display.flip()
pygame.quit()
