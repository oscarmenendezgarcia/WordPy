import youtube_dl
import speech_recognition as sr
from wordcloud import WordCloud
from matplotlib import pyplot as plt

def download_audio(url, lang="en"):
        ops = {
                'outtmpl': 'tmp.fac',
                "format" : "bestaudio/best",                
                "postprocessors": [{
                "key": "",
                "preferredcodec": "flac",
                "preferredquality": "320",
        }],
        }
        with youtube_dl.YoutubeDL(ops) as yt:
                yt.download([url])

def transcribe_audio(path):
        r = sr.Recognizer()
        audioFile = sr.AudioFile(path)
        with audioFile as source:
                try:
                        r.adjust_for_ambient_noise(source,duration=5)
                        audio = r.record(source)
                        return r.recognize_google(audio, language="es-ES")
                except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))



def create_visualization(text):
        stop_words = { "a", "ante", "bajo", "cabo", "con", "contra", "de", "desde", "durante", "hacia", "hasta", "mediante", "para", "por", "segun", "sin", "son", "sobre", "tras", "el", "la", "los", "las"}
        wordcloud = WordCloud(background_color="white", stopwords=stop_words).generate(text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()


url = "https://www.youtube.com/watch?v=8qerVyCdlg4"
path = "tmp.flac"

# download_audio(url)
text = transcribe_audio(path)
create_visualization(text)