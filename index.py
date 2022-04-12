from pytube import YouTube
link = input("Wprowadź link do filmu: ")
print("Pobieranie...")
YouTube(link).streams.first().download()
print("Pobieranie zakończone")