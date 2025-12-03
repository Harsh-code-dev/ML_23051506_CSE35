import soundfile as sf

audio, sample_rate = sf.read("mixkit-crickets-and-insects-in-the-wild-ambience-39.wav")
print("Sample Rate:", sample_rate)
print("Audio Length:", len(audio))