import torch
import numpy as np
import librosa
from synthesizer.inference import Synthesizer
from encoder import inference as encoder
from vocoder import inference as vocoder

# Load the pretrained models
encoder_model = encoder.load_model(torch.load("encoder/encoder.pt", map_location=torch.device('cpu')))
synthesizer_model = Synthesizer(torch.load("encoder/synthesizer.pt", map_location=torch.device('cpu')))
vocoder_model = vocoder.load_model(torch.load("encoder/vocoder.pt", map_location=torch.device('cpu')))

# Get the target speaker's voice from the user
target_speaker_audio = input("Enter the path to the target speaker's audio file: ")

# Define the target speaker's voice
speaker_embedding = encoder_model.embed_utterance(encoder_model.preprocess_wav(target_speaker_audio))

# Generate speech from text input
text = "Hello, how are you? I am Ravi Sastry Kolluru. This is my Openinapp assignment"
embeds = [speaker_embedding]
texts = [text]
specs = synthesizer_model.synthesize_spectrograms(texts, embeds)
generated_wav = vocoder_model.infer_waveform(specs[0])

# Save the generated speech as a WAV file
generated_audio_path = "gen_audio.wav"
librosa.output.write_wav(generated_audio_path, generated_wav.astype(np.float32), synthesizer_model.sample_rate)

print(f"Generated audio saved at: {generated_audio_path}")
