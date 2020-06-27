import wave
import struct
import numpy as np
from pylab import *

def createSineWave (A, f0, fs, length):
    """振幅A、基本周波数f0、サンプリング周波数 fs、
    長さlength秒の正弦波を作成して返す"""
    data = []
    for n in arange(length * fs): 
        s = A * np.sin(2 * np.pi * f0 * n / fs)
        if s > 1.0:  s = 1.0
        if s < -1.0: s = -1.0
        data.append(s)

    data = [int(x * 32767.0) for x in data]
    data = struct.pack("h" * len(data), *data)
    return data


def createwav(data, f0, fs):
    print("create")
    w = wave.Wave_write("./create{}.wav".format(f0))
    p = (1, 2, fs, len(data), "NONE", "not compressed")
    w.setparams(p)
    w.writeframes(data)
    w.close


if __name__ == "__main__" :
    freqList = [250]
    for f in freqList:
        data = createSineWave(0.25, f, 8000, 1.0)
        createwav(data, f,  8000)
