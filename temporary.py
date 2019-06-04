import arcade


WIDTH = 1280
HEIGHT = 720
position_x = WIDTH/2
position_y = HEIGHT/2

up_pressed, down_pressed, right_pressed, left_pressed, fire = False, False, False, False, False
player_idle_up, player_idle_down, player_idle_right, player_idle_left = False, False, False, False
fire_up, fire_down, fire_right, fire_left = False, False, False, False

grid = []

collision_up, collision_down, collision_right, collision_left = True, True, True, True

bullet_list_x, bullet_list_y, bullet_direction = [], [], []
bullet_count = 0
bullet_index = []
bullet_timer = 0

char_model = arcade.load_texture("images/Model1_Right.png")
wall = arcade.load_texture("images/wall.png")


def on_update(delta_time):
    global position_x, position_y, bullet_direction, bullet_count, bullet_index, bullet_timer, collision_up, \
        collision_down, collision_right, collision_left

    if up_pressed:
        position_y += 5
    if down_pressed:
        position_y -= 5
    if right_pressed:
        position_x += 5
    if left_pressed:
        position_x -= 5

    # temporary
    if position_x > 1175:
        position_x = 1175
    if position_x < 105:
        position_x = 105
    if position_y > 615:
        position_y = 615
    if position_y < 105:
        position_y = 105

    if 375 < position_x < 505 and 375 < position_y < 505:
        if player_idle_up and collision_down and collision_right and collision_left:
            position_y = 375
            collision_up = False
        elif player_idle_down and collision_up and collision_right and collision_left:
            position_y = 505
            collision_down = False
        if player_idle_right and collision_up and collision_down and collision_left:
            position_x = 375
            collision_right = False
        elif player_idle_left and collision_up and collision_down and collision_right:
            position_x = 505
            collision_left = False
    else:
        collision_up, collision_down, collision_right, collision_left = True, True, True, True

    # print(collision_up, collision_down, collision_right, collision_left)
    print(player_idle_up, player_idle_down, player_idle_right, player_idle_left)

    # bullet code
    if fire and bullet_timer == 0:
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

    for i in range(bullet_count):
        if bullet_direction[i] == "up":
            bullet_list_y[i] += 20
        elif bullet_direction[i] == "down":
            bullet_list_y[i] -= 20
        elif bullet_direction[i] == "right":
            bullet_list_x[i] += 20
        elif bullet_direction[i] == "left":
            bullet_list_x[i] -= 20

        if bullet_list_y[i] >= 640 or bullet_list_y[i] <= 80 or bullet_list_x[i] >= 1200 or bullet_list_x[i] <= 80:
            bullet_index.append(i)

    for _ in bullet_index:
        bullet_list_x.pop(0)
        bullet_list_y.pop(0)
        bullet_direction.pop(0)
        bullet_count -= 1
    bullet_index = []

    if bullet_timer > 0:
        bullet_timer -= 1


def on_draw():
    arcade.start_render()
    # Draw in here...
    for row in range(9):
        for column in range(16):
            if grid[row][column] == 0:
                arcade.draw_rectangle_filled(40 + (column * 80), 40 + (row * 80), 80, 80, arcade.color.GRAY_BLUE)
            else:
                # arcade.draw_rectangle_filled(40 + (column * 80), 40 + (row * 80), 80, 80, arcade.color.BLACK)
                arcade.draw_texture_rectangle(40 + (column * 80), 40 + (row * 80), 80, 80, wall)

            """
            if column%2 == 0:
                if row % 2 == 0:
                    arcade.draw_rectangle_filled(20 + (row * 40), 20 + (column * 40), 40, 40, arcade.color.GRAY)
                else:
                    arcade.draw_rectangle_filled(20 + (row * 40), 20 + (column * 40), 40, 40, arcade.color.BLACK)
            else:
                if row % 2 == 1:
                    arcade.draw_rectangle_filled(20 + (row * 40), 20 + (column * 40), 40, 40, arcade.color.GRAY)
                else:
                    arcade.draw_rectangle_filled(20 + (row * 40), 20 + (column * 40), 40, 40, arcade.color.BLACK)
            """

    for i in range(bullet_count):
        arcade.draw_circle_filled(bullet_list_x[i], bullet_list_y[i], 5, arcade.color.YELLOW)
    arcade.draw_circle_filled(position_x, position_y, 25, arcade.color.BLUE)

    if fire_up:
        arcade.draw_text("up", position_x, position_y, arcade.color.BLACK, 12)
    elif fire_down:
        arcade.draw_text("down", position_x, position_y, arcade.color.BLACK, 12)
    elif fire_right:
        arcade.draw_text("right", position_x, position_y, arcade.color.BLACK, 12)
    elif fire_left:
        arcade.draw_text("left", position_x, position_y, arcade.color.BLACK, 12)
    elif player_idle_up:
        arcade.draw_text("up", position_x, position_y, arcade.color.BLACK, 12)
    elif player_idle_down:
        arcade.draw_text("down", position_x, position_y, arcade.color.BLACK, 12)
    elif player_idle_right:
        arcade.draw_text("right", position_x, position_y, arcade.color.BLACK, 12)
    elif player_idle_left:
        arcade.draw_text("left", position_x, position_y, arcade.color.BLACK, 12)


def on_key_press(key, modifiers):
    global up_pressed, down_pressed, right_pressed, left_pressed, fire, player_idle_up, player_idle_down, \
        player_idle_right, player_idle_left, fire_up, fire_down, fire_right, fire_left
    if key == arcade.key.W:
        up_pressed = True
        player_idle_up = True
    if key == arcade.key.S:
        down_pressed = True
        player_idle_down = True
    if key == arcade.key.D:
        right_pressed = True
        player_idle_right = True
    if key == arcade.key.A:
        left_pressed = True
        player_idle_left = True

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


def on_key_release(key, modifiers):
    global up_pressed, down_pressed, right_pressed, left_pressed, fire, player_idle_up, player_idle_down, \
        player_idle_right, player_idle_left, fire_up, fire_down, fire_right, fire_left
    if key == arcade.key.W:
        up_pressed = False
        player_idle_up = False
    if key == arcade.key.S:
        down_pressed = False
        player_idle_down = False
    if key == arcade.key.D:
        right_pressed = False
        player_idle_right = False
    if key == arcade.key.A:
        left_pressed = False
        player_idle_left = False

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

    grid[5][5] = 1

    arcade.run()


if __name__ == '__main__':
    setup()
