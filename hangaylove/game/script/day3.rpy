$movie=0
label day3:
    "2주일이 지났다."
    ms "학교에 관한 대화"

    ms "영화티켓이 마침 2장이있는데, 어떡할래?"

    "누구랑 영화를 볼까?"
    menu:
        "민수":
            ms "으흐흐... 일루와잇!"
            jump ms_ending
        "윤서":
            if love['ys']>=35 :
                ys "ㄱㄱ"
                $movie="윤서"
                jump cinema
            else:
                ys "ㄴㄴ"
                ms "뭐? 볼 사람이 없어? 일루와잇!"
                jump ms_ending
        "민아":
            if love['ma']>=35 :
                ma "ㄱㄱ"
                $movie="민아"
                jump cinema
            else:
                ma "ㄴㄴ"
                ms "뭐? 볼 사람이 없어? 일루와잇!"
                jump ms_ending
        "서린":
            if love['sr']>=35 :
                sr "ㄱㄱ"
                $movie="서린"
                jump cinema
            else:
                sr "ㄴㄴ"
                ms "뭐? 볼 사람이 없어? 일루와잇!"
                jump ms_ending
        "지혜":
            if love['jh']>=35 :
                jh "ㄱㄱ"
                $movie="지혜"
                jump cinema
            else:
                jh "ㄴㄴ"
                ms "뭐? 볼 사람이 없어? 일루와잇!"
                jump ms_ending
        "리나":
            if love['rn']>=35 :
                rn "ㄱㄱ"
                $movie="리나"
                jump cinema
            else:
                rn "ㄴㄴ"
                ms "뭐? 볼 사람이 없어? 일루와잇!"
                jump ms_ending
