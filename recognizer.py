import os
from faster_whisper import WhisperModel


model_path = "./asr-model/"
model_folder = os.path.join(model_path)
model_exists = os.path.exists(model_folder) and len(os.listdir(model_folder)) > 0


def speech_recognizer(audio):
    model = WhisperModel(
        model_size_or_path="small.en",
        device="cpu",
        compute_type="int8",
        download_root=model_path,
        local_files_only=model_exists,
    )

    segments, _ = model.transcribe(
        audio,
        language="en",
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=1000),
    )

    for segment in segments:
        return segment.text
