import game_framework
import pico2d
import play_state
# import logo_state

# start_state = logo_state
pico2d.open_canvas(1137, 854)
# game_framework.run(logo_state)
game_framework.run(play_state)
pico2d.close_canvas()
