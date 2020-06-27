import wave
import numpy as np
import matplotlib.pyplot as plt
import os

# waveファイル名
wfile = ""

# 開始
start = 0

# サンプル数
N = 256

# 表示する周波数上限
dis = 2000

class dft_obj:
  ar = 0.0
  ai = 0.0
  x = 0.0

# 講義にあった方
def dft_lect(start, f, N):
  Y = []
  for k in range(N):
    obj = dft_obj()
    ar = 0.0
    ai = 0.0
    for n in range(N):
      x = ((2 * np.pi) / N) * n * k
      ar += f[start + n] * np.cos(-x)
      ai += f[start + n] * np.sin(-x)
      
    ar /= N
    ai /= N
    x = np.sqrt(4.0 * ar * ar + 4.0 * ai * ai)

    obj.x = round(x, 2)
    obj.ar = round(ar, 2)
    obj.ai = round(ai, 2)

    Y.append(obj)

  return Y


def plt_lect(Y):
  print("次数\t実数部\t虚数部\t絶対値")
  i = 0
  freqList = [k * fs / N for k in range(N)]
  amplitudeSpectrum = [c.x for c in Y]
  phaseSpectrum = [np.arctan2(int(c.ai), int(c.ar)) for c in Y]
  for obj in Y:
    print(i, obj.ar, obj.ai, obj.x)
    i += 1

  fig = plt.figure()

  ax1 = fig.add_subplot(311)
  ax1.plot(range(start, start + N), f[start: start + N])
  ax1.axis([start, start + N, -1000.0, 1000.0])

  ax2 = fig.add_subplot(312)
  ax2.plot(freqList, amplitudeSpectrum, marker='o', linestyle='-')
  ax2.axis([0, dis, 0, 100])
  ax2.grid(True)

  ax3 = fig.add_subplot(313)
  ax3.plot(freqList, phaseSpectrum, marker='o', linestyle='-')
  ax3.axis([0, dis, -np.pi, np.pi])
  ax3.grid(True)

  plt.show()



if __name__ == "__main__":
    wf = wave.open(wfile, "r")

    fs = wf.getframerate()

    tmp = wf.readframes(wf.getnframes())
    f = np.frombuffer(tmp, dtype="int16") / float((2 ^ 15))

    
    wf.close()

    Y = dft_lect(start, f, N)
    plt_lect(Y)
