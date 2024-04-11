def on_received_value(name, value):
    global opponentScore
    opponentScore = value
radio.on_received_value(on_received_value)

def on_button_pressed_a():
    global MyGuy
    MyGuy += -1
    if MyGuy == 1:
        led.plot(0, 4)
        led.unplot(1, 4)
        led.unplot(4, 4)
    elif MyGuy == 2:
        led.unplot(0, 4)
        led.plot(1, 4)
        led.unplot(2, 4)
    elif MyGuy == 3:
        led.unplot(1, 4)
        led.plot(2, 4)
        led.unplot(3, 4)
    elif MyGuy == 4:
        led.unplot(2, 4)
        led.plot(3, 4)
        led.unplot(4, 4)
    else:
        led.unplot(3, 4)
        led.plot(4, 4)
        led.unplot(0, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global MyGuy
    MyGuy += 1
    if MyGuy == 1:
        led.plot(0, 4)
        led.unplot(1, 4)
        led.unplot(4, 4)
    elif MyGuy == 2:
        led.unplot(0, 4)
        led.plot(1, 4)
        led.unplot(2, 4)
    elif MyGuy == 3:
        led.unplot(1, 4)
        led.plot(2, 4)
        led.unplot(3, 4)
    elif MyGuy == 4:
        led.unplot(2, 4)
        led.plot(3, 4)
        led.unplot(4, 4)
    else:
        led.unplot(3, 4)
        led.plot(4, 4)
        led.unplot(0, 4)
input.on_button_pressed(Button.B, on_button_pressed_b)

Score = 0
opponentScore = 0
MyGuy = 0
death = 0
radio.set_group(128)
MyGuy = 3
line = randint(0, 4)
First = 0
Second = 0
Third = 0
Fourth = 0
fifth = 0
if MyGuy == 3:
    led.plot(2, 4)

def on_forever():
    global opponentScore, First, death, line
    if line == 0:
        if First == 0:
            led.plot(0, 0)
            opponentScore = randint(350000, 1000000)
            control.wait_micros(1000000)
            led.unplot(0, 0)
            First += 1
        elif First == 1:
            led.plot(0, 1)
            control.wait_micros(opponentScore)
            led.unplot(0, 1)
            First += 1
        elif First == 2:
            led.plot(0, 2)
            control.wait_micros(opponentScore)
            led.unplot(0, 2)
            First += 1
        elif First == 3:
            led.plot(0, 3)
            control.wait_micros(opponentScore)
            led.unplot(0, 3)
            First += 1
        elif First == 4:
            led.plot(0, 4)
            control.wait_micros(opponentScore)
            led.unplot(0, 4)
            First += 1
        elif First == 5:
            death += 1
            First = 0
            line = randint(0, 4)
            music.play(music.string_playable("E D D C - - - - ", 400),
                music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)

def on_forever2():
    global First
    if First >= 6:
        First = 0
basic.forever(on_forever2)

def on_forever3():
    global MyGuy
    if MyGuy == 0:
        MyGuy = 5
basic.forever(on_forever3)

def on_forever4():
    global Score, Second, line
    if Second == 4 and MyGuy == 2:
        Score += 1
        Second = 0
        line = randint(0, 4)
        music.play(music.string_playable("G A C5 - - - - - ", 400),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever4)

def on_forever5():
    global opponentScore, Second, death, line
    if line == 1:
        if Second == 0:
            led.plot(1, 0)
            opponentScore = randint(350000, 1000000)
            control.wait_micros(opponentScore)
            led.unplot(1, 0)
            Second += 1
        elif Second == 1:
            led.plot(1, 1)
            control.wait_micros(opponentScore)
            led.unplot(1, 1)
            Second += 1
        elif Second == 2:
            led.plot(1, 2)
            control.wait_micros(opponentScore)
            led.unplot(1, 2)
            Second += 1
        elif Second == 3:
            led.plot(1, 3)
            control.wait_micros(opponentScore)
            led.unplot(1, 3)
            Second += 1
        elif Second == 4:
            led.plot(1, 4)
            control.wait_micros(opponentScore)
            led.unplot(1, 4)
            Second += 1
        elif Second == 5:
            death += 1
            Second = 0
            line = randint(0, 4)
            music.play(music.string_playable("E D D C - - - - ", 400),
                music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever5)

def on_forever6():
    global Score, fifth, line
    if fifth == 4 and MyGuy == 5:
        Score += 1
        fifth = 0
        line = randint(0, 4)
        music.play(music.string_playable("G A C5 - - - - - ", 400),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever6)

def on_forever7():
    global MyGuy
    if MyGuy > 5:
        MyGuy = 1
        led.plot(0, 4)
        led.unplot(4, 4)
basic.forever(on_forever7)

def on_forever8():
    global opponentScore, fifth, death, line
    if line == 4:
        if fifth == 0:
            led.plot(4, 0)
            opponentScore = randint(350000, 1000000)
            control.wait_micros(opponentScore)
            led.unplot(4, 0)
            fifth += 1
        elif fifth == 1:
            led.plot(4, 1)
            control.wait_micros(opponentScore)
            led.unplot(4, 1)
            fifth += 1
        elif fifth == 2:
            led.plot(4, 2)
            control.wait_micros(opponentScore)
            led.unplot(4, 2)
            fifth += 1
        elif fifth == 3:
            led.plot(4, 3)
            control.wait_micros(opponentScore)
            led.unplot(4, 3)
            fifth += 1
        elif fifth == 4:
            led.plot(4, 4)
            control.wait_micros(opponentScore)
            led.unplot(4, 4)
            fifth += 1
        elif fifth == 5:
            death += 1
            fifth = 0
            line = randint(0, 4)
            music.play(music.string_playable("E D D C - - - - ", 400),
                music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever8)

def on_forever9():
    global Score, Third, line
    if Third == 4 and MyGuy == 3:
        Score += 1
        Third = 0
        line = randint(0, 4)
        music.play(music.string_playable("G A C5 - - - - - ", 400),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever9)

def on_forever10():
    global line
    if line == 5:
        basic.clear_screen()
        basic.show_string("Game Over")
        basic.show_number(Score)
        line = 6
        basic.pause(1000)
        if Score > opponentScore:
            basic.show_icon(IconNames.HAPPY)
        elif Score < opponentScore:
            basic.show_icon(IconNames.SAD)
        elif Score == opponentScore:
            basic.show_icon(IconNames.ASLEEP)
basic.forever(on_forever10)

def on_forever11():
    global line
    if death > 3:
        radio.send_value("Score", Score)
        line = 5
basic.forever(on_forever11)

def on_forever12():
    global opponentScore, Fourth, death, line
    if line == 3:
        if Fourth == 0:
            led.plot(3, 0)
            opponentScore = randint(350000, 1000000)
            control.wait_micros(opponentScore)
            led.unplot(3, 0)
            Fourth += 1
        elif Fourth == 1:
            led.plot(3, 1)
            control.wait_micros(opponentScore)
            led.unplot(3, 1)
            Fourth += 1
        elif Fourth == 2:
            led.plot(3, 2)
            control.wait_micros(opponentScore)
            led.unplot(3, 2)
            Fourth += 1
        elif Fourth == 3:
            led.plot(3, 3)
            control.wait_micros(opponentScore)
            led.unplot(3, 3)
            Fourth += 1
        elif Fourth == 4:
            led.plot(3, 4)
            control.wait_micros(opponentScore)
            led.unplot(3, 4)
            Fourth += 1
        elif Fourth == 5:
            death += 1
            Fourth = 0
            line = randint(0, 4)
            music.play(music.string_playable("E D D C - - - - ", 400),
                music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever12)

def on_forever13():
    global Score, Fourth, line
    if Fourth == 4 and MyGuy == 4:
        Score += 1
        Fourth = 0
        line = randint(0, 4)
        music.play(music.string_playable("G A C5 - - - - - ", 400),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever13)

def on_forever14():
    global opponentScore, Third, death, line
    if line == 2:
        if Third == 0:
            led.plot(2, 0)
            opponentScore = randint(350000, 1000000)
            control.wait_micros(opponentScore)
            led.unplot(2, 0)
            Third += 1
        elif Third == 1:
            led.plot(2, 1)
            control.wait_micros(opponentScore)
            led.unplot(2, 1)
            Third += 1
        elif Third == 2:
            led.plot(2, 2)
            control.wait_micros(opponentScore)
            led.unplot(2, 2)
            Third += 1
        elif Third == 3:
            led.plot(2, 3)
            control.wait_micros(opponentScore)
            led.unplot(2, 3)
            Third += 1
        elif Third == 4:
            led.plot(2, 4)
            control.wait_micros(opponentScore)
            led.unplot(2, 4)
            Third += 1
        elif Third == 5:
            death += 1
            Third = 0
            line = randint(0, 4)
            music.play(music.string_playable("E D D C - - - - ", 400),
                music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever14)

def on_forever15():
    global Score, First, line
    if First == 4 and MyGuy == 1:
        Score += 1
        First = 0
        line = randint(0, 4)
        music.play(music.string_playable("G A C5 - - - - - ", 400),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever15)
