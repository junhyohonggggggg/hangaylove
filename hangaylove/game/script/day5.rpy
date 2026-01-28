init:
    transform quiz_zoom_center:
        zoom 3
        xalign 0.5
        yalign 0.5


label day5:
    scene black
    $ import random
    "2주 후"
    #여기서 스터디데이트, 퀴즈 이벤트 ㅇㅇ
    $score=0
    $ r = random.randint(1, 5) #1번부터 5번까지중 랜덤으로 한 문제 뽑기
    python:
        if r==1:
            renpy.show("quiz1", at_list=[quiz_zoom_center])
            renpy.say(None, "정답을 고르시오")
            renpy.call_screen("input")
            if answer=="3":
                renpy.say(None, "정답")
                score+=3
                grade+=1
            else :
                renpy.say(None, "오답")

            renpy.hide("quiz1")
        elif r==2:
            renpy.show("quiz2", at_list=[quiz_zoom_center])
            renpy.say(None, "정답을 고르시오")
            renpy.call_screen("input")
            if answer=="2":
                renpy.say(None, "정답")
                score+=3
                grade+=1
            else :
                renpy.say(None, "오답")
                
            renpy.hide("quiz2")
        elif r==3:
            renpy.show("quiz3", at_list=[quiz_zoom_center])
            renpy.say(None, "정답을 고르시오")
            renpy.call_screen("input")
            if answer=="5":
                renpy.say(None, "정답")
                score+=4
                grade+=1
            else :
                renpy.say(None, "오답")
                
            renpy.hide("quiz3")
        elif r==4:
            renpy.show("quiz4", at_list=[quiz_zoom_center])
            renpy.say(None, "정답을 입력하시오")
            renpy.call_screen("input")
            if answer=="16":
                renpy.say(None, "정답")
                score+=3
                grade+=1
            else :
                renpy.say(None, "오답")
                
            renpy.hide("quiz4")
        elif r==5:
            renpy.show("quiz5", at_list=[quiz_zoom_center])
            renpy.say(None, "정답을 입력하시오")
            renpy.call_screen("input")
            if answer=="65":
                renpy.say(None, "정답")
                score+=4
                grade+=1
            else :
                renpy.say(None, "오답")
                
            renpy.hide("quiz5")

    "일단 여기까지"