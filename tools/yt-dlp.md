---
id: yt-dlp
name: yt-dlp
emoji: 📺
category: process
desc: Descarga videos/audio de YouTube y +1000 sitios.
install: pip install yt-dlp
docs: https://github.com/yt-dlp/yt-dlp
code: |
  import yt_dlp

  # Descargar video
  ydl_opts = {
      'format': 'best',
      'outtmpl': '%(title)s.%(ext)s',
  }
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download(['https://youtube.com/watch?v=VIDEO_ID'])

  # Solo audio MP3
  ydl_opts = {
      'format': 'bestaudio/best',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
      }],
  }
input: URL de video
output: Archivo video/audio
---
