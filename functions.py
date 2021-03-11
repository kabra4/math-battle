import sys, pygame
from time import time as ttime
from time import sleep
from random import choice, randint
def check_keydown(event, ques, stat, score, time):
    if event.key==pygame.K_RIGHT:
        ques.yesno=False
        checktruefalse(ques, stat, score, time)
    elif event.key==pygame.K_LEFT:
        ques.yesno=True
        checktruefalse(ques, stat, score, time)
    elif event.key==pygame.K_SPACE:
        startgame(stat, score)
    elif event.key==pygame.K_q:
        sys.exit()
    elif event.key==pygame.K_ESCAPE:
        sys.exit()

def endgame(stat, ques):
    if stat.timeleft>2:
        stat.endtime-=2.5
        gettype(ques, stat)
    else:
        stat.game_active=False
        stat.reset_stats()
        gettype(ques, stat)
        sleep(2)


def startgame(stat, score):
    stat.reset_stats()
    stat.game_active=True
    score.prep_top()
    score.prep_score()
    stat.endtime=ttime()+15

def activenot(ques, yes, no, play, time, stat):
    if stat.game_active:
        ques.show_q()
        yes.blitme()
        no.blitme()
        stat.current=ttime()
        stat.timeleft=stat.endtime-stat.current
        if stat.timeleft<=0:
            stat.game_active=False
        else:
            time.prep()
            time.draw()
    else:
        play.blitme()

def nextr(ques, stat, score, time):
    stat.score+=1
    score.prep_score()
    if stat.timeleft>13:
        stat.endtime=15+stat.current
    else:
        stat.endtime+=2
    time.prep()
    check_record(stat, score)
    gettype(ques, stat)

def checktruefalse(ques, stat, score, time):
    if ques.q and ques.yesno and stat.game_active:
        nextr(ques, stat, score, time)
    elif not ques.q and not ques.yesno and stat.game_active:
        nextr(ques, stat, score, time)
    else:
        endgame(stat, ques)


def check_event(ques, stat, score, yes, no, play, time):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown(event, ques, stat, score, time)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            x, y=pygame.mouse.get_pos()
            mousekey(ques, stat, score, play, time, yes, no, x, y)

def mousekey(ques, stat, score, play, time, yes, no, x, y):
    if play.rect.collidepoint(x, y) and not stat.game_active:
        startgame(stat, score)
    elif yes.rect.collidepoint(x, y):
        ques.yesno=True
        checktruefalse(ques, stat, score, time)
    elif no.rect.collidepoint(x, y):
        ques.yesno=False
        checktruefalse(ques, stat, score, time)

def gettype(ques, stat):
    ques.sign=choice(['+','-','*','/'])
    if ques.sign=='+':
        plus(ques, stat)
    elif ques.sign=='-':
        minus(ques, stat)
    elif ques.sign=='*':
        multiply(ques, stat)
    else:
        divide(ques, stat)

def wrongans(ques, stat):
    if choice([True, False]):
        ques.ans=ques.tans+randint(1, stat.score+1)
    else:
        while ques.ans<=0:
            ques.ans=ques.tans-randint(1, stat.score+1)
    ques.prep()

def plus(ques, stat):
    ques.sign='+'
    ques.q=choice([True, False])
    ques.e1=randint(stat.score*2, stat.score*15)
    ques.e2=randint(stat.score*2, stat.score*15)
    ques.tans=ques.e1+ques.e2
    if ques.q:
        ques.ans=ques.tans
        ques.prep()
    else:
        wrongans(ques, stat)

def minus(ques, stat):
    ques.sign='-'
    ques.q=choice([True, False])
    ques.e1=randint(stat.score*5, stat.score*15)
    ques.e2=randint(stat.score*2, ques.e1-1)
    ques.tans=ques.e1-ques.e2
    if ques.q:
        ques.ans=ques.tans
        ques.prep()
    else:
        wrongans(ques, stat)

def multiply(ques, stat):
    ques.sign='*'
    ques.q=choice([True, False])
    if stat.score>15:
        ques.e1=randint(5, stat.score)
        ques.e2=randint(5, stat.score)
    else:
        ques.e1=randint(stat.score, stat.score*2)
        ques.e2=randint(stat.score, stat.score*2)
    ques.tans=round(ques.e1*ques.e2)
    if ques.q:
        ques.ans=ques.tans
        ques.prep()
    else:
        wrongans(ques, stat)

def divide(ques, stat):
    ques.sign='/'
    ques.q=choice([True, False])
    if stat.score>15:
        me1=randint(5, stat.score)
        me2=randint(5, stat.score)
    else:
        me1=randint(stat.score*2, stat.score*4)
        me2=randint(stat.score, stat.score*3)
    ques.e1=round(me1*me2)
    ques.e2=round(ques.e1/me1)
    ques.tans=round(ques.e1/ques.e2)
    if ques.q:
        ques.ans=ques.tans
        ques.prep()
    else:
        wrongans(ques, stat)

def check_record(stat, score):
    if stat.score>stat.top_score:
        stat.top_score=stat.score
        score.prep_top()

def updatescreen(screen, bg2, st, score, stat):
    screen.fill(st.bg)
    bg2.bg2draw()
    score.show_score()