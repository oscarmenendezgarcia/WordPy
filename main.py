import youtube_dl
import speech_recognition as sr
from wordcloud import WordCloud
from matplotlib import pyplot as plt

spanish_prepositions = [ "a", "ante", "bajo", "cabo", "con", "contra", "de", "desde", "durante", "hacia", "hasta", "mediante", "para", "por", "segun", "sin", "son", "sobre", "tras"]

def download_audio(url, lang="es"):
        ops = {
                "format" : "bestaudio/best",
                "outtmpl" : "",
                "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "flac",
                "preferredquality": "320",
        }],
        }
        with youtube_dl.YoutubeDL(ops) as yt:
                yt.download([url])

def transcribe_audio(path):
        r = sr.Recognizer()

        audioFile = sr.AudioFile("DEBATE ATRESMEDIA 28A - LOS MEJORES MOMENTOS-8qerVyCdlg4.flac")
        with audioFile as source:
                audio = r.record(source, duration=90)
                return r.recognize_google(audio, language="es")

def create_visualization(text):     
        wordcloud = WordCloud().generate(text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()


url = "https://www.youtube.com/watch?v=8qerVyCdlg4"

# download_audio(url)

path = "C:/Users/omenendez.ext/Desktop/WordPy/DEBATE ATRESMEDIA 28A - LOS MEJORES MOMENTOS-8qerVyCdlg4"
text = transcribe_audio(path)
create_visualization(text)