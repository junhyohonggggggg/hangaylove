init python:
    import ctypes
    def wnrdj():
        ctypes.windll.user32.MessageBoxW(0, "죽어 쓰레기", "죽어", 0)




label crime_end:
    scene black
    "경찰서에 잡혀갔다..."
    "💔 감옥 엔딩"
    python:
        wnrdj()
    return
