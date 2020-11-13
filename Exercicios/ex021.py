from pygame import mixer

mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
while mixer.music.get_busy() == True: continue