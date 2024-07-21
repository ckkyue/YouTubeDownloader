# Imports
import datetime as dt
import ffmpeg
import os
from pytube import YouTube
from youtube_search import YoutubeSearch
from tqdm import tqdm
import validators

# Check if a string is a URL
def check_url(url_str):
    result = validators.url(url_str)
    if isinstance(result, validators.ValidationError):
        return False
    return result

# Create a list of URLs
def create_urls(querylist, view_filter=False, max_results=3):
    # Initialize an empty list to store the URLs
    urls = []

    # Iterate over the list of queries
    for query in querylist:
        if check_url(query):
            # Append the query if it is already a URL
            urls.append(query)
        else:
            # Search YouTube for the query
            results = YoutubeSearch(query, max_results=max_results).to_dict()
            
            if view_filter:
                # Find the URL corresponding to the maximum views
                max_view = 0
                max_url = None

                # Iterate over all results
                for result in results:
                    view = int(''.join(filter(str.isdigit, result['views'])))
                    url = f"https://youtube.com{result['url_suffix']}"

                    # Replace the URL if the number of views is greater
                    if view > max_view:
                        max_view = view
                        max_url = url

                # Append the URL corresponding to the maximum views
                urls.append(max_url)
            else:
                # Get the first result
                result = results[0]
                url = f"https://youtube.com{result['url_suffix']}"

                # Append the URL
                urls.append(url)

        return urls
    
# Get the resolution of the available streams
def get_resolution(s):
    return int(s.resolution[:-1])

# Mix video and audio files
def video_audio_mix(path_audio, path_video, output_path):
    video = ffmpeg.input(path_video)
    audio = ffmpeg.input(path_audio)
    ffmpeg.concat(video, audio, v=1, a=1).output(output_path).run()

# Download YouTube audio and video files for the URLs
def download_urls(need_video, max_res, urls, mp3=True):
    # Iterate over all urls
    for url in tqdm(urls):
        # Create a YouTube object with the URL
        yt = YouTube(url)

        try:
            # Download the audio first
            audio = yt.streams.filter(only_audio=True).first()
            audio_file = audio.download()
            base, ext = os.path.splitext(audio_file)
            if mp3:
                audio_file_new = base + ".mp3"
                os.rename(audio_file, audio_file_new)
            else:
                audio_file_new = audio_file
            print(f"Audio download completed for {url}.")
            
            # Download the video if needed
            if need_video:
                # Download the video
                video = max(filter(lambda s: get_resolution(s) <= max_res, 
                            filter(lambda s: s.type == "video", yt.fmt_streams)),
                            key=get_resolution)
                video_file = video.download()
                base, ext = os.path.splitext(video_file)
                video_file_int = base + "_int" + ext
                os.rename(video_file, video_file_int)

                # Mix the video and audio files
                video_audio_mix(audio_file_new, video_file_int, video_file)
                os.remove(audio_file_new)
                os.remove(video_file_int)
                print(f"Video download completed for {url}.")

        except Exception as e:
            print(f"Error downloading for {url}: {e}\n.")

# Main function
def main():
    # Start of the program
    start = dt.datetime.now()
    print(start, "\n")

    # Variables
    view_filter = False
    max_results = 3
    need_video = True
    max_res = 1080
    mp3 = True

    # Define the queries
    querylist = [""]

    # Create a list of URLS from queries
    urls = create_urls(querylist, view_filter=view_filter, max_results=max_results)

    # Download YouTube audio and video files for the URLs
    download_urls(need_video, max_res, urls, mp3=mp3)

    # Print the end time and total runtime
    end = dt.datetime.now()
    print(end, "\n")
    print("The program used", end - start)

# Run the main function
if __name__ == "__main__":
    main()