import yt_dlp

def download_youtube_mp3(url, output_path):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{output_path}/%(title)s.%(ext)s'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f'Successfully downloaded {url}')
    except Exception as e:
        print(f'Error downloading {url}: {str(e)}')

def download_from_list(file_path, output_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()

        for url in urls:
            url = url.strip()
            if url:  # Ignore empty lines
                download_youtube_mp3(url, output_path)

if __name__ == '__main__':
    input_file = 'list.txt'
    output_directory = 'downloaded_songs'

    download_from_list(input_file, output_directory)