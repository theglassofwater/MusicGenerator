from miditok import REMI, TokenizerConfig
from miditok.pytorch_data import DatasetTok, DataCollator
from pathlib import Path
from symusic import Score
# import tokenizers
# from matplotlib import pyplot as plt
# import glob


# from torch.utils.data import DataLoader

# class data_controller:

#     def __init__(self, num_velocities=16, use_chords=True, use_programs=True) -> None:
#         config =  TokenizerConfig(num_velocities=num_velocities, use_chords=use_chords, use_programs=use_programs)
#         tokenizer = REMI(config)
#         midi_files = list(Path("..\\data\\test\\").glob("**/*.mid"))

#     def train_tokenizer(self, vocab):
#         tokenizer.learn_bpe(30000, files_paths=midi_files)

#     def load_tokenizer(self, file_path):
#         pass

#     def generate_data_loader(self, min_seq_len=100, max_seq_len=1024):
#         dataset = DatasetTok(
#             files_paths=midi_files,
#             min_seq_len=100,
#             max_seq_len=1024,
#             tokenizer=tokenizer
#         )

#         collator = DataCollator(
#             tokenizer["PAD_None"], tokenizer["BOS_None"], tokenizer["EOS_None"]
#         )

        
#         return DataLoader(dataset=dataset, collate_fn=collator)