import os
def createIfNotExist(folder):
    if not os.path.exists(folder):
            os.makedirs(folder)

def move(files, folderName):
    for file in files:
        os.replace(file, f"{folderName}\{file}")

if __name__ == "__main__":
    files = os.listdir()
    files.remove("AutomaticFolderCleaner.py")
    
    docExts = [".txt", ".doc", ".docx", ".pdf", ".xls", ".xlsx", ".xlsm", ".ods", ".htm", ".html", ".ppt", ".pptx"]
    docs = [file for file in files  if os.path.splitext(file)[1].lower() in docExts]
    
    imageExts = [".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".ps", ".pstde", ".svg", ".tif", ".tiff"]
    images = [file for file in files  if os.path.splitext(file)[1].lower() in imageExts]
    
    mediaExts = [".mp3", ".mid", ".midi", ".wav", ".3gp", ".avi", ".flv", ".mkv", ".mp4", ".wmv"]
    medias = [file for file in files  if os.path.splitext(file)[1].lower() in mediaExts]
    
    compressedExts = [".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar", ".gz", ".z", ".zip"]
    compressed = [file for file in files  if os.path.splitext(file)[1].lower() in compressedExts]
    
    otherExts = []
    
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in docExts) and (ext not in imageExts) and (ext not in mediaExts) and (ext not in compressedExts) and (os.path.isfile(file)):
            otherExts.append(file)

    if len(docs)>0:
        createIfNotExist("Docs")
        move(docs, "Docs")
    if len(images)>0:
        createIfNotExist("Images")
        move(images, "Images")
    if len(medias)>0:
        createIfNotExist("Media")
        move(medias, "Media")
    if len(compressed)>0:
        createIfNotExist("Compressed")
        move(compressed, "Compressed")
    if len(otherExts)>0:
        createIfNotExist("otherExts")
        move(otherExts, "otherExts")
