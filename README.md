# YouTube Downloader
This script allows you to download audio and/or video files from YouTube.

## Libraries
Before running the script, make sure you have installed the following libraries:
```bash
pip install ffmpeg-python pytube youtube-search-python tqdm validators
```
If you are using macOS, use the following command instead of `pip install ffmpeg-python`:
```bash
brew install ffmpeg
```

## Usage
To use the script, follow these steps:
1. Edit the `querylist` variable in the `main()` function. This list should contain the YouTube search queries or URLs of the videos you want to download.
2. Adjust the following variables in the `main()` function according to your requirements:
   - `view_filter`: Set this boolean variable to `True` if you want the script to prioritize downloading the video with the highest view count from the YouTube search results. Set it to `False` to download the first result in the search list.
   - `max_results`: This integer variable specifies the maximum number of search results to consider when using a search query. For example, if `max_results` is set to 3, the script will only look at the top 3 results from the YouTube search.
   - `need_video`: Set this boolean variable to `True` if you want to download both the video and audio files. Set it to `False` to only download the audio file.
   - `max_res`: This integer variable specifies the maximum resolution for video downloads. For example, if `max_res` is set to 1080, the script will download the highest available resolution up to 1080p.
   - `mp3`: Set this boolean variable to `True` if you want the downloaded audio file to be converted to MP3 format. Set it to `False` to download the audio file in its original format.
3. Run the script.

## Notes
- The script assumes that the YouTube videos you are downloading are not age-restricted.
- The script may not work correctly if the YouTube videos are unavailable or have been removed.
