# =====================================
# 영진 아카데미 - 연애 시뮬 공통 루트
# =====================================

define h = Character("한결")
define ys = Character("윤서")
define ma = Character("민아")
define sr = Character("서린")
define jh = Character("지혜")
define rn = Character("리나")
define ny = Character("노윤아")
define ms = Character("민수")

default affection_yoonseo = 0
default affection_mina = 0
default affection_seorin = 0
default trust_jihye = 0
default affection_rina = 0
default male_flag = 0

label start:

    scene black
    with dissolve

    h "스무 살."
    h "다시 시작하기엔 애매한 나이다."

    h "영진 아카데미."
    h "고등학교도, 대학도 아닌 곳."
    h "하지만 여긴, 다시 시작하려는 사람들만 모여 있다."

    jump day1


# -------------------------
label day1:
# 소꿉친구 윤서
# -------------------------

    scene black
    "강의실."

    ys "……설마, 한결?"

    h "윤서… 맞지?"

    ys "와, 진짜 몇 년 만이야."
    ys "여기로 올 줄은 몰랐네."

    menu:
        "너도 여기 다녀?":
            affection_yoonseo += 1
            ys "응. 나도 다시 준비 중이야."
        "잘 지냈어?":
            affection_yoonseo += 2
            ys "…그럭저럭."

    ys "사람은 변하더라."
    ys "너도, 나도."

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
            affection_mina += 2
            ma "헤헤. 역시 느낌이 좋았어."
        "왜 나 알아?":
            affection_mina += 1
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
            affection_seorin += 2
            sr "……이쪽이에요."
        "그냥 둘러보려고요.":
            affection_seorin += 1
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
            trust_jihye += 2
            jh "협조해줘서 고마워."
        "생각보다 딱딱하네요.":
            trust_jihye -= 1
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
            affection_rina -= 1
            rn "하, 역시 재미없네."
        "처음 뵙겠습니다.":
            affection_rina += 1
            rn "오? 예의는 있네."

    rn "보통은 다 피하거든."
    jump day6


# -------------------------
label day6:
# 노윤아
# -------------------------

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

    menu:
        "아무도 선택 안 했어.":
            male_flag += 2
            ms "그럼 아직 기회 있는 거네."
        "글쎄.":
            male_flag += 1
            ms "애매한 게 제일 위험한데."

    jump route_check


# -------------------------
label route_check:
# 루트 판정
# -------------------------

    if affection_mina >= 3:
        jump mina_route
    elif affection_yoonseo >= 3:
        jump yoonseo_route
    elif affection_seorin >= 3:
        jump seorin_route
    elif trust_jihye >= 2:
        jump jihye_route
    elif affection_rina >= 2:
        jump rina_route
    elif male_flag >= 3:
        jump male_route
    else:
        jump solo_end


# -------------------------
label mina_route:
    scene black
    ma "선배, 저 사실 처음부터 좋아했어요."
    "💖 민아 루트 진입"
    return

label yoonseo_route:
    scene black
    ys "다시 만난 건… 우연 아니라고 생각해."
    "💖 윤서 루트 진입"
    return

label seorin_route:
    scene black
    sr "말 안 해도… 알아줬으면 좋겠어요."
    "💖 서린 루트 진입"
    return

label jihye_route:
    scene black
    jh "나도… 감정 가져도 될까?"
    "💖 지혜 루트 진입"
    return

label rina_route:
    scene black
    rn "끝까지 온 거야?"
    "💖 리나 루트 진입"
    return

label male_route:
    scene black
    ms "그럼 이제 나 차례지?"
    "🧑‍🤝‍🧑 히든 엔딩"
    return

label solo_end:
    scene black
    "아무도 선택하지 못했다."
    "💔 솔로 엔딩"
    return
