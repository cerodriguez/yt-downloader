# YouTube Video Downloader

This Python project allows you to download YouTube videos by providing their URL. It uses the `pytube` library to handle the download process.

## Project Structure

```
yt-downloader/
├── youtube_video.py
├── youtube_audio.py
├── README.md
└── requirements.txt
```

## Features

- Download videos in the highest available resolution.
- Download audio-only streams.
- Customizable output path.

## Requirements

- Python 3.x
- `pytube` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/cerodriguez/yt-downloader.git
    cd yt-downloader
    ```

2. **Install the required libraries:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the script:**

For videos:

    ```bash
    python youtube_video.py
    ```

For audio:

    ```bash
    python youtube_audio.py
    ```

2. **Enter the URL of the YouTube video and the output path when prompted.**

    ```plaintext
    Enter the URL of the YouTube video: https://www.youtube.com/watch?v=example
    Enter the output path (leave blank for current directory): /path/to/save
    ```

3. **The video will be downloaded to the specified path.**

## Example

```bash
python youtube_video.py
```

Output:

```plaintext
Enter the URL of the YouTube video: https://www.youtube.com/watch?v=example
Enter the output path (leave blank for current directory): /path/to/save
Downloading 'Example Video'...
Downloaded 'Example Video' successfully!
```

