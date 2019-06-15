import arcade


WIDTH = 1280
HEIGHT = 720

player_x_coord = 2
player_y_coord = 6
start_coord_x = 1
start_coord_y = 1
player_speed = 10
x_move, y_move = 0, 0
move_up, move_down, move_right, move_left = True, True, True, True
movable = True

up_pressed, down_pressed, right_pressed, left_pressed, fire = False, False, False, False, False
player_idle_up, player_idle_down, player_idle_right, player_idle_left = False, False, False, False
fire_up, fire_down, fire_right, fire_left = False, False, False, False

map_setup = False
mapcounter = 1

grid = []

bullet_list_x, bullet_list_y, bullet_direction = [], [], []
bullet_count = 0
bullet_timer = 0
bullet_index = []
bullet_amount = 0
bullet_collected1, bullet_collected2, bullet_activated1, bullet_activated2 = False, False, False, False

char_model_up = arcade.load_texture("images/Model2_Up.png")
char_model_down = arcade.load_texture("images/Model2_Down.png")
char_model_right = arcade.load_texture("images/Model2_Right.png")
char_model_left = arcade.load_texture("images/Model2_Left.png")
arrow = arcade.load_texture("images/arrow.png")
tile0 = arcade.load_texture("images/tile0.png")
tile1 = arcade.load_texture("images/tile1.png")
tile2 = arcade.load_texture("images/tile2.jpg")
tile3 = arcade.load_texture("images/tile3.png")
tile4 = arcade.load_texture("images/tile4.png")
tile5 = arcade.load_texture("images/tile5.png")
tile6 = arcade.load_texture("images/tile6.gif")
tile7 = arcade.load_texture("images/tile7.png")

# temporary
mapcounter_cheat = False


def door1(y, x):
    if bullet_activated1:
        grid[y][x] = 0
    else:
        grid[y][x] = 7


def door2(y, x):
    if bullet_activated2:
        grid[y][x] = 0
    else:
        grid[y][x] = 7


def bullet_activate1(y, x):
    global bullet_activated1
    grid[y][x] = 3
    for i in range(bullet_count):
        if bullet_list_y[i] // 80 == y and bullet_list_x[i] // 80 == x:
            bullet_index.append(i)
            bullet_activated1 = True


def bullet_activate2(y, x):
    global bullet_activated2
    grid[y][x] = 3
    for i in range(bullet_count):
        if bullet_list_y[i] // 80 == y and bullet_list_x[i] // 80 == x:
            bullet_index.append(i)
            bullet_activated2 = True


def bullet_collect1(y, x):
    global bullet_collected1, bullet_amount
    if not bullet_collected1:
        grid[y][x] = 4
    else:
        grid[y][x] = 0
    if player_y_coord == y and player_x_coord == x and not bullet_collected1:
        bullet_collected1 = True
        bullet_amount += 1


def bullet_collect2(y, x):
    global bullet_collected2, bullet_amount
    if not bullet_collected2:
        grid[y][x] = 4
    else:
        grid[y][x] = 0
    if player_y_coord == y and player_x_coord == x and not bullet_collected2:
        bullet_collected2 = True
        bullet_amount += 1


