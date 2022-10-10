import os
import shutil

def CheckFile(inDstPathStr, inTmplPathStr):
	if os.path.exists(inDstPathStr) == False:
		shutil.copy(inTmplPathStr, inDstPathStr)

def CheckFolder(inDstPathStr):
    # проверка наличия всех файлов/каталогов
    if not os.path.exists(os.path.abspath(inDstPathStr)):
        os.mkdir(inDstPathStr)