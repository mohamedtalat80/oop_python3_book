import abc
class Medialoder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass
    @property
    @abc.abstractmethod
    def ext(self):
        pass

class MP3File(Medialoder):
    def ext(self):
        return ".mp3"
    def play(self):
        pass
mediamp3=MP3File()
mediamp3.play()