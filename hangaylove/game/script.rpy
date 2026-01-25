# =====================================#
# 영진 아카데미 - 연애 시뮬 공통 루트     # 
# =====================================#





define h = Character("한결")
define ys = Character("윤서")
define ma = Character("민아")
define sr = Character("서린")
define jh = Character("지혜")
define rn = Character("리나")
define ny = Character("담임교사 노윤아")
define ms = Character("민수")
define fr = Character("학생")
define ex1 = Character("체육교사")

default affection_yoonseo = 0      #이것들은 왜 있는겨
default affection_mina = 0
default affection_seorin = 0
default trust_jihye = 0
default affection_rina = 0
default male_flag = 0


default love = {
    "ys": 0,
    "ma": 0,
    "sr": 0,
    "jh": 0,
    "rn": 0,
    "ny": 0,
    "ms": 0
}

default shoot_count = {
    "ys": 0,
    "ma": 0,
    "sr": 0,
    "jh": 0,
    "rn": 0,
    "ny": 0,
    "ms": 0
}


label start:
        
    scene school1  
    
    show screen stat_overlay    
    




    h "5월 12일"
    h "내 나이, 열아홉 살."
    h "인생에서 가장 중요하다고 할 수 있는 시기일까."
    h "영진고등학교,"
    h "새롭게 전학 온, 시골의 한 고등학교."
    h "여긴, 공부에만 집중하고 싶은 나를 위한 공간이다."

    jump day1


# -------------------------
label day1:
# 소꿉친구 윤서
# 윤서만나고 선생님 만나고 기타등등
# -------------------------

    scene school2
   
    "교실 문 안은 학생들이 떠드는 소리로 시끌벅적하다."
    "그리고, 나는 문 앞에서 기다리는 중이었다."
    $love['ny'] = 10
    ny "들어와, 전학생"

    "그 말과 함께, 나는 교실문을 열고 들어갔다."
    scene classroom1
    show ny1
    ny "오늘 전학 온 학생이다. 자기소개해"
    hide ny1
    "문이 열리자 시선이 한꺼번에 쏟아진다."
    "나는 숨을 한번 고르고 입을 열었다."
    
    h "한결입니다. 잘 부탁드립니다."

    "학생들의 반응은 제각각이다."
    "고개를 끄덕이는 애, 관심 없는 표정, 이미 졸고 있는 애들."
    "그리고— 그 순간,"
    "교실 한가운데서 나는 어떤 시선과 마주쳤다."
    
    show ys1 at center
    $ love['ys'] += 40   #여거 나중에 내가보낸스토리라인대로암튼 거시기 ㅇㅋ? 잊지말도록

    ys "……설마, 한결?"
    
    h "넌… 방윤서?"

    "그 목소리 하나로,"
    "머릿속에 오래된 기억들이 터지듯 떠오른다."
    "방윤서, 나와 인큐베이터에서부터 함께한 소꿉친구."
    "고등학교가 갈라지며 작별했었는데……"
   
    ys "와, 진짜 몇 년 만이야?"
    ys "너가 영진고로 올 줄이야."
    

    menu:
        "윤서 너 영진고등학교 다녔었어?":
            $ love['ys'] -= 5 #왜 마이너스5냐면 자기가 영진고인걸 기억도못한 한결에게 화난거임
            ys "…응. 맞아."
            ys "오랜만이다, 우리."
            ys "다시 잘 지내보자."
            "이런 곳에서 아는 사람을 만날 줄이야…"
        "잘 지냈어?":
            $ love['ys'] += 5
            ys "…그럭저럭."
            ys "오랜만이다, 우리."
            hide ys1
            show ys2
            ys "다시 잘 지내보자."
            "이런 곳에서 아는 사람을 만날 줄이야…"
        "히히! 발사!ㅋㅋ":
            show shoot :
                xpos 300 
                ypos -150
            $ shoot_count['ys'] += 1
            $ love['ys'] -= 100
            ys "...?"
            h "아 쌌다 ㅈㅅ"
            jump crime_end
            #이거 다음에 바로 배드엔딩없냐
    hide ys1
    hide ys2
    hide ys1black
    
    #여기서 이제 나레이션할게요          
    
    "소꿉친구과의 짧은 재회 후,"
    
    "윤서는 짧게 웃고는 친구 쪽으로 돌아갔다."
    "그 뒷모습을 잠깐 바라보다가, 나도 시선을 거둔다."

    "말은 몇 마디 안 섞었는데,"
    "마음만은 괜히 더 복잡해졌다."

    "아는 사이라서 편할 줄 알았는데…"
    "오히려 모르는 사람보다 더 조심스러운 것 같다."
    "…"

    "교실 안은 다시 각자의 일상으로 돌아간 분위기다."
    "누군가는 졸고,"
    "누군가는 책을 넘기고,"
    "누군가는 전학 온 나를 힐끗거리다 관심을 거둔다."

    "나는 자리에서 가방을 정리하며 숨을 한 번 고른다."
    
    show ny1
    ny "자, 이제 체육 수업이다. 체육관으로 이동하자."
    show ny1black

    "의자가 밀리는 소리,"
    "가방에서 체육복을 꺼내는 소리,"
    "교실이 한순간에 소란스러워진다."
    hide ny1
    hide ny1black
    "멍 때릴 때가 아니지."
    "체육관으로 이동하자."
    jump palestra

