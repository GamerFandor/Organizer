#!/usr/bin/env python3

import os

def Main() -> None:
    Files :list(str) = GetFiles()
    FileTypes :list(str) = GetAllFileTypes(Files)

    RootFolderName = "Files"
    MakeFolderHierarchy(FileTypes, RootFolderName)
    ManageFiles(Files, RootFolderName)   

# Returns every single file in the specific folder
def GetFiles():
    try:
        return os.listdir(os.getcwd())
    except:
        PrintError("Something went wrong while getting files from current working directory.")
        return None

# Exmaines the file and returns the type of it
def GetFileType(File :str) -> str:
    if File == None:
        return None

    try:
        ImageExtensions :list(str) = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps"]
        DocumentExtensions :list(str) = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ods", ".ppt", ".pptx", ".txt"]
        VideoExtensions :list(str) = [".WEBM", ".MPG", ".MP2", ".MPEG", ".MPE", ".MPV", ".OGG", ".MP4", ".M4P", ".M4V", ".AVI", ".WMV", ".MOV", ".QT", ".FLV", ".SWF", ".MPG"]
        AudioExtensions :list(str) = [".MP3", ".M4A", ".AAC", ".OGA", ".FLAC", ".WAV", ".PCM", ".AIFF"]
        ArchiveExtensions :list(str) = [".7z", ".XZ", ".BZIP2", ".GZIP", ".TAR", ".ZIP", ".WIM", ".AR", ".ARJ", ".CAB", ".CHM", ".CPIO", ".CramFS", ".DMG", ".EXT", ".FAT", ".GPT", ".HFS", ".IHEX", ".ISO", ".LZH", ".LZMA", ".MBR", ".MSI", ".NSIS", ".NTFS", ".QCOW2", ".RAR", ".RPM", ".SquashFS", ".UDF", ".UEFI", ".VDI", ".VHD", ".VHDX", ".VMDK", ".WIM", ".XAR", ".Z"]

        if not os.path.isfile(File):
            return "Folder"

        for i in ImageExtensions:
            if File.endswith(i.lower()):
                return "Image"

        for i in DocumentExtensions:
            if File.endswith(i.lower()):
                return "Document"

        for i in VideoExtensions:
            if File.endswith(i.lower()):
                return "Video"

        for i in AudioExtensions:
            if File.endswith(i.lower()):
                return "Audio"

        for i in ArchiveExtensions:
            if File.endswith(i.lower()):
                return "Archive"
        
        return "Other"
    except:
        PrintError("Something went wrong while determining file types.")
        return None

# Examines files in the specific folder and determines the type of every file
def GetAllFileTypes(Files):
    if Files == None:
        return None

    output :list(str) = []
    for f in Files:
        if f.startswith("."):
            continue

        if not GetFileType(f) in output:
            output.append(GetFileType(f)) 
    
    PrintSuccess("File types determined.")
    return output

# Make separeted folders for each file type
def MakeFolderHierarchy(FileTypes, RootFolderName) -> None:
    if FileTypes == None:
        return

    try:
        cwd :str = os.getcwd()
        if not os.path.exists(cwd + "/" + RootFolderName):
                os.makedirs(cwd + "/" + RootFolderName)    

        for Type in FileTypes:
            if Type == "Folder" and not os.path.exists(cwd + "/" + RootFolderName + "/Folders"):
                os.makedirs(cwd + "/" + RootFolderName + "/Folders")
            if Type == "Image" and not os.path.exists(cwd + "/" + RootFolderName + "/Images"):
                os.makedirs(cwd + "/" + RootFolderName + "/Images")
            if Type == "Document" and not os.path.exists(cwd + "/" + RootFolderName + "/Documents"):
                os.makedirs(cwd + "/" + RootFolderName + "/Documents")
            if Type == "Video" and not os.path.exists(cwd + "/" + RootFolderName + "/Videos"):
                os.makedirs(cwd + "/" + RootFolderName + "/Videos")
            if Type == "Auido" and not os.path.exists(cwd + "/" + RootFolderName + "/Auidos"):
                os.makedirs(cwd + "/" + RootFolderName + "/Auidos")
            if Type == "Archive" and not os.path.exists(cwd + "/" + RootFolderName + "/Archives"):
                os.makedirs(cwd + "/" + RootFolderName + "/Archives")
            if Type == "Other" and not os.path.exists(cwd + "/" + RootFolderName + "/Other"):
                os.makedirs(cwd + "/" + RootFolderName + "/Other")
        
        PrintSuccess("File hierarchy created.")
    except:
        PrintError("Something went wrong while making file hierarchy.")

# Manages files into the specific folder
def ManageFiles(Files, RootFolderName) -> None:
    if Files == None:
        return
    
    try:
        cwd :str = os.getcwd().replace("\\", "/")
        for i in Files:
            if i.startswith(".") or i == RootFolderName:
                continue

            if GetFileType(i) == "Image":
                os.rename(cwd + "/" + i, cwd + "/" + RootFolderName + "/Images/" + i)
            elif GetFileType(i) == "Document":
                os.rename(cwd + "/" + i, cwd + "/" + RootFolderName + "/Documents/" + i)
            elif GetFileType(i) == "Video":
                os.rename(cwd + "/" + i, cwd + "/" + RootFolderName + "/Videos/" + i)
            elif GetFileType(i) == "Audio":
                os.rename(cwd + "/" + i, cwd + "/" + RootFolderName + "/Audios/" + i)
            elif GetFileType(i) == "Archive":
                os.rename(cwd + "/" + i, cwd + "/" + RootFolderName + "/Archives/" + i)
            elif GetFileType(i) == "Folder":
                os.rename(cwd + "/" + i, cwd + "/" + RootFolderName + "/Folders/" + i)
            else:
                os.rename(cwd + "/" + i, cwd + "/" + RootFolderName + "/Other/" + i)

        PrintSuccess(f"Every file organised in '{GetCurrentWorkingDirectory()}' folder.")
    except:
        PrintError("Something went wrong while copying files.")

# Get Current working directory (only the directory's name, not the path to the directory)
def GetCurrentWorkingDirectory() -> str:
    CWD :str = os.getcwd()
    CWD = CWD.replace("\\", "/")
    Folders :list(str) = CWD.split("/")

    return Folders[len(Folders) - 1]

# Print a formatted succes message
def PrintSuccess(Message :str):
    Green = '\033[92m'
    EndGreen = '\033[0m'
    print(f"[ {Green}Done{EndGreen} ] {Message}")

# Print a formatted error message
def PrintError(Message :str):
    Red = '\033[91m'
    EndRed = '\033[0m'
    print(f"[ {Red}Fail{EndRed} ] {Message}")

if __name__ == "__main__":
    Main()
