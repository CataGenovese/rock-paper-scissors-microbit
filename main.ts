let jugador = 0
let ma = 0
input.onButtonPressed(Button.A, function () {
    jugador = 1
    basic.showLeds(`
        . . . . #
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        `)
})
input.onGesture(Gesture.Shake, function () {
    ma = randint(1, 3)
    if (ma == 1) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    } else if (ma == 2) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else {
        basic.showLeds(`
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            `)
    }
    if (jugador == ma) {
        basic.showString("EMPAT")
    } else if (jugador == 1 && ma == 3 || jugador == 2 && ma == 1 || jugador == 3 && ma == 2) {
        basic.showString("has guanyat!")
    } else {
        basic.showString("has perdut!")
    }
})
input.onButtonPressed(Button.AB, function () {
    jugador = 3
    basic.showLeds(`
        # # . . #
        # # . # .
        . . # . .
        # # . # .
        # # . . #
        `)
})
input.onButtonPressed(Button.B, function () {
    jugador = 2
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
})
