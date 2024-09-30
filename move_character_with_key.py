from pico2d import *


open_canvas(960, 750)
background = load_image('TUK_GROUND.png')
character = load_image('walk.png')


def handle_events():
    global running
    global dir_x
    global dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

        if event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            if event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

running = True
x = 960 // 2
y = 300
width = 960
height = 750
frame = 0
dir_x = 0
dir_y = 0
flip = ''
while running:
    clear_canvas()
    background.draw(480, 375, 960, 750)

    if dir_x == 1:
        flip = ''
    elif dir_x == -1:
        flip = 'h'

    character.clip_composite_draw(frame * 128, 0, 128, 128, 0, flip, x, y, 200, 200)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 6
    x += dir_x * 5
    delay(0.05)


close_canvas()