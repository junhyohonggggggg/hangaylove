label cinema:
    #scene cinema #영화관 앞
    if movie=="윤서":
        jump cinema_ys
    if movie=="민아":
        jump cinema_ma
    if movie=="서린":
        jump cinema_sr
    if movie=="지혜":
        jump cinema_jh
    if movie=="리나":
        jump cinema_rn

label cinema_ys:
    #scene cinema_in #영화관 안
    "어떤 영화를 볼까?"
    menu:
        "로맨스":
            $love['ys'] += 10
        "호러":
            $love['ys'] += 10
        "액션":
            $love['ys'] -= 5
        "문학":
            pass
        "정치":
            pass
jump day5

label cinema_ma:
    #scene cinema_in #영화관 안
    "어떤 영화를 볼까?"
    menu:
        "로맨스":
            $love['ma'] += 10
        "호러":
            $love['ma'] -= 5
        "액션":
            $love['ma'] += 10
        "문학":
            pass
        "정치":
            pass
jump day5

label cinema_sr:
    #scene cinema_in #영화관 안
    "어떤 영화를 볼까?"
    menu:
        "로맨스":
            pass
        "호러":
            pass
        "액션":
            pass
        "문학":
            $love['sr'] += 10
        "정치":
            pass
jump day5

label cinema_jh:
    #scene cinema_in #영화관 안
    "어떤 영화를 볼까?"
    menu:
        "로맨스":
            pass
        "호러":
            pass
        "액션":
            pass
        "문학":
            pass
        "정치":
            $love['jh'] += 10
jump day5

label cinema_rn:
    #scene cinema_in #영화관 안
    "어떤 영화를 볼까?"
    menu:
        "로맨스":
            pass            
        "호러":
            pass            
        "액션":
            pass            
        "문학":
            pass
        "정치":
            pass
jump day5