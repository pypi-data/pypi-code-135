
from pyOpenRPA.Tools import CrossOS
if CrossOS.IS_WINDOWS_BOOL: import pyaudio
if CrossOS.IS_WINDOWS_BOOL: from pydub import AudioSegment
import threading
import time
from pyOpenRPA.Utils import Text
import os

def DeviceMicrophoneIndex():
    """L-,W+: Выполнить поиск устройства, с помощью которого можно будет выполнить захват c микрофона.
    """
    p = pyaudio.PyAudio()
    lDeviceInfoDict = p.get_default_input_device_info()
    lDefaultIndexInt = lDeviceInfoDict["index"]
    return lDefaultIndexInt

def DeviceSystemSoundIndex():
    """L-,W+: Выполнить поиск устройства, с помощью которого можно будет выполнить захват аудио, которое поступает из приложений. Например: аудиоконференции Zoom, whatsapp, telegram и т.д.
    """
    p = pyaudio.PyAudio()
    inInputBool = True
    inIsLoopbackBool = True
    if inInputBool == True:
        lDeviceInfoDict = p.get_default_output_device_info()
        lDefaultIndexInt = lDeviceInfoDict["index"]
        lDefaultNameStr = lDeviceInfoDict["name"]
        lCatchIndexInt = None
        lCatchDiffRatioFloat = 0.0
        for lItemDict in DeviceListGet():
            lCompareBool = False
            if lItemDict["MaxOutputChannelsInt"]>0:
                if inIsLoopbackBool==True and lItemDict["HostApiStr"]=="Windows WASAPI": lCompareBool = True
                elif inIsLoopbackBool==False: lCompareBool = True
            if lCompareBool == True:
                lDiffRationFloat = Text.SimilarityNoCase(in1Str=lDefaultNameStr, in2Str=lItemDict["NameStr"])
                if lDiffRationFloat> lCatchDiffRatioFloat: 
                    lCatchDiffRatioFloat = lDiffRationFloat
                    lCatchIndexInt=lItemDict["IndexInt"]
    else:
        lDeviceInfoDict = p.get_default_output_device_info()
        lDefaultIndexInt = lDeviceInfoDict["index"]
        lDefaultNameStr = lDeviceInfoDict["name"]
        lCatchIndexInt = None
        lCatchDiffRatioFloat = 0.0
        for lItemDict in DeviceListGet():
            lCompareBool = False
            if lItemDict["MaxInputChannelsInt"]>0:
                if inIsLoopbackBool==True and lItemDict["HostApiStr"]=="Windows WASAPI": lCompareBool = True
                elif inIsLoopbackBool==False: lCompareBool = True
            if lCompareBool == True:
                lDiffRationFloat = Text.SimilarityNoCase(in1Str=lDefaultNameStr, in2Str=lItemDict["NameStr"])
                if lDiffRationFloat> lCatchDiffRatioFloat: lCatchIndexInt=lItemDict["IndexInt"]
    return lCatchIndexInt

def DeviceListGet():
    """L-,W+: Вернуть список аудио устройст (входящих и исходящих, микрофонов и динамиков).
    
    from pyOpenRPA.Robot import Audio
    Audio.DeviceListGet()

    :return: [{"IndexInt":1, "NameStr": "", 
            "HostApiInt": 0, "HostApiStr": "MME"|"Windows WASAPI"|"Windows WDM-KS",
            "MaxInputChannelsInt": 0, "MaxOutputChannelsInt": 0,
            "DefaultSampleRateFloat": 44100.0
        },...]
    :rtype: list
    """
    l_result = []
    p = pyaudio.PyAudio()
    for i in range(0, p.get_device_count()):
        l_info = p.get_device_info_by_index(i)
        l_info_dict = {
            "IndexInt":l_info["index"], 
            "NameStr": l_info["name"], 
            "MaxInputChannelsInt": l_info["maxInputChannels"], 
            "MaxOutputChannelsInt": l_info["maxOutputChannels"], 
            "HostApiInt": l_info["hostApi"], 
            "DefaultSampleRateFloat": l_info["defaultSampleRate"],
            "HostApiStr": p.get_host_api_info_by_index(l_info["hostApi"])["name"] #"MME"|"Windows WASAPI"|"Windows WDM-KS"
        }
        l_result.append(l_info_dict)
    return l_result

