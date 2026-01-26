init python:
    import ctypes
    def wnrdj():
        ctypes.windll.user32.MessageBoxW(0, "죽어 쓰레기", "죽어", 0)

init :
    $answer=""
    screen input():
        frame:
            xalign 0.5
            yalign 0.5
            padding (30, 30)

            vbox:
                spacing 10

                text "입력"
                input:
                    value VariableInputValue("answer")
                    length 3
                    allow "0123456789"

                textbutton "확인" action Return()




label crime_end:
    scene black
    "경찰서에 잡혀갔다..."
    "💔 감옥 엔딩"
    call screen input
    python:
        if answer=="123":
            renpy.say(None, "정답")
        else:
            renpy.say(None, "오답")
    

    return
