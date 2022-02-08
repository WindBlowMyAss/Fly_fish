from pydub import AudioSegment
import os


def mp3_wav(s_path, d_path):
    file = []
    for files in os.listdir(s_path):
        if files.endswith('.mp3'):
            file.append(files)
    for i in range(len(file)):
        sound = AudioSegment.from_mp3(s_path+'/'+file[i])
        sound.export(d_path+'/'+file[i].split('.')[0]+'.wav', format='wav')


if __name__ == "__main__":
    source_file_path = "E://CoffeeData/RecordFile/20211216/192.168.1.214_8000_1_158BB0CF903C41DABBD6A47CF1305427_"
    end_path = "E://CoffeeData/RecordFile/20211216/192.168.1.214_8000_1_158BB0CF903C41DABBD6A47CF1305427_"
    mp3_wav(source_file_path, end_path)
