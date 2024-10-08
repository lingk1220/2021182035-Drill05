from pico2d import *

running = True
x = 960 // 2
y = 300
width = 960
height = 750
frame = 0
dir_x = 0
dir_y = 0
flip = ''
sprite_size = 128

open_canvas(width, height)
background = load_image('TUK_GROUND.png')
character_walk = load_image('walk.png')
character_idle = load_image('idle.png')

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

def move():
    global x, y

    x += dir_x * 5
    if 0 > x - sprite_size//2 + 60 or width < x + sprite_size//2 - 60:
        x -= dir_x * 5

    y += dir_y * 5
    if 0 > y - sprite_size//2 - 35 or height < y + sprite_size//2 - 65:
        y -= dir_y * 5

while running:
    clear_canvas()
    background.draw(width/2, height/2, width, height)

    if dir_x == 1:
        flip = ''
    elif dir_x == -1:
        flip = 'h'

    if dir_x == 0 and dir_y == 0:
        character_idle.clip_composite_draw(frame * sprite_size, 0, sprite_size, sprite_size, 0, flip, x, y, 200, 200)
    else:
        character_walk.clip_composite_draw(frame * sprite_size, 0, sprite_size, sprite_size, 0, flip, x, y, 200, 200)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 7
    move()
    delay(0.05)


close_canvas()