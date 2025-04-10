class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format.")
        self.filename = filename
class MP3File(AudioFile):
    ext = ".mp3"
    def play(self):
        print(f"Playing {self.filename} as MP3.")   
class WAVFile(AudioFile):   
    ext = ".wav"
    def play(self):
        print(f"Playing {self.filename} as WAV.")
class OOGFile(AudioFile):
    ext = ".ogg"
    def play(self):
        print(f"Playing {self.filename} as OGG.")
mp3=MP3File("song.mp3")
wav=WAVFile("song.wav")
ogg=OOGFile("song.ogg")

mp3.play()
wav.play()  
ogg.play()


    