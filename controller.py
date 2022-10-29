"""Implementation for extract subtitle from video & audio file"""

import argparse
from datetime import timedelta
import os
from pathlib import Path
import sys

from tqdm import tqdm
from moviepy.editor import VideoFileClip, AudioFileClip
import speech_recognition as sr
from pydub.audio_segment import AudioSegment
from pydub.silence import split_on_silence

parser = argparse.ArgumentParser()
parser.add_argument(
    "cmd",
    choices=(
        "subtitle-video",
        "subtitle-audio",
    ),
)

parser.add_argument(
    "--file",
    "-f",
)

parser.add_argument("--outdir", "-o")

parser.add_argument(
    "--audio", "-a", default=False, action=argparse.BooleanOptionalAction
)

parser.add_argument("--lang", "-l", default="en-US")

r = sr.Recognizer()


class Program:
    pass


class File:
    """To processed file implementation based on moviepy.VideoClip"""

    def __init__(self, filename, is_audio=False):
        if is_audio:
            self.audio = AudioFileClip(filename)
        else:
            self.audio = VideoFileClip(filename).audio
        self.path: Path = Path(filename)

    def save_audio(self):
        if self.audio is not None:
            try:
                self.audio.write_audiofile(self.path.with_suffix(".mp3"))
            except AttributeError as e:
                pass
        else:
            print("Audio channel not found in file", self.path)
            sys.exit(2)

    @staticmethod
    def as_srt(idx: int, start: timedelta, end: timedelta, content: str):
        return f"""{idx}
{File.duration_as_str(start)} --> {File.duration_as_str(end)}
{content.strip()}\n
"""

    @staticmethod
    def duration_as_str(duration: timedelta) -> str:
        days, seconds = duration.days, duration.seconds
        hours = days * 24 + seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        milliseconds = duration.microseconds / 1e6 * 1000  # seconds // 1000

        return "%02d:%02d:%02d,%03d" % (hours, minutes, seconds, milliseconds)

    def generate_srt(self):
        errors = False
        self.save_audio()
        sound: AudioSegment = AudioSegment.from_mp3(self.path.with_suffix(".mp3"))
        print("Spliting audio file into chunks. Wait an instant ...")
        chunks: list[AudioSegment] = split_on_silence(
            sound,
            min_silence_len=500,
            silence_thresh=sound.dBFS - 15,  # type: ignore
            keep_silence=500,
        )

        current = 0
        with open(self.path.with_suffix(".srt"), "w") as f:
            for i, chunk in enumerate(tqdm(chunks), 1):
                chunk_path = os.path.join("assets", "chunks", f"chunk-{i}.flac")
                chunk.export(
                    chunk_path, format="flac"
                )  # Use flac format to be more lightweight
                with sr.AudioFile(chunk_path) as source:
                    listened = r.record(source)
                    try:
                        txt: str = r.recognize_google(listened)  # type: ignore
                    except sr.UnknownValueError as e:
                        txt = "Unable to recognize this part"
                        errors = True
                    except Exception as e:
                        print(e, e.args)
                        errors = True
                        txt = "Unable to recognize this part"

                content = File.as_srt(
                    i,
                    timedelta(seconds=current) + timedelta(milliseconds=100),
                    timedelta(seconds=current + chunk.duration_seconds),
                    txt,
                )
                f.write(content)
                os.remove(chunk_path)
                current += chunk.duration_seconds
        if errors:
            print(
                "Certaines erreurs ont été rencontrer lors de la génération du fichier."
            )
        print("Fichier de sous titre générer à", self.path.with_suffix(".srt"))


if __name__ == "__main__":
    pass