class Recorder:
    mStatusStr = "0_READY" # "0_READY", "1_RECORDING"
    mAudio = None
    mCaptureThread = None
    mStream = None

    mDeviceInt = None
    mChannelCountInt = None
    mFramesInt = 512
    mRecordedFramesList = []
    mSampleRateInt = None
    mSampleSizeInt = None

    mCaptureBool = True
    mFolderPathStr = None
    mFileNameStr = None
    mFileFormatStr = None
    mFileAvailableChunkInt = None
    mFileNameList=None

    mFileInfoDict=None # {"file.mp3":{StartSecFloat:, EndSecFloat:, Extra:,PathStr, }}

    mChunkSecFloat = None

    mStartSecFloat = None
    mStartChunkSecFloat = None
    mDurationSecFloat = None
    mThresholdInt = 500

    mSilentLastCheckTimeFloat = None
    mIsMicrophoneBool=None
    
    mCallbackChunkDef = None
    mCallbackChunkDefThreadList = []
    mCallbackStopDef = None
    mCallbackStopDefThreadList = []

    def __init__(self, inDeviceInt=None):
        """L-,W+: Инициализация экземпляра класса записи звука

        .. code-block:: python
            from pyOpenRPA.Robot import Audio
            lRec = Audio.Recorder()

        :param inDeviceInt: , по умолчанию None (использование устройства, полученного от DeviceSystemSoundIndex())
        :type inDeviceInt: int, опционально
        """
        
        self.mDeviceInt = inDeviceInt
        if inDeviceInt == None: inDeviceInt = DeviceSystemSoundIndex()
        self.mDeviceInt = inDeviceInt
        if DeviceListGet()[inDeviceInt]["MaxInputChannelsInt"]>0: self.mIsMicrophoneBool = True
        else: self.mIsMicrophoneBool = False
    
    def StatusGet(self):
        """L-,W+: Вернуть статус записи звука 

        .. code-block:: python
            from pyOpenRPA.Robot import Audio
            lRec = Audio.Recorder()
            lRec.StatusGet()

        :return: "0_READY" или "1_RECORDING"
        :rtype: str
        """
        return self.mStatusStr

    def CaptureStart(self, inFolderPathStr="",inFileNameStr = "out", inFileFormatStr = "mp3", inDurationSecFloat = None, inChunkSecFloat = 300.0, inCallbackChunkDef = None, inCallbackStopDef = None):
        """L-,W+: Начать запись звука

        .. code-block:: python

            def CallbackChunk(lRec, lFilenameStr):
                pass # КОД ОБРАБОТКИ ПОСЛЕ СОХРАНЕНИЯ ЧАСТИ

            from pyOpenRPA.Robot import Audio
            lRec = Audio.Recorder()
            lRec.CaptureStart(inFileNameStr = "out", inFileFormatStr = "mp3", inDurationSecFloat = None, inChunkSecFloat = 5.0, inCallbackChunkDef=CallbackChunk)
            lRec.CaptureStop()

        :param inFolderPathStr: Путь к папке, в которую сохранять аудиофайлы захвата , по умолчанию ""
        :type inFolderPathStr: str, опционально
        :param inFileNameStr: Наименование файла без расширения, по умолчанию "out"
        :type inFileNameStr: str, опционально
        :param inFileFormatStr: Наименование формата, в который будет происходить сохранение ("mp3" или "wav" или "raw" или "aif"), по умолчанию "mp3"
        :type inFileFormatStr: str, опционально
        :param inDurationSecFloat: Длительность захвата аудио, по умолчанию None (пока не поступит команда CaptureStop() )
        :type inDurationSecFloat: float, опционально
        :param inChunkSecFloat: Максимальная длина части аудиофайла, по умолчанию 300.0
        :type inChunkSecFloat: float, опционально
        :param inCallbackChunkDef: Функция, которая будет инициирована в случае выполнения Chunk сохранения (сохранение части). Callback функция должна принимать 2 аргумента: экземпляр класса Recorder и наименование сохраненного файла. Внимание! Функция запускается асинхронно!
        :type inCallbackChunkDef: def, опционально
        :param inCallbackStopDef: Функция, которая будет инициирована в случае окончания записи. Callback функция должна принимать 2 аргумента: экземпляр класса Recorder и наименование сохраненного файла. Внимание! Функция запускается асинхронно!
        :type inCallbackStopDef: def, опционально
        """
        # CHECK AUX.mp3
        self.mFileInfoDict = {}
        self.mFileNameList=[]
        #self.mRecordedFramesList=[]
        self.mStatusStr = "1_RECORDING"
        if inChunkSecFloat != None: self.mFileAvailableChunkInt = 0
        self.mDurationSecFloat = inDurationSecFloat
        self.mChunkSecFloat = inChunkSecFloat
        self.mSilentLastCheckTimeFloat=time.time()
        self.mFolderPathStr = inFolderPathStr
        self.mFileNameStr = inFileNameStr
        self.mFileFormatStr = inFileFormatStr
        self.mAudio = pyaudio.PyAudio()
        self.mSampleSizeInt = self.mAudio.get_sample_size(pyaudio.paInt16)
        self.mCallbackChunkDef = inCallbackChunkDef
        self.mCallbackStopDef = inCallbackStopDef
        lDeviceInfoDict = self.mAudio.get_device_info_by_index(self.mDeviceInt)
        #Open stream
        self.mSampleRateInt = int(lDeviceInfoDict["defaultSampleRate"])
        self.mChannelCountInt = lDeviceInfoDict["maxInputChannels"] if (lDeviceInfoDict["maxOutputChannels"] < lDeviceInfoDict["maxInputChannels"]) else lDeviceInfoDict["maxOutputChannels"]
        self.mStream = self.mAudio.open(format = pyaudio.paInt16,
                        channels = self.mChannelCountInt,
                        rate = self.mSampleRateInt,
                        input = True,
                        frames_per_buffer = self.mFramesInt,
                        input_device_index = lDeviceInfoDict["index"],
                        as_loopback = not self.mIsMicrophoneBool)
        self.mCaptureThread = threading.Thread(target=self.__Capture__, daemon = True)
        self.mStartSecFloat = time.time()
        self.mStartChunkSecFloat = self.mStartSecFloat
        self.mCaptureThread.start()

    def __Capture__(self):
        while self.mCaptureBool==True:
            self.mRecordedFramesList.append(self.mStream.read(self.mFramesInt))
            self.__TriggerCheck__()

    def CaptureWait(self, inWaitCallbackChunkBool = True, inWaitCallbackStopBool = True):
        """L-,W+: Ожидать окончания захвата аудио. Дополнительно настраивается ожидание окончания всех callback функций.

        .. code-block:: python
            from pyOpenRPA.Robot import Audio
            lRec = Audio.Recorder()
            lRec.CaptureStart(inFileNameStr = "out", inFileFormatStr = "mp3", inDurationSecFloat = 10.0, inChunkSecFloat = 5.0)
            lRec.CaptureWait()

        :param inWaitCallbackChunkBool: True - ожидать выполнение всех асинхронных callback по сохранению части аудиофайла, по умолчанию True
        :type inWaitCallbackChunkBool: bool, опционально
        :param inWaitCallbackStopBool: True - ожидать выполнение всех асинхронных callback по завершению записи, по умолчанию True
        :type inWaitCallbackStopBool: bool, опционально
        """
        self.mCaptureThread.join()
        if inWaitCallbackChunkBool==True:
            for lItemThread in self.mCallbackChunkDefThreadList:
                if lItemThread.is_alive(): lItemThread.join()
            self.mCallbackChunkDefThreadList = []
        if inWaitCallbackStopBool==True:
            for lItemThread in self.mCallbackStopDefThreadList:
                if lItemThread.is_alive(): lItemThread.join()
            self.mCallbackStopDefThreadList = []

    def CaptureStop(self, inWaitStream=True, inExtra=None):
        """L-,W+: Остановить захват аудио

        .. code-block:: python
            from pyOpenRPA.Robot import Audio
            lRec = Audio.Recorder()
            lRec.CaptureStart(inFileNameStr = "out", inFileFormatStr = "mp3", inDurationSecFloat = None, inChunkSecFloat = 5.0)
            lRec.CaptureStop()

        :param inWaitStream: True - выполнить ожидание окончания потока захвата перед окончанием, по умолчанию True
        :type inWaitStream: bool, опционально
        :param inExtra: Дополнительный контент, необходимый для идентификации файла. В дальнейшем получить структуру можно с помощью функции FileInfoGet()['Extra'], по умолчанию None
        :type inExtra: any, опционально
        """
        self.mCaptureBool=False
        self.mStream.stop_stream()
        if inWaitStream == True: self.mCaptureThread.join()
        self.mStream.close()
        #Close module
        self.mAudio.terminate()
        lFileNameStr = self.CaptureChunk(inExtra=inExtra, inForceChunkBool=False)
        self.mStatusStr = "0_READY"
        if self.mCallbackStopDef != None:
            lCallbackThread = threading.Thread(target=self.mCallbackStopDef,args=[self, lFileNameStr], daemon = True)
            lCallbackThread.start()
            self.mCallbackStopDefThreadList.append(lCallbackThread)
        
        
    def CaptureChunk(self, inExtra=None, inForceChunkBool=True, inShiftSecFloat = 0.0):
        """L-,W+: Зафиксировать захват аудио в виде промежуточного файла вида: <имя файла>_00000.mp3

        .. code-block:: python
            from pyOpenRPA.Robot import Audio
            lRec = Audio.Recorder()
            lRec.CaptureStart(inFileNameStr = "out", inFileFormatStr = "mp3", inDurationSecFloat = None, inChunkSecFloat = 5.0)
            lRec.CaptureChunk()

        :param inExtra: Дополнительный контент, необходимый для идентификации файла. В дальнейшем получить структуру можно с помощью функции FileInfoGet()['Extra'], по умолчанию None
        :type inExtra: any, опционально
        :param inForceChunkBool: True - вне зависимости от текущего режима перейти на режим сохранения по частям, по умолчанию True
        :type inForceChunkBool: bool, опционально
        :param inShiftSecFloat: Последние секунды, которые не записывать в промежуточный аудиофайл. Они будут началом следующего аудио отрывка, по умолчанию 0.0
        :type inShiftSecFloat: float
        :return: Наименование сохраненного аудиофайла
        :rtype: str
        """
        if inForceChunkBool==True and self.mFileAvailableChunkInt==None: self.mFileAvailableChunkInt=0
        lFileNameStr = self.mFileNameStr
        if self.mFileAvailableChunkInt!=None: 
            lFileNameStr+=f"_{self.mFileAvailableChunkInt:05}"
            self.mFileAvailableChunkInt = self.mFileAvailableChunkInt + 1
        lFileNameWExtStr = f"{lFileNameStr}.{self.mFileFormatStr}"
        lFilePathStr = os.path.abspath(os.path.join(self.mFolderPathStr,lFileNameWExtStr))
        lDataFrameBytes = b''.join(self.mRecordedFramesList)
        if inShiftSecFloat != 0.0: 
            lFrameLenInt = int(self.mSampleSizeInt*inShiftSecFloat*self.mChannelCountInt*self.mSampleRateInt)
            lFrameLenInt = int(lFrameLenInt // (self.mChannelCountInt * self.mSampleSizeInt)) * (self.mChannelCountInt * self.mSampleSizeInt)
            if lFrameLenInt<len(lDataFrameBytes): 
                self.mRecordedFramesList=[lDataFrameBytes[-lFrameLenInt:]]
                lDataFrameBytes = lDataFrameBytes[:-lFrameLenInt]
            else:
                lDataFrameBytes=b""
        else:
            self.mRecordedFramesList = []
        # Advanced usage, if you have raw audio data:
        sound = AudioSegment(
            # raw audio data (bytes)
            data=lDataFrameBytes,
            # 2 byte (16 bit) samples
            sample_width=self.mSampleSizeInt,
            # 44.1 kHz frame rate
            frame_rate=self.mSampleRateInt,
            # stereo
            channels=self.mChannelCountInt
        )
        lTimeSecFloat = time.time() - inShiftSecFloat
        if not os.path.exists(os.path.abspath(self.mFolderPathStr)):
            os.mkdir(self.mFolderPathStr)
        sound.export(lFilePathStr, format=f"{self.mFileFormatStr}")
        self.mFileNameList.append(lFileNameWExtStr)
        self.mFileInfoDict[lFileNameWExtStr]= {
            "StartSecFloat": self.mStartChunkSecFloat, 
            "EndSecFloat": lTimeSecFloat, 
            "Extra": inExtra, 
            "PathStr": lFilePathStr 
        }
        if self.mCallbackChunkDef != None and self.mFileAvailableChunkInt!=None:
            lCallbackThread = threading.Thread(target=self.mCallbackChunkDef,args=[self, lFileNameWExtStr], daemon = True)
            lCallbackThread.start()
            self.mCallbackChunkDefThreadList.append(lCallbackThread)
        self.mStartChunkSecFloat = lTimeSecFloat
        return lFileNameWExtStr

    def FileInfoGet(self, inFileNameStr=None):
        """L-,W+: Вернуть информацию по аудиофайлу inFileNameStr. Если inFileNameStr == None -> Функция вернет информацию по последнему записанному файлу

        .. code-block:: python
            from pyOpenRPA.Robot import Audio
            lRec = Audio.Recorder()
            lRec.CaptureStart(inFileNameStr = "out", inFileFormatStr = "mp3", inDurationSecFloat = None, inChunkSecFloat = 5.0)
            lRec.CaptureChunk()
            lFileInfoDict = lRec.FileInfoGet()

        :param inFileNameStr: Наименование аудиофайла с указанием расширения, по умолчанию None (взять последний записанный файл)
        :type inFileNameStr: str, опционально
        :return: {StartSecFloat:, EndSecFloat:, Extra:, PathStr:, } или None
        :rtype: dict
        """
        if inFileNameStr == None: inFileNameStr = self.FileLastGet()
        return self.mFileInfoDict.get(inFileNameStr, None)

    def FileListGet(self):
        """L-,W+: Вернуть список сохраненных аудиофайлов (наименования)

        .. code-block:: python
            from pyOpenRPA.Robot import Audio
            lRec = Audio.Recorder()
            lRec.CaptureStart(inFileNameStr = "out", inFileFormatStr = "mp3", inDurationSecFloat = None, inChunkSecFloat = 5.0)
            lRec.CaptureChunk()
            lRec.CaptureChunk()
            lRec.FileListGet()

        :return: ["out_00000.mp3", "out_00001.mp3", ...]
        :rtype: list
        """
        return self.mFileNameList

    def FileLastGet(self):
        """L-,W+: Вернуть наименование последнего сохраненного аудиофайла

        .. code-block:: python
            from pyOpenRPA.Robot import Audio
            lRec = Audio.Recorder()
            lRec.CaptureStart(inFileNameStr = "out", inFileFormatStr = "mp3", inDurationSecFloat = None, inChunkSecFloat = 5.0)
            lRec.CaptureChunk()
            lRec.CaptureChunk()
            lRec.FileListGet()

        :return: ["out_00000.mp3", "out_00001.mp3", ...]
        :rtype: list
        """
        return self.mFileNameList[-1]
    
    #def IsSilent(self, inLastSecFloat=None):
    #    "Returns 'True' if below the 'silent' threshold"
    #    self.mSilentLastCheckTimeFloat = time.time()
    #    if inLastSecFloat == None: inLastSecFloat = self.mChunkSilentSecFloat
    #    lFrameLenInt = int(self.mSampleSizeInt*inLastSecFloat)
    #    if lFrameLenInt<len(self.mRecordedFramesList): lData = self.mRecordedFramesList[-lFrameLenInt:]
    #    else: lData = self.mRecordedFramesList
    #    return max(lData) < self.mThresholdInt
    
    def __TriggerCheck__(self):
        """Контроль записи / остановки аудио по следующим критериям: 
        - Общая длительность, 
        - Максимальная длительность части, 
        - Максимальная длит тишины (часть), 
        - Максимальная длительность тишины (остановка), 
        """
        # Проверка по длине записи (CHUNK)
        if self.mChunkSecFloat != None and time.time() - self.mStartChunkSecFloat > self.mChunkSecFloat: self.CaptureChunk()
        # Остановка записи по максимальной длине
        if self.mDurationSecFloat != None and time.time() - self.mStartSecFloat > self.mDurationSecFloat: self.CaptureStop(inWaitStream=False)
        # Проверка тишины
        #if self.mChunkSilentSecFloat != None and time.time() - self.mSilentLastCheckTimeFloat and self.IsSilent(): self.mT.append("ТИШИНА!!")

        
