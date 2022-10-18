from pico2d import*

open_canvas()

main_char = load_image('main_move.png')

x = 0
frame = 0
while x < 800:
    clear_canvas()
    main_char.clip_draw(frame * 100, 90)
    x = x + 2
    delay(0.01)

close_canvas()