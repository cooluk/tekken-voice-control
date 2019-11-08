import speech_recognition as sr 
import pyvjoy
import time

def electric() :
    j = pyvjoy.VJoyDevice(1)

    wAxisX = 0x4000
    wAxisY = 0x4000

    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX

    j.update()


    # ELECTRIC

    time.sleep(0.20)
    wAxisX = 0x8000 #6
    j.data.wAxisX = wAxisX
    j.update()
    time.sleep(0.15)

    wAxisX = 0x4000
    wAxisY = 0x4000 #N
    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX
    j.update()
    time.sleep(0.05)

    wAxisY = 0x8000 #2
    j.data.wAxisY = wAxisY
    j.update()
    time.sleep(0.020)

    wAxisX = 0x8000 #23
    j.data.wAxisX = wAxisX
    j.update()
    j.set_button(4,1)
    time.sleep(0.05)

    wAxisX = 0x4000
    wAxisY = 0x4000 #N
    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX
    j.update()
     
def narak() :
    j = pyvjoy.VJoyDevice(1)

    wAxisX = 0x4000
    wAxisY = 0x4000

    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX

    j.update()


    # ELECTRIC

    time.sleep(0.20)
    wAxisX = 0x8000 #6
    j.data.wAxisX = wAxisX
    j.update()
    time.sleep(0.15)

    wAxisX = 0x4000
    wAxisY = 0x4000 #N
    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX
    j.update()
    time.sleep(0.05)

    wAxisY = 0x8000 #2
    j.data.wAxisY = wAxisY
    j.update()
    time.sleep(0.020)

    wAxisX = 0x8000 #23
    j.data.wAxisX = wAxisX
    j.update()
    j.set_button(3,1)
    time.sleep(0.05)

    wAxisX = 0x4000
    wAxisY = 0x4000 #N
    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX
    j.update()

def soccerkick() :
    j = pyvjoy.VJoyDevice(1)

    wAxisX = 0x4000
    wAxisY = 0x4000

    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX

    j.update()

    time.sleep(0.20)
    wAxisX = 0x1 #4
    j.data.wAxisX = wAxisX
    j.update()
    time.sleep(0.15)

    j.set_button(3,1)
    time.sleep(0.05)

    wAxisX = 0x4000
    wAxisY = 0x4000 #N
    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX
    j.update()

def mashin() :
    j = pyvjoy.VJoyDevice(1)

    wAxisX = 0x4000
    wAxisY = 0x4000

    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX

    j.update()


    time.sleep(0.20)
    wAxisX = 0x8000 #6
    j.data.wAxisX = wAxisX
    j.update()
    time.sleep(0.15)

    wAxisX = 0x4000
    wAxisY = 0x4000 #N
    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX
    j.update()
    time.sleep(0.05)

    wAxisY = 0x8000 #2
    j.data.wAxisY = wAxisY
    j.update()
    time.sleep(0.020)

    wAxisX = 0x8000 #23
    j.data.wAxisX = wAxisX
    j.update()
    
    time.sleep(0.05)

    wAxisX = 0x4000
    wAxisY = 0x4000 #N
    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX
    j.update()

    time.sleep(0.3)
    j.set_button(4,1)
    time.sleep(0.03)

    wAxisX = 0x4000
    wAxisY = 0x4000 #N
    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX
    
    j.update()

    time.sleep(0.05)

def getup() :
    j = pyvjoy.VJoyDevice(1)

    wAxisX = 0x4000
    wAxisY = 0x4000

    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX

    j.update()

    j.set_button(4,1)

    # ELECTRIC



def wave() :
    j = pyvjoy.VJoyDevice(1)

    wAxisX = 0x4000
    wAxisY = 0x4000

    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX

    j.update()


    # ELECTRIC

    time.sleep(0.20)
    wAxisX = 0x8000 #6
    j.data.wAxisX = wAxisX
    j.update()
    time.sleep(0.15)

    wAxisX = 0x4000
    wAxisY = 0x4000 #N
    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX
    j.update()
    time.sleep(0.05)

    wAxisY = 0x8000 #2
    j.data.wAxisY = wAxisY
    j.update()
    time.sleep(0.020)

    wAxisX = 0x8000 #23
    j.data.wAxisX = wAxisX
    j.update()
    time.sleep(0.05)

    wAxisX = 0x4000
    wAxisY = 0x4000 #N
    j.data.wAxisY = wAxisY
    j.data.wAxisX = wAxisX
    j.update()

