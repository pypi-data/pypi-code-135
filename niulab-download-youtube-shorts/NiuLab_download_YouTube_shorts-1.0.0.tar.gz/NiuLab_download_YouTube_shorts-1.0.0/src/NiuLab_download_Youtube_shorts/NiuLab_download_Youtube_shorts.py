import youtube_dl
import pandas
import os

# from download_youtube_clips import main
failed=[]

def video_processing(VIDEO_ID, OUTPUT_DIRECTORY):
    video_id = VIDEO_ID
    output_directory = OUTPUT_DIRECTORY
    os.chdir(output_directory)
    ydl_opts = {'format':'bestvideo[height<=480]'}
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.extract_info(video_id)

def read_xlsx_file(FILE_LOCATION):
    column_a = pandas.read_excel(FILE_LOCATION, usecols="A")
    return column_a


def youtube_download(FILE_LOCATION, OUTPUT_DIRECTORY):
    column_a = read_xlsx_file(FILE_LOCATION)
    #index has 0...n and row contains video_id
    for index, row in column_a.iterrows():
        video_id=row['video_id']
        print("***************************************************")
        print("Processing video with ID: "+video_id)
        try:
            video_processing(video_id, OUTPUT_DIRECTORY)
        except:
            print("Failed")
            failed.append(video_id)
            continue

    print("***************************************************")
    print("FAILED: "+' '.join(failed))
