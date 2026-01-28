
label day2:
    scene black
    with dissolve

    "전학 온 지 며칠이 지났다."
    "시간은 생각보다 빠르게 흘렀고,"
    "나는 어느새 이 학교의 풍경에 조금씩 익숙해지고 있었다."

    scene school_morning
    with fade

    "아침 등굣길."
    "낯설기만 하던 교문도, 이제는 그리 어색하지 않다."

    h "(벌써 적응한 건가…)"
    h "(아니면, 그냥 생각할 틈이 없었던 걸까.)"

    # --------------------------------------------------
    # 민수 등장 (이미 베프 상태)
    # --------------------------------------------------

    show ms3 at left
    with dissolve

    ms "야, 한결!"
    ms "오늘은 늦지 않았네?"

    h "맨날 늦는 사람 취급하지 마."

    ms "아니 근데 진짜 웃긴 게 뭔지 아냐?"
    ms "너 전학생인데, 반에서 존재감이 너무 자연스러워."

    h "그게 좋은 건지 나쁜 건지 모르겠는데."

    ms "좋은 거지."
    ms "최소한 외톨이는 아니라는 거니까."

    "민수는 아무렇지 않게 말하지만,"
    "그 말이 묘하게 마음에 남는다."

    h "(확실히… 민수 덕을 좀 봤지.)"

    ms "아 맞다."
    ms "너 아직 동아리 안 정했지?"

    h "동아리?"

    ms "응."
    ms "원래는 다 1학년 때 정하는데,"
    ms "전학생은 예외거든."

    "그제서야 떠오른다."
    "며칠 전 담임이 했던 말."

    show ny1 at right
    with dissolve

    ny "한결."
    ny "동아리는 아직이랬지?"

    ny "이번 주 안으로 하나는 정해."
    ny "혼자 남는 건 좋지 않거든."

    hide ny1
    with dissolve

    h "(다들 이미 자리 잡은 상태에서…)"
    h "(나 혼자 선택하는 느낌이네.)"

    ms "선도부는 어때?"
    ms "아, 아니면 사서부도 괜찮고."

    ms "만화부는 좀 시끄럽고,"
    ms "보건부는… 음, 관심 많으면 추천."

    "민수는 가볍게 말하지만,"
    "그 선택이 단순하지 않다는 걸"
    "나는 왠지 알고 있었다."

    h "(어디를 고르느냐에 따라…)"
    h "(앞으로 보는 얼굴도 달라질지도.)"

    "복도 끝에,"
    "각 동아리 게시판이 보인다."

    "아직은,"
    "결정하지 않았다."

    "하지만—"
    "곧 선택해야 한다."

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
