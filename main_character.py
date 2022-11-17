import game_world
from pico2d import *

RD, LD, RU, LU  = range(4)
event_name = ['RD', 'LD', 'RU', 'LU']

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}


class character:
    image = None

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
        self.frame = (self.frame + 1) % 10
        self.x += 1
        print('x = ', self.x, 'y = ', self.y)

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

    def draw(self):
        if self.face_dir == 1:
            print('idle_image is none')
        else:
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


next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE}
}