import yt_dlp

def descargar_youtube(url, tipo="video"):
    try:
        if tipo == "audio":
            ydl_opts = {
                'format': 'bestaudio',
                'ext': 'mp3',
                'outtmpl': '%(title)s.%(ext)s'
            }
        else:
            ydl_opts = {
                'format': 'best',
                'outtmpl': '%(title)s.%(ext)s'
            }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    url = input("URL del video: ")
    tipo = input("Tipo (video/audio): ").lower()
    descargar_youtube(url, tipo)