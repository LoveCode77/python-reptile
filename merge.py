from moviepy.editor import VideoFileClip, AudioFileClip

# 加载视频和音频文件
video_clip = VideoFileClip("shiping1.mp4")
audio_clip = AudioFileClip("yingping1.mp3")

# 确保音频和视频的长度相匹配
# 如果它们不匹配，你可能需要裁剪或填充其中一个
# 这里我们假设它们的长度已经匹配

# 设置视频的音频为加载的音频
video_clip = video_clip.set_audio(audio_clip)

# 导出合并后的视频
video_clip.write_videofile("merge_video.mp4", codec="libx264", audio_codec="aac")