label palestra:
    scene palestra
    
    "체육관 문을 열자, 눅눅한 공기와 함께 공이 바닥에 튀는 소리가 귀에 들어온다."
    "운동화가 마룻바닥을 긁는 소리, 웃음소리, 누군가의 불평."
    
    "전학 첫날에 체육이라니."
    "타이밍이 썩 좋다고는 못 하겠다."
    
    "체육 교사는 호루라기를 불며 출석을 부른다."
    show ex1
    ex1 "오늘은 자유 활동이다. 다치지 않게만 해."
    show ex1black
    "그 한마디에 체육관 분위기가 느슨해진다."
    hide ex1
    hide ex1black
    
    "나는 체육관 한쪽에 서서 주변을 둘러본다."
    "아직 누구와 어떻게 어울려야 할지, 감이 잡히지 않는다."

    "그때—"
    #민수랑 토크
    show ms4
    $love['ms'] = 70
    ms "야, 한결 맞지?"
    show ms4black
    "갑작스러운 목소리에 고개를 돌리자,"
    "체육복 차림의 남학생 하나가 손을 흔들고 있다."
    hide ms4black
    ms "아까 교실에서 봤어. 전학생."
    show ms4black
    h "아, 응. 맞아."
    hide ms4black
    ms "난 민수야. 그냥… 너 할거 없어보이길래."

    "그는 호쾌하게 웃으며 공 하나를 들고 흔든다."

    ms "농구할 건데, 같이 할거지?"
    show ms4black
    "거절할 이유는 없다."
    "적어도 지금은."
    "나는 고개를 끄덕이고 민수 쪽으로 걸어갔다."
    $love['ms'] += 10

    hide ms4
    "공은 생각보다 무겁고, 체육관은 생각보다 넓다."
    "몇 번의 패스, 몇 번의 실수."
    "민수는 실수해도 웃고 넘긴다."
    show ms4
    ms "괜찮아, 괜찮아. 처음이면 그럴 수 있지."
    show ms4black
    "그 말에 이상하게 마음이 조금 풀린다."
    hide ms4
    hide ms4black
    
    #체육복 윤서 사진
    "잠시 숨을 고르다 고개를 들었을 때—"
    show ys3
    "체육관 반대편에서 스트레칭을 하고 있는 윤서가 보인다."
    hide ys3
    show ys3black

    "익숙한 얼굴이다."
    "유치원때부터 내내 봐왔던, 항상 변함없이 웃던 그 얼굴."
    "그런데도, 이상하게 거리감이 느껴진다."

    "같은 공간에 있는데도, 아까 교실에서보다 더 멀어 보인다."
    show ys3
    hide ys3black
    "윤서는 잠깐 내 쪽을 본다."
    "일순간, 우리는 눈이 마주쳤다."

    "하지만—"
    show ys3black
    hide ys3
    "아무 말도 하지 않고, 다시 시선을 돌린다."
    hide ys3black

    "어릴 땐,"
    "같은 체육관에 있으면 꼭 옆에 있었는데."

    "지금은, 같은 공간에 있어도 말을 걸 이유를 찾지 못한다."






    hide ms4
    jump vending_machine

label vending_machine:
    scene vending_machine
    #대충 더워서 자판기 간다는 한결의 혼잣말
    $love['ma']=25 #100 -> 25 하려는 상황이 안 보인다.
    show ma1
    ma "선배 혹시 몇반이에요? 인스타아이디 교환할래요?"
    menu:
        "교환한다.":
            hide ma1
            show ma3
            ma "ㄳ"
            $ love['ma'] +=5
            $ love['ys'] -=5   #이거 윤서가 스토커마냥 근처에서 지켜보는거?
            "무언가 익숙한 시선이 느껴졌다."
            hide ma3

        "안 한다.":
            hide ma1
            show ma2
            ma "ㄲㅂ"
            $ love['ys'] +=5
            hide ma2
    jump day2