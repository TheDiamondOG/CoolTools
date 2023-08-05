# multitool.py
import os
from pytube import YouTube
import ffmpeg
import shlex


def download_youtube(url, output_path, audio_only=False):
    try:
        yt = YouTube(url)
        if audio_only:
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(output_path=output_path)
            input_file = os.path.join(output_path, f"{yt.title}.mp4")
            output_file = os.path.join(output_path, f"{yt.title}.mp3")
            ffmpeg.input(input_file).output(output_file).run()
            os.remove(input_file)  # Remove the original MP4 file after conversion
        else:
            video_stream = yt.streams.filter(file_extension="mp4", progressive=True).first()
            video_stream.download(output_path=output_path)
        return True
    except Exception as e:
        print(f"Error downloading video: {e}")
        return False


def convert(input_path, output_format="mp4"):
    try:
        output_path = "./converted"
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        output_file = os.path.join(output_path, f"converted.{output_format}")

        # Properly handle file paths with spaces using shlex.quote
        input_path_quoted = shlex.quote(input_path)
        output_file_quoted = shlex.quote(output_file)

        ffmpeg.input(input_path_quoted).output(output_file_quoted).run()
        print(f"File converted successfully! You can download it here: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main_menu():
    print("Welcome to the Multitool!")
    print("1. Download YouTube Video")
    print("2. Convert Video File")
    print("3. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        youtube_url = input("Enter the YouTube URL: ")
        download_youtube(youtube_url, "./downloads")
    elif choice == "2":
        input_file = input("Enter the path of the input video file: ")
        output_format = input("Enter the output format (mp4 by default): ")
        if not output_format:
            output_format = "mp4"
        convert(input_file, output_format)
    elif choice == "3":
        print("Exiting...")
        exit()
    else:
        print("Invalid option. Please try again.")

    main_menu()


if __name__ == "__main__":
    main_menu()
