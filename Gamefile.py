import arcade


WIDTH = 1360
HEIGHT = 680
position_x = WIDTH/2
position_y = HEIGHT/2

up_pressed, down_pressed, right_pressed, left_pressed, fire = False, False, False, False, False

grid = []

bullet_list_x, bullet_list_y = [], []
bullet_count = 0
bullet_index = []
bullet_timer = 0


def on_update(delta_time):
    global position_x, position_y, bullet_count, bullet_index, bullet_timer

    if up_pressed:
        position_y += 5
    if down_pressed:
        position_y -= 5
    if right_pressed:
        position_x += 5
    if left_pressed:
        position_x -= 5

    if position_x > 1335:
        position_x = 1335
    if position_x < 25:
        position_x = 25
    if position_y > 675:
        position_y = 675
    if position_y < 25:
        position_y = 25

    if fire and bullet_timer == 0:
        bullet_list_x.append(position_x)
        bullet_list_y.append(position_y)
        bullet_count += 1
        bullet_timer = 20

    for i in range(bullet_count):
        bullet_list_y[i] += 10

        if bullet_list_y[i] >= 700:
            bullet_index.append(i)

    for j in bullet_index:
        bullet_list_x.pop(j)
        bullet_list_y.pop(j)
        bullet_count -= 1
    bullet_index = []

    if bullet_timer > 0:
        bullet_timer -= 1


def on_draw():
    arcade.start_render()
    # Draw in here...

    for row in range(17):
        for column in range(34):
            if grid[row][column] == 0:
                arcade.draw_rectangle_filled(20 + (column * 40), 20 + (row * 40), 40, 40, arcade.color.GRAY)
            else:
                arcade.draw_rectangle_filled(20 + (column * 40), 20 + (row * 40), 40, 40, arcade.color.BLACK)

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

    arcade.draw_circle_filled(position_x, position_y, 25, arcade.color.BLUE)
    for i in range(bullet_count):
        arcade.draw_rectangle_filled(bullet_list_x[i], bullet_list_y[i], 5, 10, arcade.color.YELLOW)


def on_key_press(key, modifiers):
    global up_pressed, down_pressed, right_pressed, left_pressed, fire
    if key == arcade.key.W:
        up_pressed = True
    if key == arcade.key.S:
        down_pressed = True
    if key == arcade.key.D:
        right_pressed = True
    if key == arcade.key.A:
        left_pressed = True

    if key == arcade.key.SPACE:
        fire = True


def on_key_release(key, modifiers):
    global up_pressed, down_pressed, right_pressed, left_pressed, fire
    if key == arcade.key.W:
        up_pressed = False
    if key == arcade.key.S:
        down_pressed = False
    if key == arcade.key.D:
        right_pressed = False
    if key == arcade.key.A:
        left_pressed = False

    if key == arcade.key.SPACE:
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

    for row in range(17):
        grid.append([])
        for column in range(34):
            grid[row].append(0)

    for row in range(17):
        for column in range(34):
            if row == 0 or row == 16:
                grid[row][column] = 1
            elif column == 0 or column == 33:
                grid[row][column] = 1

    print(grid)
    arcade.run()


if __name__ == '__main__':
    setup()