kor_begin = 44032
kor_end = 55203
chosung_base = 588
jungsung_base = 28
jaum_begin = 12593
jaum_end = 12622
moum_begin = 12623
moum_end = 12643

chosung_list = [ 'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 
        'ㅅ', 'ㅆ', 'ㅇ' , 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

jungsung_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 
        'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 
        'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 
        'ㅡ', 'ㅢ', 'ㅣ']

jongsung_list = [
    ' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ',
        'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 
        'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 
        'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

jaum_list = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄸ', 'ㄹ', 
              'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 
              'ㅃ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

moum_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 
              'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

def compose(chosung, jungsung, jongsung):
    char = chr(
        kor_begin +
        chosung_base * chosung_list.index(chosung) +
        jungsung_base * jungsung_list.index(jungsung) +
        jongsung_list.index(jongsung)
    )
    return char

def decompose(c):
    if not character_is_korean(c):
        return None
    i = ord(c)
    if (jaum_begin <= i <= jaum_end):
        return (c, ' ', ' ')
    if (moum_begin <= i <= moum_end):
        return (' ', c, ' ')

    # decomposition rule
    i -= kor_begin
    cho  = i // chosung_base
    jung = ( i - cho * chosung_base ) // jungsung_base 
    jong = ( i - cho * chosung_base - jung * jungsung_base )    
    return (chosung_list[cho], jungsung_list[jung], jongsung_list[jong])

def character_is_korean(c):
    i = ord(c)
    return ((kor_begin <= i <= kor_end) or
            (jaum_begin <= i <= jaum_end) or
            (moum_begin <= i <= moum_end))

def levenshtein(s1, s2, debug=False):
    if len(s1) < len(s2):
        return levenshtein(s2, s1, debug)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))

        if debug:
            print(current_row[1:])

        previous_row = current_row

    return previous_row[-1]


def jamo_levenshtein(s1, s2, debug=False):
    if len(s1) < len(s2):
        return jamo_levenshtein(s2, s1, debug)

    if len(s2) == 0:
        return len(s1)

    def substitution_cost(c1, c2):
        if c1 == c2:
            return 0
        return levenshtein(decompose(c1), decompose(c2))/3

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            # Changed
            substitutions = previous_row[j] + substitution_cost(c1, c2)
            current_row.append(min(insertions, deletions, substitutions))

        if debug:
            print(['%.3f'%v for v in current_row[1:]])

        previous_row = current_row

    return previous_row[-1]


preCmds = ["초풍", "나락", "웨캔마신", "웨이브", "뻥발", "일어나"]

r = sr.Recognizer()
mic = sr.Microphone()

while 1 :

    print('Wait voice command ..')
    with mic as source :
        audio = r.listen(source)

    print('Your voice command :', end='')
    print(r.recognize_google(audio, language='ko-KR'))

    cmd = r.recognize_google(audio, language='ko-KR')

    if cmd in preCmds :
        if cmd == '나락' :
            narak()
        elif cmd == '초풍' :
            electric()

        elif cmd == '뻥발' :
            soccerkick()

        elif cmd == '웨캔마신' :
            mashin()
        
        elif cmd == '일어나' :
            getup()

        elif cmd == '웨이브' :
            wave()
    else :

        similarCmd = ""
        mostValue = 100
        for i in preCmds :
            value = jamo_levenshtein(cmd, i)
            if value < mostValue :
                mostValue = value
                similarCmd = i

        print('Most similar cmd : ', end='')
        print(similarCmd + ' / ', end='')
        print(mostValue)

        if similarCmd == '나락' :
            narak()
        elif similarCmd == '초풍' :
            electric()

        elif similarCmd == '뻥발' :
            soccerkick()

        elif similarCmd == '웨캔마신' :
            mashin()
        
        elif similarCmd == '일어나' :
            getup()

        elif similarCmd == '웨이브' :
            wave()
