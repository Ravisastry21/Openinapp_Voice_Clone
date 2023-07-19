# Openinapp_Voice_Clone


**Voice Cloning using Real-Time-Voice-Cloning**

This project allows you to perform voice cloning by generating speech from text input using a target speaker's voice. The Real-Time-Voice-Cloning model is used for this purpose, which utilizes a combination of three models: an encoder, a synthesizer, and a vocoder.

Getting Started

To use this project, follow the steps below:

**Install the required dependencies by running the following commands:**
pip install inflect==5.3.0
pip install librosa==0.8.1
pip install matplotlib==3.5.1
pip install numpy==1.20.3
pip install Pillow==8.4.0
pip install PyQt5==5.15.6
pip install scikit-learn==1.0.2
pip install scipy==1.7.3
pip install sounddevice==0.4.3
pip install SoundFile==0.10.3.post1
pip install tqdm==4.62.3
pip install umap-learn==0.5.2
pip install Unidecode==1.3.2
pip install urllib3==1.26.7
pip install visdom==0.1.8.9
pip install webrtcvad==2.0.10
Save the pretrained model weights for the encoder, synthesizer, and vocoder in the encoder directory. Make sure to name the files as follows:

encoder.pt for the encoder model weights
synthesizer.pt for the synthesizer model weights
vocoder.pt for the vocoder model weights
Running the Voice Cloning Script

To clone a target speaker's voice, run the clone.py script. The script will prompt you to enter the path to the target speaker's audio file. The script will then use the Real-Time-Voice-Cloning model to generate speech from text input using the specified speaker's voice.

**Important Notes**

Ensure that you have Python and pip installed on your system.
Make sure to use compatible model weights with the Real-Time-Voice-Cloning model.
Respect privacy and obtain proper consent before using someone's voice for cloning.
Example Usage

Install the required dependencies using the provided pip commands.

Save the encoder, synthesizer, and vocoder model weights in the encoder directory.

Run the clone.py script.

Enter the path to the target speaker's audio file when prompted.

Provide text input to generate speech using the target speaker's voice.

The generated speech will be saved as a WAV file named generated_audio.wav.
