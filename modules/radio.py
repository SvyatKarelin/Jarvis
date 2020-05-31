import os
import pty
import subprocess
import time


class Radio(BaseModule):

    # конструктор
    def __init__(self):
        self.name = "Радио"
        self.listening = False
        super().__init__(self)

    def listen(self):
        if not self.listening:
            #p = subprocess.Popen(['mpg123', '-C', 'http://nashe1.hostingradio.ru/nashe-128.mp3'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p = subprocess.Popen(['mpg123', '-C', 'http://online.radiorecord.ru:8102/sd90_128'], stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.listening = True

    def stop(self):
        os.system("pkill mpg123")
        self.listening = False
