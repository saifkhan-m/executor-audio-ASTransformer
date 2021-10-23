import csv
import json
import torchaudio
import numpy as np
import torch
import torch.nn.functional
import ast_exec.ast_params as ast_params

def _wav2fbank(filename, target_length):

    waveform, sr = torchaudio.load(filename)
    waveform = torchaudio.transforms.Resample(sr, ast_params.SAMPLE_RATE)(waveform[0:1].view(1, -1))
    waveform = waveform - waveform.mean()


    fbank = torchaudio.compliance.kaldi.fbank(waveform, htk_compat=True, sample_frequency=ast_params.SAMPLE_RATE, use_energy=False,
                                              window_type='hanning', num_mel_bins=ast_params.NUM_MEL_BINS, dither=0.0, frame_shift=10)

    target_length = target_length
    n_frames = fbank.shape[0]

    p = target_length - n_frames

    # cut and pad
    if p > 0:
        m = torch.nn.ZeroPad2d((0, 0, 0, p))
        fbank = m(fbank)
    elif p < 0:
        fbank = fbank[0:target_length, :]

    return fbank

def get_input(file, target_length, norm_mean, norm_std):
    """
    returns: image, audio, nframes
    where image is a FloatTensor of size (3, H, W)
    audio is a FloatTensor of size (N_freq, N_frames) for spectrogram, or (N_frames) for waveform
    nframes is an integer
    """
    fbank = _wav2fbank(file, target_length)

    # normalize the input for both training and test
    fbank = (fbank - norm_mean) / (norm_std * 2)
    fbank= torch.unsqueeze(fbank, 0)
    return fbank