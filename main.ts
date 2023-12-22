input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    led.unplot(posX, 4)
    posX = 0
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    led.unplot(posX, 4)
    posX = 4
})
let posX = 0
let i = 0
game.setScore(0)
posX = 0
let dangerY = [-2, -4]
let dangerSide = [Math.randomBoolean(), Math.randomBoolean()]
let dangerLength = [randint(0, 4), randint(0, 4)]
basic.forever(function on_forever() {
    let j: number;
    
    led.plot(posX, 4)
    while (i < 2) {
        if (dangerSide[i] == true) {
            j = 0
            while (j < dangerLength[i]) {
                led.unplot(j, dangerY[i] - 1)
                if (led.point(j, dangerY[i])) {
                    game.gameOver()
                }
                
                led.plotBrightness(j, dangerY[i], 140)
                j += 1
            }
        } else if (dangerSide[i] == false) {
            j = 0
            while (j < dangerLength[i]) {
                led.unplot(5 - j, dangerY[i] - 1)
                if (led.point(5 - j, dangerY[i])) {
                    game.gameOver()
                }
                
                led.plotBrightness(5 - j, dangerY[i], 140)
                j += 1
            }
        }
        
        if (dangerY[i] >= 5) {
            dangerY.removeAt(i)
            dangerLength.removeAt(i)
            dangerSide.removeAt(i)
            dangerSide.push(Math.randomBoolean())
            dangerY.push(0)
            dangerLength.push(randint(0, 4))
        }
        
        dangerY[i] += 1
        i += 1
    }
})
