
label day2:
    scene classroom1
    "영진고로 전학 온 지 사흘 뒤."
    "시간은 나름대로 빠르게 흘렀고,"
    "어느새, 그 날이 되었다."
    show ms3
    ms "야, 한결."
    ms "쌤이 이거 갖다주라더라."
    
    hide ms3
    menu:
        "유도부":
            $dongari="유도부"
            jump dongari1
        "보건부":
            $dongari="보건부"
            jump dongari2
        "만화부":
            $dongari="만화부"
            jump dongari3
        "사서부":
            $dongari="사서부"
            jump dongari4
        "선도부":
            $dongari="선도부"
            jump dongari5
    
#동아리 마다 동아리에 맞는 배경

label dongari1:
    scene palestra
    show ms0
    ms "으흐흐... 일루와잇!"
    

    jump ms_ending

label dongari2:
    show ys1
    ys "과거 회상 어쩌구 저쩌구"
    $love['ys'] +=10
    hide ys1
    jump day3

label dongari3:
    scene library:
        zoom 2.4
    show ma1
    ma "반한 이유 어쩌구"
    $love['ma'] +=10
    hide ma1
    jump day3

label dongari4:
    scene library:
        zoom 2.4
    show sr1
    $love['sr'] = 10
    sr "조용한 대화"
    $love['sr'] += 10
    hide sr1
    jump day3

label dongari5:
    show jh1
    $love['jh'] = 10
    jh "어쩌구 리나 잡아라"
    hide jh1
    $love['jh'] += 5
    show rn1
    rn "어쩌구 저쩌구"
    hide rn1
    $love['rn'] += 5
    jump day3
