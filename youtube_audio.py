from pytube import YouTube


def download_audio(url, output_path='.'):
    try:
        # Create YouTube object
        yt = YouTube(url)
        
        # Get the audio stream
        stream = yt.streams.filter(only_audio=True).first()
        
        # Download the audio
        print(f"Downloading audio of '{yt.title}'...")
        stream.download(output_path)
        print(f"Downloaded audio of '{yt.title}' successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    video_url = input("Enter the URL of the YouTube video: ")
    output_path = input("Enter the output path (leave blank for current directory): ") or '.'
    download_audio(video_url, output_path)

