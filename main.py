#given a csv file with the filename of the test audio file converts it to spectrogram
def make_specs():
    import os
    import matplotlib
    matplotlib.use('Agg')  # No pictures displayed
    import pylab
    import librosa
    import librosa.display
    import numpy as np
    import pandas as pd
    path = r"C:\Users\harih\Downloads"#enter path
    df = pd.read_csv(os.path.join(path, 'india.csv'))#filtered csv file based on country
    for index, row in df.iterrows():
        try:
            a = row["filename"]
            print(a)
            sig, fs = librosa.load(os.path.join(path,"archive","recordings","recordings", a+'.mp3'))#path to audio recordings
            save_path=os.path.join(path, "archive", "india", a + '.jpg')#save path
            pylab.axis('off')
            pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
            S = librosa.feature.melspectrogram(y=sig, sr=fs)
            librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
            pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
        except FileNotFoundError:
            continue
    pylab.close()


if __name__ == '__main__':
    make_specs()

