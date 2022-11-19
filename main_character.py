import game_world
from pico2d import *

RD, LD, RU, LU, ATTACK1, ATTACK2, ATTACK3,ATTACK_OFF, SUMMON1, SUMMON2, SUMMON3,\
    SUMMON4, SUMMON5, SUMMON6, SUMMON7, SUMMON8, SUMMON9 = range(17)
event_name = ['RD', 'LD', 'RU', 'LU', 'ATTACK1', 'ATTACK2', 'ATTACK3',
              'SUMMON1', 'SUMMON2', 'SUMMON3', 'SUMMON4', 'SUMMON5', 'SUMMON6', 'SUMMON7', 'SUMMON8', 'SUMMON9']

key_event_table = {
    (SDL_KEYDOWN, SDLK_1): SUMMON1,
    (SDL_KEYDOWN, SDLK_2): SUMMON2,
    (SDL_KEYDOWN, SDLK_3): SUMMON3,
    (SDL_KEYDOWN, SDLK_4): SUMMON4,
    (SDL_KEYDOWN, SDLK_5): SUMMON5,
    (SDL_KEYDOWN, SDLK_6): SUMMON6,
    (SDL_KEYDOWN, SDLK_7): SUMMON7,
    (SDL_KEYDOWN, SDLK_8): SUMMON8,
    (SDL_KEYDOWN, SDLK_9): SUMMON9,
    (SDL_KEYDOWN, SDLK_k): ATTACK3,
    (SDL_KEYDOWN, SDLK_l): ATTACK2,
    (SDL_KEYDOWN, SDLK_j): ATTACK1,
    # (SDL_KEYUP, SDLK_j, SDLK_k, SDLK_l): ATTACK_OFF,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}


class Character:

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def __init__(self):
        self.x, self.y = 100, 90,
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.first = load_image('main_move1.PNG')
        self.second = load_image('main_move2.PNG')
        self.third = load_image('main_move3.PNG')
        self.fourth_sixth = load_image('main_move4_6.PNG')
        self.fifth = load_image('main_move5.PNG')
        self.seventh = load_image('main_move7.PNG')
        self.eighth = load_image('main_move8.PNG')
        self.ninth = load_image('main_move9.PNG')
        self.first_b = load_image('main_move1b.PNG')
        self.second_b = load_image('main_move2b.PNG')
        self.third_b = load_image('main_move3b.PNG')
        self.fourth_sixth_b = load_image('main_move4_6b.PNG')
        self.fifth_b = load_image('main_move5b.PNG')
        self.seventh_b = load_image('main_move7b.PNG')
        self.eighth_b = load_image('main_move8b.PNG')
        self.ninth_b = load_image('main_move9b.PNG')
        self.timer = 100
        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)
        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}  Event{event_name[event]}')
            self.cur_state.enter(self, event)
        # self.frame = (self.frame + 1) % 10
        # self.x += 1
        # print('x = ', self.x, 'y = ', self.y)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
        # if self.frame == 1:
        #     self.first.draw(self.x, self.y)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def handle_collision(self, other, group):
        pass


class IDLE:
    @staticmethod
    def enter(self, event):
        print('enter IDLE')
        self.dir = 0
        self.timer = 1000

    @staticmethod
    def exit(self, event):
        print('exit IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            print('idle_image is none')
        else:
            pass


class SUMMON:
    # 1~9 번의 아군을 소환
    pass


class ATTACK:
    def enter(self, event):
        pass

    def exit(self, event):
        pass

    def do(self):
        # 공격 하는 주인공 이미지
        pass
    def draw(self):
        # 1번 무기 2번 무기 3번 무기 공격 나가게 세팅
        pass


class RUN:
    def enter(self, event):
        print('enter run')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self, event):
        print('Exit run')
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + 1) % 9
        self.x += self.face_dir
        self.x = clamp(0, self.x, 1137)

    def draw(self):
        if self.dir == -1:
            if self.frame == 0:
                self.first.draw(self.x, self.y)
            elif self.frame == 1:
                self.second.draw(self.x, self.y)
            elif self.frame == 2:
                self.third.draw(self.x, self.y)
            elif self.frame == 3:
                self.fourth_sixth.draw(self.x, self.y)
            elif self.frame == 4:
                self.fifth.draw(self.x, self.y)
            elif self.frame == 5:
                self.fourth_sixth.draw(self.x, self.y)
            elif self.frame == 6:
                self.seventh.draw(self.x, self.y)
            elif self.frame == 7:
                self.eighth.draw(self.x, self.y)
            elif self.frame == 8:
                self.ninth.draw(self.x, self.y)
        elif self.dir == -1:
            if self.frame == 0:
                self.first_b.draw(self.x, self.y)
            elif self.frame == 1:
                self.second_b.draw(self.x, self.y)
            elif self.frame == 2:
                self.third_b.draw(self.x, self.y)
            elif self.frame == 3:
                self.fourth_sixth_b.draw(self.x, self.y)
            elif self.frame == 4:
                self.fifth_b.draw(self.x, self.y)
            elif self.frame == 5:
                self.fourth_sixth.draw_b(self.x, self.y)
            elif self.frame == 6:
                self.seventh_b.draw(self.x, self.y)
            elif self.frame == 7:
                self.eighth_b.draw(self.x, self.y)
            elif self.frame == 8:
                self.ninth_b.draw(self.x, self.y)


next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, SUMMON1: SUMMON, SUMMON2: SUMMON, SUMMON3: SUMMON, SUMMON4: SUMMON,
           SUMMON5: SUMMON, SUMMON6: SUMMON, SUMMON7: SUMMON, SUMMON8: SUMMON, SUMMON9: SUMMON, ATTACK1: ATTACK,
           ATTACK2: ATTACK, ATTACK3: ATTACK},
    ATTACK: {ATTACK1: IDLE, ATTACK2: IDLE, ATTACK3: IDLE},
    SUMMON: {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE}
}