def tile_check():
    global movable, player_speed, mapcounter, map_setup
    if up_pressed:
        if grid[player_y_coord + 1][player_x_coord] == 1:
            movable = False
        elif grid[player_y_coord + 1][player_x_coord] == 2:
            player_speed = 20
            movable = True
        elif grid[player_y_coord + 1][player_x_coord] == 3:
            movable = True
        elif grid[player_y_coord + 1][player_x_coord] == 4:
            pass
        elif grid[player_y_coord + 1][player_x_coord] == 5:
            movable = False
        elif grid[player_y_coord + 1][player_x_coord] == 7:
            movable = False
        else:
            movable = True
            player_speed = 10
    elif down_pressed:
        if grid[player_y_coord - 1][player_x_coord] == 1:
            movable = False
        elif grid[player_y_coord - 1][player_x_coord] == 2:
            player_speed = 20
            movable = True
        elif grid[player_y_coord - 1][player_x_coord] == 3:
            movable = True
        elif grid[player_y_coord - 1][player_x_coord] == 4:
            pass
        elif grid[player_y_coord - 1][player_x_coord] == 5:
            movable = False
        elif grid[player_y_coord - 1][player_x_coord] == 7:
            movable = False
        else:
            movable = True
            player_speed = 10
    elif right_pressed:
        if grid[player_y_coord][player_x_coord + 1] == 1:
            movable = False
        elif grid[player_y_coord][player_x_coord + 1] == 2:
            player_speed = 20
            movable = True
        elif grid[player_y_coord][player_x_coord + 1] == 3:
            movable = True
        elif grid[player_y_coord][player_x_coord + 1] == 4:
            pass
        elif grid[player_y_coord][player_x_coord + 1] == 5:
            movable = False
        elif grid[player_y_coord][player_x_coord + 1] == 7:
            movable = False
        else:
            movable = True
            player_speed = 10
    elif left_pressed:
        if grid[player_y_coord][player_x_coord - 1] == 1:
            movable = False
        elif grid[player_y_coord][player_x_coord - 1] == 2:
            player_speed = 20
            movable = True
        elif grid[player_y_coord][player_x_coord - 1] == 3:
            movable = True
        elif grid[player_y_coord][player_x_coord - 1] == 4:
            pass
        elif grid[player_y_coord][player_x_coord - 1] == 5:
            movable = False
        elif grid[player_y_coord][player_x_coord - 1] == 7:
            movable = False
        else:
            movable = True
            player_speed = 10

    if grid[player_y_coord][player_x_coord] == 6:
        mapcounter += 1
        map_setup = True


