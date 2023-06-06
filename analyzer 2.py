import numpy as np
import wave
def getfr(path: str):
    raw = wave.open(path)

    # reads all the frames
    # -1 indicates all or max frames
    fr_rate = raw.getframerate()
    signal = raw.readframes(fr_rate)
    signal = np.frombuffer(signal, dtype="int16")
    chng=0
    for i in range(0,len(signal)-1):
        if (signal[i]<0 and signal[i+1]>0) or (signal[i]>0 and signal[i+1]<0):
            chng+=1
    fq=int(chng/3)
    wl=int(343/fq*10000)

    return (wl,fq)

if __name__ == "__main__":
    path = 'example_audio.wav'
    print(getfr(path))
