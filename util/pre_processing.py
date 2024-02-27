import pypianoroll
import muspy


def midi_2_array(midi_file, num_of_tracks=1):
    midi= pypianoroll.read(midi_file)
    midi.tracks[0].trim()
    roll = muspy.from_pypianoroll(midi)
    roll = muspy.to_pianoroll_representation(roll)
    roll = roll[:][:-1]
    return roll

def array_2_midi(array, file_name="output"):
    output = muspy.from_pianoroll_representation(array)
    output_folder = "output/"
    file_name = file_name+".MID"
    muspy.outputs.write_midi(output_folder+file_name, output)
    return output_folder+file_name