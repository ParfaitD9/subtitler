import argparse
from moviepy.editor import VideoFileClip
import speech_recognition as sr
from datetime import timedelta
import os 
from pydub.audio_segment import AudioSegment
from pydub.silence import split_on_silence


parser = argparse.ArgumentParser()
parser.add_argument(
    'cmd',
    choices=(
        'subtitle-video',
        'subtitle-audio',
    ),
)

parser.add_argument(
    '--file',
    '-f',   
)

parser.add_argument(
    '--outdir',
    '-o'
)

parser.add_argument(
    '--audio',
    '-a',
    default=False,
    action=argparse.BooleanOptionalAction
)

parser.add_argument(
    '--lang',
    '-l',
    default='en-US'
)

r = sr.Recognizer()

def get_audio(file : str) -> str:
    video = VideoFileClip(file)
    audio_name = file.replace('mp4', 'wav')

    try:
        video.audio.write_audiofile(audio_name, codec='pcm_s16le')
    except:
        pass
    else:
        return audio_name

def get_large_audio_transcription(path, outdir=None, save_audio=False, lang='en-US'):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    filename : str = os.path.basename(path)
    if outdir is None:
        outdir = os.path.dirname(path)
    
    # open the audio file using pydub
    sound : AudioSegment= AudioSegment.from_wav(path)
    
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks : list[AudioSegment] = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    chunks_dir = "./files/audio/audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(chunks_dir):
        os.makedirs(chunks_dir, exist_ok=True)
    current = 0
    with open(os.path.join(outdir, filename.replace('wav', 'srt')), 'w') as f:
        # process each chunk 
        for i, audio_chunk in enumerate(chunks, start=1):
            # export audio chunk and save it in
            # the `folder_name` directory.
            chunk_filename = os.path.join(chunks_dir, f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            # recognize the chunk
            with sr.AudioFile(chunk_filename) as source:
                audio_listened = r.record(source)
                
                # try converting it to text
                try:
                    text : str = r.recognize_google(audio_listened, language=lang)
                except sr.UnknownValueError as e:
                    print("Error:", str(e))
                except (Exception, ) as e:
                    print(f'{e.__class__} : {e.args}')
                else:
                    _from = str(timedelta(seconds=current)).replace('.', ',')[:-3]
                    to = str(timedelta(seconds= current + audio_chunk.duration_seconds)).replace('.', ',')[:-3]
                    to_wrote = f"""
{i}
{_from} --> {to}
{text}\n
""".removeprefix('\n')
                    print("to_wrote est :\n", to_wrote)
                    f.write(to_wrote)
                current += audio_chunk.duration_seconds
                print(f"{round(current / sound.duration_seconds * 100, 2)} % done ")
    print('Subtitle generation done !')
    print('Removing junks ...')
    for fil in os.listdir(chunks_dir):
        try:
            os.remove(os.path.join(chunks_dir, fil))
        except (FileNotFoundError, ) as e:
            pass
        except (Exception, ) as e:
            print(f'{e.__class__} : {e.args}')
    else:
        print('Chunks removed !')
        if not save_audio:
            os.remove(path)

def get_subtitle(path,):
    audio = get_audio(path)
    get_large_audio_transcription(audio)

def _get_subtitle(file, outdir=None, save_audio=False, lang='en-US'):
    video = VideoFileClip(file)
    audio_name = file.replace('mp4', 'wav')

    try:
        video.audio.write_audiofile(audio_name, codec='pcm_s16le')
    except:
        return
    else:
        path =  audio_name
        filename : str = os.path.basename(path)
        if outdir is None:
            outdir = os.path.dirname(path)
        
        # open the audio file using pydub
        sound : AudioSegment= AudioSegment.from_wav(path)
        
        # split audio sound where silence is 700 miliseconds or more and get chunks
        chunks : list[AudioSegment] = split_on_silence(sound,
            # experiment with this value for your target audio file
            min_silence_len = 500,
            # adjust this per requirement
            silence_thresh = sound.dBFS-14,
            # keep the silence for 1 second, adjustable as well
            keep_silence=500,
        )
        chunks_dir = "./files/audio/audio-chunks"
        # create a directory to store the audio chunks
        if not os.path.isdir(chunks_dir):
            os.makedirs(chunks_dir, exist_ok=True)
        current = 0
        with open(os.path.join(outdir, filename.replace('wav', 'srt')), 'w') as f:
            # process each chunk 
            for i, audio_chunk in enumerate(chunks, start=1):
                # export audio chunk and save it in
                # the `folder_name` directory.
                chunk_filename = os.path.join(chunks_dir, f"chunk{i}.wav")
                audio_chunk.export(chunk_filename, format="wav")
                # recognize the chunk
                with sr.AudioFile(chunk_filename) as source:
                    audio_listened = r.record(source)
                    
                    # try converting it to text
                    try:
                        text : str = r.recognize_google(audio_listened, language=lang)
                    except sr.UnknownValueError as e:
                        print("Error:", str(e))
                    except (Exception, ) as e:
                        print(f'{e.__class__} : {e.args}')
                    else:
                        #print("To is", str(timedelta(seconds= current + audio_chunk.duration_seconds)).replace('.', ','))
                        to_wrote = f"""
{i}
{str(timedelta(seconds=current)).replace('.', ',')[:-3]} --> {str(timedelta(seconds= current + audio_chunk.duration_seconds)).replace('.', ',')[:-3]}
{text}\n
""".removeprefix('\n')
                        f.write(to_wrote)
                    current += audio_chunk.duration_seconds
                    print(f"{round(current / sound.duration_seconds * 100, 2)} % done ")

        print('Subtitle generation done !')
        print('Removing junks ...')
        for fil in os.listdir(chunks_dir):
            try:
                os.remove(os.path.join(chunks_dir, fil))
            except (FileNotFoundError, ) as e:
                pass
            except (Exception, ) as e:
                print(f'{e.__class__} : {e.args}')
        else:
            print('Chunks removed !')
            if not save_audio:
                os.remove(path)
    
if __name__ == '__main__':
    args = parser.parse_args()
    if args.cmd == 'subtitle-video':
        _get_subtitle(file=args.file, outdir=args.outdir, save_audio=args.audio, lang=args.lang)
    elif args.cmd == 'subtitle-audio':
        pass