def on_update(delta_time):
    global position_x, position_y, bullet_direction, bullet_count, bullet_index, bullet_timer, move_up, move_down, \
        move_right, move_left, x_move, y_move, player_x_coord, player_y_coord, mapcounter, map_setup, bullet_amount, \
        bullet_collected1, bullet_collected2, bullet_activated1, bullet_activated2, start_coord_x, start_coord_y

    position_x, position_y = 40 + (player_x_coord * 80) + x_move, 40 + (player_y_coord * 80) + y_move

    tile_check()
    if up_pressed and move_down and move_right and move_left and movable or not move_up:
        if y_move < 80:
            y_move += player_speed
            move_up = False
        else:
            player_y_coord += 1
            move_up = True
            y_move = 0
    elif down_pressed and move_up and move_right and move_left and movable or not move_down:
        if y_move > -80:
            y_move -= player_speed
            move_down = False
        else:
            player_y_coord -= 1
            move_down = True
            y_move = 0
    elif right_pressed and move_up and move_down and move_left and movable or not move_right:
        if x_move < 80:
            x_move += player_speed
            move_right = False
        else:
            player_x_coord += 1
            move_right = True
            x_move = 0
    elif left_pressed and move_up and move_down and move_right and movable or not move_left:
        if x_move > -80:
            x_move -= player_speed
            move_left = False
        else:
            player_x_coord -= 1
            move_left = True
            x_move = 0

    # bullet code
    if fire and bullet_amount > 0 and bullet_timer == 0:
        if fire_up:
            bullet_direction.append("up")
        elif fire_down:
            bullet_direction.append("down")
        elif fire_right:
            bullet_direction.append("right")
        elif fire_left:
            bullet_direction.append("left")

        bullet_list_x.append(position_x)
        bullet_list_y.append(position_y)

        bullet_count += 1
        bullet_timer = 20
        bullet_amount -= 1

    for i in range(bullet_count):
        if bullet_direction[i] == "up":
            bullet_list_y[i] += 20
        elif bullet_direction[i] == "down":
            bullet_list_y[i] -= 20
        elif bullet_direction[i] == "right":
            bullet_list_x[i] += 20
        elif bullet_direction[i] == "left":
            bullet_list_x[i] -= 20

        if grid[bullet_list_y[i]//80][bullet_list_x[i]//80] == 1:
            bullet_index.append(i)

    for _ in bullet_index:
        bullet_list_x.pop(0)
        bullet_list_y.pop(0)
        bullet_direction.pop(0)
        bullet_count -= 1
    bullet_index = []

    if bullet_timer > 0:
        bullet_timer -= 1

    # if mapcounter == 1:
    #     grid[5][5] = 1
    #     grid[6][7] = 1
    #     grid[4][8] = 1
    #     grid[3][6] = 1
    #     grid[2][3] = 2
    #     grid[2][4] = 2
    #     grid[2][5] = 2
    #     grid[2][6] = 2
    #     grid[5][13] = 5
    #     grid[6][13] = 6
    #
    #     bullet_collect1(3, 5)
    #     bullet_activate1(3, 12)
    if mapcounter == 1:
        print(player_y_coord, player_x_coord)

        grid[2][13] = 6
    elif mapcounter == 2:
        start_coord_y, start_coord_x = 2, 2

        for i in range(4):
            grid[i][5] = 1

        for i in range(3, 8):
            grid[i][10] = 1

        grid[6][13] = 6

    elif mapcounter >= 3:
        start_coord_y, start_coord_x = 2, 2

        grid[1][8] = 1
        grid[3][8] = 1
        grid[4][8] = 1

        for i in range(5, 8):
            grid[i][8] = 5

        bullet_collect1(6, 2)
        bullet_activate1(6, 13)
        door1(2, 8)

        grid[2][13] = 6

    if map_setup:
        for row in range(9):
            for column in range(16):
                if row == 0 or row == 8:
                    grid[row][column] = 1
                elif column == 0 or column == 15:
                    grid[row][column] = 1
                else:
                    grid[row][column] = 0

        player_x_coord, player_y_coord = start_coord_x, start_coord_y
        map_setup = False
        bullet_collected1, bullet_collected2 = False, False
        bullet_activated1, bullet_activated2 = False, False
        bullet_amount = 0

    # temporary
    if mapcounter_cheat:
        mapcounter += 1
        map_setup = True


def on_draw():
    global row, column
    arcade.start_render()
    # Draw in here...
    for row in range(9):
        for column in range(16):
            if grid[row][column] == 0:
                arcade.draw_texture_rectangle(40 + (column * 80), 40 + (row * 80), 80, 80, tile0)
            elif grid[row][column] == 1:
                arcade.draw_texture_rectangle(40 + (column * 80), 40 + (row * 80), 80, 80, tile1)
            elif grid[row][column] == 2:
                arcade.draw_texture_rectangle(40 + (column * 80), 40 + (row * 80), 80, 80, tile2)
            elif grid[row][column] == 3:
                arcade.draw_texture_rectangle(40 + (column * 80), 40 + (row * 80), 80, 80, tile3)
            elif grid[row][column] == 4:
                arcade.draw_texture_rectangle(40 + (column * 80), 40 + (row * 80), 80, 80, tile4)
            elif grid[row][column] == 5:
                arcade.draw_texture_rectangle(40 + (column * 80), 40 + (row * 80), 80, 80, tile5)
            elif grid[row][column] == 6:
                arcade.draw_texture_rectangle(40 + (column * 80), 40 + (row * 80), 80, 80, tile6)
            elif grid[row][column] == 7:
                arcade.draw_texture_rectangle(40 + (column * 80), 40 + (row * 80), 80, 80, tile7)
            else:
                arcade.draw_rectangle_filled(40 + (column * 80), 40 + (row * 80), 80, 80, arcade.color.LIGHT_GRAY)

    for i in range(bullet_count):
        arcade.draw_texture_rectangle(bullet_list_x[i], bullet_list_y[i], 87, 22.5, arrow)

    if mapcounter == 1:
        arcade.draw_text("Welcome to the Escapade", 200, 430, arcade.color.WHITE, 30)
        arcade.draw_text("The goal is to reach the portal at the end of each room", 200, 350, arcade.color.WHITE, 30)
        arcade.draw_text("Use WASD to move around", 200, 270, arcade.color.WHITE, 30)
        arcade.draw_text("Enter the portal to move to the next room ------->", 200, 190, arcade.color.WHITE, 30)
    elif mapcounter == 2:
        arcade.draw_text("Wall blocks are tiles that can not be passed through ---->", 120, 350, arcade.color.WHITE, 21)
    elif mapcounter >= 3:
        arcade.draw_text("Arrows can be collected and shot using the arrow keys", 100, 590, arcade.color.WHITE, 15)
        arcade.draw_text("They can only pass through certain walls", 100, 430, arcade.color.WHITE, 15)
        arcade.draw_text("Press R to reset the current room", 100, 350, arcade.color.WHITE, 15)

    if fire_up:
        arcade.draw_texture_rectangle(position_x, position_y, 56, 80, char_model_up)
    elif fire_down:
        arcade.draw_texture_rectangle(position_x, position_y, 56, 80, char_model_down)
    elif fire_right:
        arcade.draw_texture_rectangle(position_x, position_y, 56, 80, char_model_right)
    elif fire_left:
        arcade.draw_texture_rectangle(position_x, position_y, 56, 80, char_model_left)
    elif player_idle_up:
        arcade.draw_texture_rectangle(position_x, position_y, 56, 80, char_model_up)
    elif player_idle_down:
        arcade.draw_texture_rectangle(position_x, position_y, 56, 80, char_model_down)
    elif player_idle_right:
        arcade.draw_texture_rectangle(position_x, position_y, 56, 80, char_model_right)
    elif player_idle_left:
        arcade.draw_texture_rectangle(position_x, position_y, 56, 80, char_model_left)
    else:
        arcade.draw_texture_rectangle(position_x, position_y, 56, 80, char_model_up)


def on_key_press(key, modifiers):
    global up_pressed, down_pressed, right_pressed, left_pressed, fire, player_idle_up, player_idle_down, \
        player_idle_right, player_idle_left, fire_up, fire_down, fire_right, fire_left, mapcounter_cheat
    if key == arcade.key.W:
        up_pressed = True
        player_idle_up, player_idle_down, player_idle_right, player_idle_left = True, False, False, False
    if key == arcade.key.S:
        down_pressed = True
        player_idle_up, player_idle_down, player_idle_right, player_idle_left = False, True, False, False
    if key == arcade.key.D:
        right_pressed = True
        player_idle_up, player_idle_down, player_idle_right, player_idle_left = False, False, True, False
    if key == arcade.key.A:
        left_pressed = True
        player_idle_up, player_idle_down, player_idle_right, player_idle_left = False, False, False, True

    if key == arcade.key.UP:
        fire_up, fire_down, fire_right, fire_left = True, False, False, False
        fire = True
    elif key == arcade.key.DOWN:
        fire_up, fire_down, fire_right, fire_left = False, True, False, False
        fire = True
    elif key == arcade.key.RIGHT:
        fire_up, fire_down, fire_right, fire_left = False, False, True, False
        fire = True
    elif key == arcade.key.LEFT:
        fire_up, fire_down, fire_right, fire_left = False, False, False, True
        fire = True

    # temporary
    if key == arcade.key.KEY_0:
        mapcounter_cheat = True


def on_key_release(key, modifiers):
    global up_pressed, down_pressed, right_pressed, left_pressed, fire, player_idle_up, player_idle_down, \
        player_idle_right, player_idle_left, fire_up, fire_down, fire_right, fire_left, map_setup, mapcounter_cheat
    if key == arcade.key.W:
        up_pressed = False
    if key == arcade.key.S:
        down_pressed = False
    if key == arcade.key.D:
        right_pressed = False
    if key == arcade.key.A:
        left_pressed = False

    if key == arcade.key.UP:
        fire_up = False
        fire = False
    if key == arcade.key.DOWN:
        fire_down = False
        fire = False
    if key == arcade.key.RIGHT:
        fire_right = False
        fire = False
    if key == arcade.key.LEFT:
        fire_left = False
        fire = False

    if key == arcade.key.R:
        map_setup = True
    # temporary
    if key == arcade.key.KEY_0:
        mapcounter_cheat = False


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.GRAY)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    for row in range(9):
        grid.append([])
        for column in range(16):
            grid[row].append(0)

    for row in range(9):
        for column in range(16):
            if row == 0 or row == 8:
                grid[row][column] = 1
            elif column == 0 or column == 15:
                grid[row][column] = 1

    arcade.run()


if __name__ == '__main__':
    setup()
