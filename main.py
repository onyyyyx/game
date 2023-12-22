def on_button_pressed_a():
    global posX
    led.unplot(posX, 4)
    posX = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global posX
    led.unplot(posX, 4)
    posX = 4
input.on_button_pressed(Button.B, on_button_pressed_b)

posX = 0
i = 0
game.set_score(0)
posX = 0
dangerY = [-2, -4]
dangerSide=[True, False]
#dangerSide = [Math.random_boolean(), Math.random_boolean()]
dangerLength=[2,4]
#dangerLength = [randint(0, 4), randint(0, 4)]

def on_forever():
    global i
    led.plot(posX, 4)
    while i < 2:
        if dangerSide[i]:
            j = 0
            while j < dangerLength[i]:
                led.unplot(j, dangerY[i] - 1)
                if led.point(j, dangerY[i]):
                    game.game_over()
                led.plot_brightness(j, dangerY[i], 140)
                j += 1
        else:
            j = 0
            while j < dangerLength[i]:
                led.unplot(5 - j, dangerY[i] - 1)
                if led.point(5 - j, dangerY[i]):
                    game.game_over()
                led.plot_brightness(5 - j, dangerY[i], 140)
                j += 1
        if dangerY[i] >= 5:
            dangerY.remove_at(i)
            dangerLength.remove_at(i)
            dangerSide.remove_at(i)
            dangerSide.append(False)
            #dangerSide.append(Math.random_boolean())
            dangerY.append(0)
            dangerLength.append(1)
            #dangerLength.append(randint(0, 4))
        dangerY[i] += 1
        i += 1
basic.forever(on_forever)
