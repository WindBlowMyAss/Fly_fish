from ffmpy import FFmpeg

import os
import numpy as np
f = open("E://CoffeeData/RecordFile/20211216/192.168.1.214_8000_1_158BB0CF903C41DABBD6A47CF1305427_/Stage1.wav")
f.seek(0)
f.read(44)
data = np.fromfile(f, dtype=np.int16)
data.tofile("E://CoffeeData/RecordFile/20211216/192.168.1.214_8000_1_158BB0CF903C41DABBD6A47CF1305427_/Stage1.pcm")

# import numpy as np
# def wav2pcm(wavfile, pcmfile, data_type=np.int16):
#     f = open(wavfile, "rb")
#     f.seek(0)
#     f.read(44)
#     data = np.fromfile(f, dtype= data_type)
#     data.tofile(pcmfile)
#将mp3转化没pcm
# ff = FFmpeg(inputs={r'E:\CoffeeData\RecordFile\20211216\192.168.1.214_8000_1_158BB0CF903C41DABBD6A47CF1305427_\Stage1.mp3':"-i"},
#            outputs={r'E:\CoffeeData\RecordFile\20211216\192.168.1.214_8000_1_158BB0CF903C41DABBD6A47CF1305427_\Stage1.pcm':"-f s16le -ar 16000 -ac 2 -acodec pcm_s16le"})
#
# print(ff.cmd)
# ff.run()

#将pcm转化为mp3
# ff1 = FFmpeg(inputs={r'd:\test\1.pcm':"-f s16be -ar 16000 -ac 1 -acodec pcm_s16be"},
#            outputs={r'd:\test\1.mp3':None})
#
# print(ff1.cmd)
# ff1.run()