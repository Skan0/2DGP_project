from pico2d import*

open_canvas()

main_char1 = load_image('main_move1.png')
main_char2 = load_image('main_move2.png')
main_char3 = load_image('main_move3.png')
main_char5 = load_image('main_move5.png')
main_char4_6 = load_image('main_move4_6.png')
main_char7 = load_image('main_move7.png')
main_char8 = load_image('main_move8.png')
main_char9 = load_image('main_move9.png')
frame = 0
# x = 0
# y = 0
# def draw_main():
#     global frame, x, y
#     frame = (frame + 1) % 9
#     if frame == 0:
#         main_char1.draw(x, y)
#     elif frame == 1:
#         main_char2.draw(x, y)
#     elif frame == 2:
#         main_char3.draw(x, y)
#     elif frame == 3:
#         main_char4_6.draw(x, y)
#     elif frame == 4:
#         main_char5.draw(x, y)
#     elif frame == 5:
#         main_char4_6.draw(x, y)
#     elif frame == 6:
#         main_char7.draw(x, y)
#     elif frame == 7:
#         main_char8.draw(x, y)
#     elif frame == 8:
#         main_char9.draw(x, y)
x = 0
y = 90
while x < 800:
    clear_canvas()
    main_char1.draw(x, y)
    update_canvas()
    main_char9.clip_draw(frame * 100, 0, 187, 140, x, y)
    update_canvas()
    frame = (frame + 1) % 9
    x = x + 2
    delay(0.1)
    get_events()

close_canvas()