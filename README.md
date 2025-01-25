# TubetoAux.py

## Overview
This script allows users to download audio from a YouTube video in their preferred format using the `yt_dlp` library. The downloaded audio file is saved locally with the video's title as the filename.

---

## Prerequisites
1. **Install Python**: Download and install Python from the official website: [https://www.python.org/](https://www.python.org/). Ensure you add Python to your system's PATH during installation.
2. **Install `yt_dlp`:** Use the following command to install the required library:
    ```bash
    pip install yt-dlp
    ```
3. **FFmpeg:** The script uses FFmpeg for audio extraction. Install FFmpeg on your system. For installation instructions, visit [FFmpeg's official website](https://ffmpeg.org/download.html).

---

## Windows Setup
1. **Install Python**:
   - Download Python from [https://www.python.org/](https://www.python.org/).
   - During installation, select "Add Python to PATH" to make it accessible from the command prompt.
2. **Install FFmpeg**:
   - Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
   - Extract the downloaded zip file and add the `bin` folder to your system's PATH. To do this:
     - Right-click "This PC" or "My Computer" and select "Properties."
     - Click "Advanced system settings" > "Environment Variables."
     - Under "System Variables," find the `Path` variable and click "Edit."
     - Add the path to the `bin` folder of FFmpeg.
3. **Run the Script**:
   - Save the script as `tubetoaux.py`.
   - Open Command Prompt in the script's directory and run:
     ```bash
     python tubetoaux.py
     ```

---

## Linux Setup
1. **Install Python**:
   - Most Linux distributions come with Python pre-installed. Verify by running:
     ```bash
     python3 --version
     ```
   - If not installed, use your package manager (e.g., `sudo apt install python3`).
2. **Install FFmpeg**:
   - Use the package manager to install FFmpeg. For example, on Ubuntu:
     ```bash
     sudo apt update
     sudo apt install ffmpeg
     ```
3. **Run the Script**:
   - Save the script as `tubetoaux.py`.
   - Open a terminal in the script's directory and run:
     ```bash
     python3 tubetoaux.py
     ```

---

## Code Explanation

### Imports
The script imports `yt_dlp` and references it as `youtube_dl` for compatibility with older code conventions:
```python
import yt_dlp as youtube_dl
```

### Function: `download_youtube_audio`
This function handles the audio download and extraction:
```python
def download_youtube_audio(url, audio_format):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': audio_format,
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
```
#### Parameters:
- `url`: The URL of the YouTube video.
- `audio_format`: Desired audio format (e.g., `mp3`, `wav`, `m4a`).

#### Options:
- `format`: Specifies the best available audio format.
- `postprocessors`: Extracts audio using FFmpeg and converts it to the desired format.
- `outtmpl`: Defines the output filename format using the video's title.

### User Input and Validation
The script prompts the user for the YouTube video URL and desired audio format:
```python
video_url = input("Enter the YouTube video URL: ").strip()
while not video_url:
    print("You must enter a valid YouTube URL!")
    video_url = input("Enter the YouTube video URL: ").strip()

audio_format = input("Enter the desired audio format (mp3, wav, m4a, etc.): ").strip()
```

### Error Handling
The script handles errors gracefully during the download process:
```python
try:
    download_youtube_audio(video_url, audio_format)
    print("Download complete!")
except Exception as e:
    print(f"An error occurred: {e}")
```
This ensures the script provides meaningful feedback if something goes wrong.

---

## Usage
1. Ensure Python is installed and accessible from your command line or terminal.
2. Save the script as a `.py` file (e.g., `tubetoaux.py`).
3. Open a terminal or command prompt in the directory where the script is saved.
4. Run the script with the following command:
    ```bash
    python tubetoaux.py
    ```
5. Enter the YouTube video URL when prompted.
6. Specify the desired audio format (e.g., `mp3`, `wav`).
7. The audio file will be downloaded and saved in the current working directory.

---

## Example
### Input:
```
Enter the YouTube video URL: https://www.youtube.com/watch?v=example
Enter the desired audio format (mp3, wav, m4a, etc.): mp3
```
### Output:
```
Download complete!
```
The file `ExampleTitle.mp3` will be saved locally.

---

## Notes
- Ensure FFmpeg is properly installed and accessible from your system's PATH.
- Check the YouTube URL validity before proceeding to avoid errors.
