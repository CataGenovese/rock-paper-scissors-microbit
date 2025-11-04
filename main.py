hand = 0

def on_gesture_shake():
    global hand
    hand = randint(1, 3)
    if hand == 1:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
        music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
                4120,
                1266,
                255,
                148,
                500,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.CURVE),
            SoundExpressionPlayMode.UNTIL_DONE)
    elif hand == 2:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
        music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
                4417,
                1,
                0,
                255,
                266,
                SoundExpressionEffect.VIBRATO,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.UNTIL_DONE)
    else:
        basic.show_leds("""
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            """)
        music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
                1177,
                4967,
                0,
                206,
                266,
                SoundExpressionEffect.TREMOLO,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
