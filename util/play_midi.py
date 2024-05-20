import IPython.display as ipd
import pretty_midi
import os
# import pygame


def play_midi(midi_path, sr=22050): # notebook only
    if str(type(midi_path)) == "<class 'symusic.core.ScoreTick'>":
        holder_path = "data/holder.mid"
        midi_path.dump_midi(holder_path)
        midi_path=holder_path
    elif type(midi_path) == pretty_midi.pretty_midi.PrettyMIDI:
        audio_data = midi_path.synthesize(fs=sr)
        return ipd.Audio(audio_data, rate=sr)
    fn = os.path.join(midi_path)
    midi_data = pretty_midi.PrettyMIDI(fn)
    # Fs = 22050*2
    audio_data = midi_data.synthesize(fs=sr)
    return ipd.Audio(audio_data, rate=sr)


# def play_music(midi_filename): # in console
 
#   clock = pygame.time.Clock()
#   pygame.mixer.music.load(midi_filename)
#   pygame.mixer.music.play()
#   while pygame.mixer.music.get_busy():
#     clock.tick(30) # check if playback has finished

# def play_midi_console(midi_path):
#     import pygame
#     # midi_filename = 'FishPolka.mid'

#     # mixer config
#     freq = 44100  # audio CD quality
#     bitsize = -16   # unsigned 16 bit
#     channels = 2  # 1 is mono, 2 is stereo
#     buffer = 1024   # number of samples
#     pygame.mixer.init(freq, bitsize, channels, buffer)

#     # optional volume 0 to 1.0
#     pygame.mixer.music.set_volume(0.8)

#     # listen for interruptions
#     try:
#     # use the midi file you just saved
#         print(midi_filename)
#         play_music(midi_filename)
#     except KeyboardInterrupt:
#         # if user hits Ctrl/C then exit
#         # (works only in console mode)
#         pygame.mixer.music.fadeout(1000)
#         pygame.mixer.music.stop()
#     raise SystemExit


# play_midi("midi_files/afine-1.mid")
    