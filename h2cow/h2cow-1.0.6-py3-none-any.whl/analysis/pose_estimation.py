#from dlclive import DLCLive, Processor
import os
import deeplabcut
#dlc_proc = Processor()

output_path = deeplabcut.DownSampleVideo(os.path.join("C:/Users/danie/Desktop/packaging_tutorial/Data", "mijnkoe.mp4"), width=300)
print(output_path)