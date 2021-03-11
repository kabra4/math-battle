import pygame
from settings import Setting
from buttons import *
from question import Question
from stats import Stats
from functions import *
from score import Scoreboard
from timeline import Timeline
def run():
    pygame.init()
    st=Setting()
    screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.get_rect().width=st.screen_w
    screen.get_rect().height=st.screen_h
    pygame.display.set_caption("Math Battle")
    bg2=Bg2(screen)
    ques=Question(screen, st)
    yes=YesNo(screen, 'yes')
    no=YesNo(screen, 'no')
    play=Play(screen)
    stat=Stats(st)
    time=Timeline(screen, stat)
    score=Scoreboard(st, screen, stat)
    gettype(ques, stat)
    while True:
        check_event(ques, stat, score, yes, no, play, time)
        screen.fill(st.bg)
        bg2.bg2draw()
        score.show_score()
        activenot(ques, yes, no, play, time, stat)
        pygame.display.flip()
run()