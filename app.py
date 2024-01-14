from pytube import YouTube
import assemblyai as aai
import os,re
from dotenv import load_dotenv
load_dotenv()

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

def transcriber(file_path):
    try:
        config = aai.TranscriptionConfig(speaker_labels=True)
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(
        file_path,
        config=config).utterances 

        return "".join([f"Speaker {utterance.speaker}: {utterance.text}\n\n" for utterance in transcript])
    
    except Exception as e:
        return "Unable to transcribe audio. Please try again later."
    
    finally:
        os.remove(file_path)

def download_youtube_audio(url):
    output_path = 'audio'

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    video = YouTube(url)
    file_path = os.path.join(output_path,f"{video.title}.mp3")

    try:
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filename=file_path)

    except KeyError:
        print("Unable to fetch video information. Please check the video URL or your network connection.")

    return file_path