from os import listdir
import os
import re

# Define the extensions to move here
documentExtensions = [".pdf", ".docx", ".doc", ".ppt", ".pptx"]
imageExtensions = [".jpg", ".png", ".jpeg"]
videoExtensins = [".mp4"]
archiveExtensions = [".xz", ".iso", ".zip", ".rar", ".7z", ".msi"]
executableExtensions = [".exe"]
# Add more types here

"""
 Use the format:
    typeExtensions = [ LIST of extensions to categorize ]
 
"""

# Add the function to check for the type

"""
    template:
    
    def isType(_fileName_):
        for i in TypeExtensions:
            if re.match(".*"+i , _fileName_):
                return True
        return False
"""



# Document file extension checker
def isDocument(_fileName_):
    for i in documentExtensions:
        if re.match(".*" + i, _fileName_):
            return True
    return False


# Image file extension checker
def isImage(_fileName_):
    for i in imageExtensions:
        if re.match(".*" + i, _fileName_):
            return True
    return False


# Video file extension checker
def isVideo(_fileName_):
    for i in videoExtensins:
        if re.match(".*" + i, _fileName_):
            return True
    return False


# Archive file extension checker
def isArchive(_fileName_):
    for i in archiveExtensions:
        if re.match(".*" + i, _fileName_):
            return True
    return False


# Exec file extension checker
def isExec(_fileName_):
    for i in executableExtensions:
        if re.match(".*" + i, _fileName_):
            return True
    return False


_location = os.path.abspath("./")
for i in listdir(_location):
    if isDocument(i):
        if os.path.exists(_location + "\\" + "Documents"):
            os.replace(_location + "\\" + i, _location + "\\Documents\\" + i)
        else:
            os.mkdir(_location + "\\" + "Documents")
            os.replace(_location + "\\" + i, _location + "\\Documents\\" + i)
    if isImage(i):
        if os.path.exists(_location + "\\" + "Images"):
            os.replace(_location + "\\" + i, _location + "\\Images\\" + i)
        else:
            os.mkdir(_location + "\\" + "Images")
            os.replace(_location + "\\" + i, _location + "\\Images\\" + i)
    if isVideo(i):
        if os.path.exists(_location + "\\" + "Videos"):
            os.replace(_location + "\\" + i, _location + "\\Videos\\" + i)
        else:
            os.mkdir(_location + "\\" + "Videos")
            os.replace(_location + "\\" + i, _location + "\\Videos\\" + i)
    if isArchive(i):
        if os.path.exists(_location + "\\" + "Archives"):
            os.replace(_location + "\\" + i, _location + "\\Archives\\" + i)
        else:
            os.mkdir(_location + "\\" + "Archives")
            os.replace(_location + "\\" + i, _location + "\\Archives\\" + i)
    if isExec(i):
        if os.path.exists(_location + "\\" + "Execs"):
            os.replace(_location + "\\" + i, _location + "\\Execs\\" + i)
        else:
            os.mkdir(_location + "\\" + "Execs")
            os.replace(_location + "\\" + i, _location + "\\Execs\\" + i)
    # Add the type checker here
    """
        Template:
        if isType(i):
            if os.path.exists(_location + "\\" + "Type"):
                os.replace(_location + "\\" + i, _location + "\\Type\\" + i)
            else:
                os.mkdir(_location + "\\" + "Execs")
                os.replace(_location + "\\" + i, _location + "\\Type\\" + i)
    """
if os.name == "nt":
    os.system("PAUSE")