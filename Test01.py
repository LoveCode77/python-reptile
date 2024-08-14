import requests


def download_video(url, filename):
    """
    下载视频并保存到本地文件。
    """
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

            # 替换成实际的视频URL


video_url = 'http://example.com/path/to/video.mp4'
filename = 'downloaded_video.mp4'

download_video(video_url, filename)
print("视频下载完成！")