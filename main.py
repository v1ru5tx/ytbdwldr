#!./venv/bin/python
import sys
from art import *
from pytube import YouTube

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def progress_func(stream, chunk, bytes_remaining):
    curr = stream.filesize - bytes_remaining
    done = int(50 * curr / stream.filesize)
    sys.stdout.write("\r[{}{}] ".format('=' * done, ' ' * (50-done)) )
    sys.stdout.flush()

def helpPanel():
    tprint(f"YTB Downloader", font="random")
    print(f"\n{OKBLUE}Usage:",sys.argv[0],f"{ENDC}",f"{FAIL}[url_youtube_to_download]{ENDC}",f"{OKGREEN}[audio|video]{ENDC}")


def main():
    if len(sys.argv) != 3:
        helpPanel()
    else: 
        url = sys.argv[1]
        tipo = "mp4"
        yt = YouTube(url,on_progress_callback=progress_func)
        if sys.argv [2] == "audio":
            yt.streams.filter(only_audio=True).order_by('abr').desc().first().download()
        else: 
            yt.streams.filter(progressive=True).order_by('resolution').desc().first().download()


if __name__ == "__main__":
    main()
