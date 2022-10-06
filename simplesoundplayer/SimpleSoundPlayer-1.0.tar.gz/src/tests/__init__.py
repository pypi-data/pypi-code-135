import vlc
import playsound

def playSoundFile(path):
    playsound.playsound(path)

def playSoundURL(url):
    p = vlc.MediaPlayer(url)
    p.play();

def playSoundYoutube(video):
    p = vlc.MediaPlayer(video)
    p.play();