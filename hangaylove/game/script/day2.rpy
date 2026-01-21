$dongari=0
label day2:
    #scene school #여기도 대충 알아서 배경
    "입학식으로 부터 며칠이 흐른 후"
    ms "동아리 골라 어쩌구 저쩌구"
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
    ms "으흐흐... 일루와잇!"
    jump ms_ending

label dongari2:
    ys "과거 회상 어쩌구 저쩌구"
    $love['ys'] +=10
    jump day3

label dongari3:
    ma "반한 이유 어쩌구"
    $love['ma'] +=10
    jump day3

label dongari4:
    $love['sr'] = 10
    sr "조용한 대화"
    $love['sr'] += 10
    jump day3

label dongari5:
    $love['jh'] = 10
    jh "어쩌구 리나 잡아라"
    $love['jh'] += 5
    rn "어쩌구 저쩌구"
    $love['rn'] += 5
    jump day3
