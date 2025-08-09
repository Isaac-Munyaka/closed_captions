import queue
import sys
import os
import numpy as np
import sounddevice as sd
from datetime import datetime
from faster_whisper import WhisperModel
from transformers import pipeline

MODEL_SIZE = "small"
CHUNK_SECONDS = 5
SUMMARY_INTERVAL = 60
SAMPLE_RATE = 16000
SUMMARY_MODEL = "facebook/bart-large-cnn"