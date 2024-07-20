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
## Error Fix
When running the script, you may encounter the following error:
```bash
pytube.exceptions.RegexMatchError: get_throttling_function_name: could not find match for multiple
```
This error occurs because YouTube made changes on its end, resulting in a regular expression filter mismatch in the `cipher.py` class of the pytube library. To resolve this issue, follow the steps below:
1. Locate the `cipher.py` file. You can find it at a path similar to: `Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pytube/cipher.py`.
2. Find the following lines of code:
```bash
r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
    r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
```
3. Replace those lines with the following code:
```bash
r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
    r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
```
By making these changes, the error should be resolved, and the script should run without any issues.

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

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
