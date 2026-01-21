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
    


    $ love['ys'] += 40   #소꿉친구니까 평소 있던 호감도라는 느낌

   
    h "열아홉 살."
    h "인생에서 가장 중요하다고 할 수 있는 시기다."

    h "영진고등학교."
    h "새롭게 전학 온, 시골의 한 고등학교."
    h "하지만 여긴, 공부에만 집중하고 싶은 나를 위한 공간이다."

    jump day1


# -------------------------
label day1:
# 소꿉친구 윤서
# 윤서만나고 선생님 만나고 기타등등
# -------------------------

    scene school2
   
    "교실 문 안에서는 학생들이 떠드는 소리와 선생님이 중재시키는 등 다양한 소리가 들린다."
    "그리고, 나는 문 앞에서 기다리는 중이다."
    
    ny "들어와, 전학생"

    "그 말과 함께, 나는 교실문을 열고 들어갔다."
    scene classroom1
    

    h "안녕, 오늘부터 3학년 8반에서 함께할 한결이라고 해. 얘들아 잘 부탁해."

    "학생들의 반응은 각양각색이다."
    "열심히 경청하는 친구, 앞자리에서 자는 친구, 자기들끼리 떠드는 학생들, 그리고..."
    show ys3 at center
       

    
    ys "……설마, 한결?"
    
    h "넌… 방윤서?"
    "방윤서, 나와 유치원, 초등학교, 중학교를 함께 나온 소꿉친구이다."
    "고등학교가 갈라지면서 더이상 볼일이 없을 줄 알았는데…"
   
    ys "와, 진짜 몇 년 만이야."
    ys "여기로 올 줄은 몰랐네."
    

    menu:
        "너도 영진고 다녔었구나?":
            $ love['ys'] -= 1
            ys "응. 맞아."
            ys "오랜만이다, 우리."
            ys "다시 잘 지내보자."
            "이런 곳에서 아는 사람을 만날 줄이야.."
        "잘 지냈어?":
            $ love['ys'] += 3
            ys "…그럭저럭."
            ys "오랜만이다, 우리."
            ys "다시 잘 지내보자."
            "이런 곳에서 아는 사람을 만날 줄이야.."
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

                
    

    jump day2
  


# -------------------------
label day2:
# 후배 민아
# -------------------------

    scene black
    "점심시간, 자판기 앞."

    ma "저기요. 혹시 한결 선배 맞죠?"

    h "맞는데…?"

    ma "전 민아예요. 신입생이에요."
    ma "어제부터 봤어요."

    menu:
        "반가워.":
            $ love['ma'] += 3
            ma "헤헤. 역시 느낌이 좋았어."
        "왜 나 알아?":
            $ love['ma'] += 1
            ma "눈에 띄었거든요."

    ma "앞으로 자주 봬요."
    jump day3


# -------------------------
label day3:
# 도서관 사서부 서린
# -------------------------

    scene black
    "도서관."

    sr "…무슨 책 찾으세요?"

    menu:
        "추천 좀 해줄래요?":
            $ love['sr'] += 3
            sr "……이쪽이에요."
        "그냥 둘러보려고요.":
            $ love['sr'] += 1
            sr "아… 네."

    "말은 없지만, 시선이 느껴진다."
    jump day4


# -------------------------
label day4:
# 학생회장 지혜
# -------------------------

    scene black
    "복도."

    jh "잠깐 시간 괜찮나?"

    jh "전학생 관련해서 확인할 게 있어."
    jh "여긴 규칙이 중요해."

    menu:
        "알겠습니다.":
            $ love['jh'] += 3
            jh "협조해줘서 고마워."
        "생각보다 딱딱하네요.":
            $ love['jh'] -= 1
            jh "감정은 나중 문제야."

    jump day5


# -------------------------
label day5:
# 일진 갸루 리나
# -------------------------

    scene black
    "계단 뒤."

    rn "쟤가 전학생이야?"

    menu:
        "문제 있어?":
            $ love['rn'] -= 1
            rn "하, 역시 재미없네."
        "처음 뵙겠습니다.":
            $ love['rn'] += 3
            rn "오? 예의는 있네."

    rn "보통은 다 피하거든."
    jump day6


# -------------------------#
label day6:                #
# 노윤아                    #노?
# -------------------------#

    scene black
    "상담실."

    ny "여긴 공부만 하는 곳 아니야."
    ny "인생도 좀 배워."

    ny "다가오는 사람 많을 거다."
    ny "문제는…"

    ny "선택할 용기가 있느냐지."

    jump day7


# -------------------------
label day7:
# 민수 (히든 루트 플래그)
# -------------------------

    scene black
    "수업이 끝나고."

    ms "야, 밥 먹을래?"
    ms "뭐야, 너 표정이 왜 그래?"

    menu:
        "아무도 선택 안 했어.":
            $ love['ms'] += 3
            ms "그럼 아직 기회 있는 거네."
        "글쎄.":
            $ love['ms'] += 2
            ms "애매한 게 제일 위험한데."

    jump route_check


# -------------------------
label route_check:
# 루트 판정
# -------------------------

label route_selection:
    
    menu:
        "누구의 루트로 진행할까요?"

        
        "민아 (Mina)" if love['ma'] >= 3:
            jump mina_route

        "윤서 (Yoonseo)" if love['ys'] >= 3:
            jump yoonseo_route

        "서린 (Seorin)" if love['sr'] >= 3:
            jump seorin_route

        "지혜 (Jihye)" if love['jh'] >= 3:
            jump jihye_route

        "리나 (Rina)" if love['rn'] >= 3:
            jump rina_route

        "노윤아" if love['ny'] >= 3:
            jump ny_route

        "민수 (Minsu)" if love['ms'] >= 3:
            jump male_route

    
    jump solo_end

# -------------------------





























