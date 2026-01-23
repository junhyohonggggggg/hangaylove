# =====================================#
# 영진 아카데미 - 연애 시뮬 공통 루트     # 
# =====================================#





define h = Character("한결")
define ys = Character("윤서")
define ma = Character("민아")
define sr = Character("서린")
define jh = Character("지혜")
define rn = Character("리나")
define ny = Character("담임 선생님 노윤아")
define ms = Character("민수")
define fr = Character("학생")

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
    
    ny "오늘 전학 온 학생이다. 자기소개해"
    "문이 열리자 시선이 한꺼번에 쏟아진다."
    "나는 숨을 한번 고르고 입을 열었다."
    
    h "한결입니다. 잘 부탁드립니다."

    "학생들의 반응은 제각각이다."
    "고개를 끄덕이는 애, 관심 없는 표정, 이미 졸고 있는 애들."
    "그리고— 그 순간,"
    "교실 한가운데서 나는 어떤 시선과 마주쳤다."
    
    show ys3 at center
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
        "너도 이 학교 다녔었어?":
            $ love['ys'] -= 5 #왜 마이너스5냐면 자기가 영진고인걸 기억도못한 한결에게 화난거임
            ys "…응. 맞아."
            ys "오랜만이다, 우리."
            ys "다시 잘 지내보자."
            "이런 곳에서 아는 사람을 만날 줄이야…"
        "잘 지냈어?":
            $ love['ys'] += 5
            ys "…그럭저럭."
            ys "오랜만이다, 우리."
            hide ys3
            show ys4
            ys "다시 잘 지내보자."
            "이런 곳에서 아는 사람을 만날 줄이야…"
        "히히! 발사!ㅋㅋ":

            show shoot :
                xpos 300 
                ypos -150
            $ shoot_count['ys'] += 1
            $ love['ys'] -= 100
            ys "...?"
            h "아 미안, 참지못하고 사정해버렸어"
            jump crime_end
            #이거 다음에 바로 배드엔딩없냐
    hide ys3
    hide ys4
    #여기서 이제 잡담            
    "윤서와의 대화 이후,"
    "이미 시간이 꽤 흐른 5월쯤이라 그런지 학생들은 전학생에게 큰 관심이 없었다."
    "단 한 사람을 제외하고,"
    #민수등장 ㄱㄱ
    show ms2 :
        zoom 0.8
        center
    $love['ms'] = 80
    ms "안녕, 전학생. 반갑다! 나는 박민수라고 해."

    "이 녀석은 뭘까. 잘 알지도 못하는 나에게 이정도의 관심이라니."
    h "안녕?"

    ms "넌 어디서 왔어?"
    hide ms2
    "잠시 후…"

    "이 녀석은 생각보다 좋은 녀석이었다."
    "친해져도 되겠어."

    "그때, 윤서가 나타나 말을 걸어왔다."
    show ys3
    ys "한결! 우리 다음시간 체육시간이야!"

    "체욱관으로 가야겠어…"
    




    jump palestra

label palestra:
    scene black
    show ms2 :
        zoom 0.8
        center
    ms "ㅎㅇ?"
    #scene palestra #여기 체육관 사진
    #민수랑 토크

    #체육복 윤서 사진
    hide ms2
    jump vending_machine

label vending_machine:
    #scene vending_machine #자판기 배경
    #대충 더워서 자판기 간다는 한결의 혼잣말
    $love['ma']=25 #100 -> 25 하려는 상황이 안 보인다.
    ma "선배 혹시 몇반이에요? 인스타아이디 교환할래요?"
    menu:
        "교환한다.":
            ma "ㄳ"
            $ love['ma'] +=5
            $ love['ys'] -=5   #이거 윤서가 스토커마냥 근처에서 지켜보는거?
            "무언가 익숙한 시선이 느껴졌다."

        "안 한다.":
            ma "ㄲㅂ"
            $ love['ys'] +=5
    jump day2