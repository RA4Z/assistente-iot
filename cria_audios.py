from gtts import gTTS

tts = gTTS('Olá, eu sou RAZ', lang='pt-br')
tts.save('audios/hello.mp3')
