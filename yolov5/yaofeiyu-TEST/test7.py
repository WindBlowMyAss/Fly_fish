# import wave as we
#
# filename = 'E://CoffeeData/RecordFile/20211216/192.168.1.214_8000_1_158BB0CF903C41DABBD6A47CF1305427_/Stage1.wav'
#
# WAVE = we.open(filename)
# for item in enumerate(WAVE.getparams()):
#     print(item)
import wave as we
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

filename = 'E://CoffeeData/RecordFile/20211216/192.168.1.214_8000_1_158BB0CF903C41DABBD6A47CF1305427_/Stage1.wav'
WAVE = we.open(filename)
print('---------声音信息------------')
for item in enumerate(WAVE.getparams()):
    print(item)
a = WAVE.getparams().nframes    # 帧总数
f = WAVE.getparams().framerate  # 采样频率
sample_time = 1/f               # 采样点的时间间隔
time = a/f                      #声音信号的长度
sample_frequency, audio_sequence = wavfile.read(filename)
print(audio_sequence)           #声音信号每一帧的“大小”
x_seq = np.arange(0,time,sample_time)

plt.plot(x_seq,audio_sequence,'blue')
plt.xlabel("time (s)")
plt.show()