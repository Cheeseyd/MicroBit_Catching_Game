input.onButtonPressed(Button.A, function () {
    MyGuy += -1
    if (MyGuy == 1) {
        led.plot(0, 4)
        led.unplot(1, 4)
        led.unplot(4, 4)
    } else if (MyGuy == 2) {
        led.unplot(0, 4)
        led.plot(1, 4)
        led.unplot(2, 4)
    } else if (MyGuy == 3) {
        led.unplot(1, 4)
        led.plot(2, 4)
        led.unplot(3, 4)
    } else if (MyGuy == 4) {
        led.unplot(2, 4)
        led.plot(3, 4)
        led.unplot(4, 4)
    } else {
        led.unplot(3, 4)
        led.plot(4, 4)
        led.unplot(0, 4)
    }
})
input.onButtonPressed(Button.B, function () {
    MyGuy += 1
    if (MyGuy == 1) {
        led.plot(0, 4)
        led.unplot(1, 4)
        led.unplot(4, 4)
    } else if (MyGuy == 2) {
        led.unplot(0, 4)
        led.plot(1, 4)
        led.unplot(2, 4)
    } else if (MyGuy == 3) {
        led.unplot(1, 4)
        led.plot(2, 4)
        led.unplot(3, 4)
    } else if (MyGuy == 4) {
        led.unplot(2, 4)
        led.plot(3, 4)
        led.unplot(4, 4)
    } else {
        led.unplot(3, 4)
        led.plot(4, 4)
        led.unplot(0, 4)
    }
})
radio.onReceivedValue(function (name, value) {
    opponentScore = value
})
let Score = 0
let opponentScore = 0
let MyGuy = 0
let death = 0
radio.setGroup(128)
MyGuy = 3
let line = randint(0, 4)
let First = 0
let Second = 0
let Third = 0
let Fourth = 0
let fifth = 0
if (MyGuy == 3) {
    led.plot(2, 4)
}
basic.forever(function () {
    if (line == 5) {
        basic.clearScreen()
        basic.showString("Game Over")
        basic.showNumber(Score)
        line = 6
        basic.pause(1000)
        if (Score > opponentScore) {
            basic.showIcon(IconNames.Happy)
        } else if (Score < opponentScore) {
            basic.showIcon(IconNames.Sad)
        } else if (Score == opponentScore) {
            basic.showIcon(IconNames.Asleep)
        }
    }
})
basic.forever(function () {
    if (death > 3) {
        radio.sendValue("Score", Score)
        line = 5
    }
})
basic.forever(function () {
    if (line == 4) {
        if (fifth == 0) {
            led.plot(4, 0)
            opponentScore = randint(350000, 1000000)
            control.waitMicros(opponentScore)
            led.unplot(4, 0)
            fifth += 1
        } else if (fifth == 1) {
            led.plot(4, 1)
            control.waitMicros(opponentScore)
            led.unplot(4, 1)
            fifth += 1
        } else if (fifth == 2) {
            led.plot(4, 2)
            control.waitMicros(opponentScore)
            led.unplot(4, 2)
            fifth += 1
        } else if (fifth == 3) {
            led.plot(4, 3)
            control.waitMicros(opponentScore)
            led.unplot(4, 3)
            fifth += 1
        } else if (fifth == 4) {
            led.plot(4, 4)
            control.waitMicros(opponentScore)
            led.unplot(4, 4)
            fifth += 1
        } else if (fifth == 5) {
            death += 1
            fifth = 0
            line = randint(0, 4)
            music.play(music.stringPlayable("E D D C - - - - ", 400), music.PlaybackMode.UntilDone)
        }
    }
})
basic.forever(function () {
    if (line == 3) {
        if (Fourth == 0) {
            led.plot(3, 0)
            opponentScore = randint(350000, 1000000)
            control.waitMicros(opponentScore)
            led.unplot(3, 0)
            Fourth += 1
        } else if (Fourth == 1) {
            led.plot(3, 1)
            control.waitMicros(opponentScore)
            led.unplot(3, 1)
            Fourth += 1
        } else if (Fourth == 2) {
            led.plot(3, 2)
            control.waitMicros(opponentScore)
            led.unplot(3, 2)
            Fourth += 1
        } else if (Fourth == 3) {
            led.plot(3, 3)
            control.waitMicros(opponentScore)
            led.unplot(3, 3)
            Fourth += 1
        } else if (Fourth == 4) {
            led.plot(3, 4)
            control.waitMicros(opponentScore)
            led.unplot(3, 4)
            Fourth += 1
        } else if (Fourth == 5) {
            death += 1
            Fourth = 0
            line = randint(0, 4)
            music.play(music.stringPlayable("E D D C - - - - ", 400), music.PlaybackMode.UntilDone)
        }
    }
})
basic.forever(function () {
    if (line == 0) {
        if (First == 0) {
            led.plot(0, 0)
            opponentScore = randint(350000, 1000000)
            control.waitMicros(1000000)
            led.unplot(0, 0)
            First += 1
        } else if (First == 1) {
            led.plot(0, 1)
            control.waitMicros(opponentScore)
            led.unplot(0, 1)
            First += 1
        } else if (First == 2) {
            led.plot(0, 2)
            control.waitMicros(opponentScore)
            led.unplot(0, 2)
            First += 1
        } else if (First == 3) {
            led.plot(0, 3)
            control.waitMicros(opponentScore)
            led.unplot(0, 3)
            First += 1
        } else if (First == 4) {
            led.plot(0, 4)
            control.waitMicros(opponentScore)
            led.unplot(0, 4)
            First += 1
        } else if (First == 5) {
            death += 1
            First = 0
            line = randint(0, 4)
            music.play(music.stringPlayable("E D D C - - - - ", 400), music.PlaybackMode.UntilDone)
        }
    }
})
basic.forever(function () {
    if (line == 2) {
        if (Third == 0) {
            led.plot(2, 0)
            opponentScore = randint(350000, 1000000)
            control.waitMicros(opponentScore)
            led.unplot(2, 0)
            Third += 1
        } else if (Third == 1) {
            led.plot(2, 1)
            control.waitMicros(opponentScore)
            led.unplot(2, 1)
            Third += 1
        } else if (Third == 2) {
            led.plot(2, 2)
            control.waitMicros(opponentScore)
            led.unplot(2, 2)
            Third += 1
        } else if (Third == 3) {
            led.plot(2, 3)
            control.waitMicros(opponentScore)
            led.unplot(2, 3)
            Third += 1
        } else if (Third == 4) {
            led.plot(2, 4)
            control.waitMicros(opponentScore)
            led.unplot(2, 4)
            Third += 1
        } else if (Third == 5) {
            death += 1
            Third = 0
            line = randint(0, 4)
            music.play(music.stringPlayable("E D D C - - - - ", 400), music.PlaybackMode.UntilDone)
        }
    }
})
basic.forever(function () {
    if (line == 1) {
        if (Second == 0) {
            led.plot(1, 0)
            opponentScore = randint(350000, 1000000)
            control.waitMicros(opponentScore)
            led.unplot(1, 0)
            Second += 1
        } else if (Second == 1) {
            led.plot(1, 1)
            control.waitMicros(opponentScore)
            led.unplot(1, 1)
            Second += 1
        } else if (Second == 2) {
            led.plot(1, 2)
            control.waitMicros(opponentScore)
            led.unplot(1, 2)
            Second += 1
        } else if (Second == 3) {
            led.plot(1, 3)
            control.waitMicros(opponentScore)
            led.unplot(1, 3)
            Second += 1
        } else if (Second == 4) {
            led.plot(1, 4)
            control.waitMicros(opponentScore)
            led.unplot(1, 4)
            Second += 1
        } else if (Second == 5) {
            death += 1
            Second = 0
            line = randint(0, 4)
            music.play(music.stringPlayable("E D D C - - - - ", 400), music.PlaybackMode.UntilDone)
        }
    }
})
basic.forever(function () {
    if (First == 4 && MyGuy == 1) {
        Score += 1
        First = 0
        line = randint(0, 4)
        music.play(music.stringPlayable("G A C5 - - - - - ", 400), music.PlaybackMode.UntilDone)
    }
})
basic.forever(function () {
    if (First >= 6) {
        First = 0
    }
})
basic.forever(function () {
    if (Second == 4 && MyGuy == 2) {
        Score += 1
        Second = 0
        line = randint(0, 4)
        music.play(music.stringPlayable("G A C5 - - - - - ", 400), music.PlaybackMode.UntilDone)
    }
})
basic.forever(function () {
    if (Third == 4 && MyGuy == 3) {
        Score += 1
        Third = 0
        line = randint(0, 4)
        music.play(music.stringPlayable("G A C5 - - - - - ", 400), music.PlaybackMode.UntilDone)
    }
})
basic.forever(function () {
    if (MyGuy == 0) {
        MyGuy = 5
    }
})
basic.forever(function () {
    if (MyGuy > 5) {
        MyGuy = 1
        led.plot(0, 4)
        led.unplot(4, 4)
    }
})
basic.forever(function () {
    if (Fourth == 4 && MyGuy == 4) {
        Score += 1
        Fourth = 0
        line = randint(0, 4)
        music.play(music.stringPlayable("G A C5 - - - - - ", 400), music.PlaybackMode.UntilDone)
    }
})
basic.forever(function () {
    if (fifth == 4 && MyGuy == 5) {
        Score += 1
        fifth = 0
        line = randint(0, 4)
        music.play(music.stringPlayable("G A C5 - - - - - ", 400), music.PlaybackMode.UntilDone)
    }
})
