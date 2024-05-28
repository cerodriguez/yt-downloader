from pytube import YouTube


def download_video(url, output_path='.'):
    try:
        # Create YouTube object
        yt = YouTube(url)
        
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        
        # Download the video
        print(f"Downloading '{yt.title}'...")
        stream.download(output_path)
        print(f"Downloaded '{yt.title}' successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    video_url = input("Enter the URL of the YouTube video: ")
    output_path = input("Enter the output path (leave blank for current directory): ") or '.'
    download_video(video_url, output_path)

