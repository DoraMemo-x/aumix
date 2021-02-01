# -*- coding: utf-8 -*-
"""
simple_signal.py

Generates simple signals such as sine waves or square waves.

@author: Chan Wai Lou
"""

from abc import ABC, abstractmethod

import numpy as np
from scipy import signal



class Signal(ABC):
    
    def __init__(self, freq=440, samp_rate=44100, duration=1):
        self.samp_rate = samp_rate
        self.duration = duration
        self.freq = freq
        self.samp_nums = np.arange(duration * samp_rate) / samp_rate
        
        self.gen_data()
        
    @abstractmethod
    def gen_data(self):
        pass
    
    

class SineSignal(Signal):
    
    def gen_data(self):
        self.data = np.sin(np.pi * self.freq * self.samp_nums)
    
    

class CosineSignal(Signal):
    
    def gen_data(self):
        self.data = np.cos(np.pi * self.freq * self.samp_nums)
    
    

class SquareSignal(Signal):
    
    def gen_data(self):
        self.data = signal.square(np.pi * self.freq * self.samp_nums)
    
    

class SawtoothSignal(Signal):
    
    def gen_data(self):
        self.data = (signal.sawtooth(np.pi * self.freq * self.samp_nums) + 1) / 2
    



    
    
# Example of using the Signal class
if __name__ == "__main__":
    print(SineSignal(freq=880).data)