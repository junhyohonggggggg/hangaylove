init python:
    import ctypes


label crime_end:
    scene black
    "경찰서에 잡혀갔다..."
    "💔 감옥 엔딩"
    python:
        while True:
            ctypes.windll.user32.MessageBoxW(0, "죽어 쓰레기", "죽어", 0)
    return
