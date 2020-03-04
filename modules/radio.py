import os
import pty
import subprocess
import time
from JarvisCore import Jarvis

class Radio:
    def __init__(self):
        self.listening = False

    def listen(self):
        if not self.listening:
            p = subprocess.Popen(['mpg123', '-C', 'http://nashe1.hostingradio.ru/nashe-128.mp3'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.listening = True

    def stop(self):
        os.system("pkill mpg123")
        self.listening = False
