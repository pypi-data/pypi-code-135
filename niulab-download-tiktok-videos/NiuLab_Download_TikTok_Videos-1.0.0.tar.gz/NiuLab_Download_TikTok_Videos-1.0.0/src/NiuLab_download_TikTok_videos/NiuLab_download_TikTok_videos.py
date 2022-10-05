import os
import pandas
from TikTokApi import TikTokApi


# from download_youtube_clips import main
failed=[]

def video_processing(VIDEO_ID, OUTPUT_DIRECTORY):
    video_id = VIDEO_ID
    output_directory = OUTPUT_DIRECTORY
    os.chdir(output_directory)
    with TikTokApi() as api:
        video_content = api.video(id=video_id).bytes()
    with open(video_id+".mp4", "wb") as out:
        out.write(video_content)


def read_xlsx_file(FILE_LOCATION):
    column_a = pandas.read_excel(FILE_LOCATION, usecols="A")
    return column_a


def tiktok_download(FILE_LOCATION, OUTPUT_DIRECTORY):
    column_a = read_xlsx_file(FILE_LOCATION)
    #index has 0...n and row contains video_id
    for index, row in column_a.iterrows():
        video_id=str(row['video_id'])
        print("***************************************************")
        print("Processing video with ID: "+video_id)
        try:
            video_processing(video_id, OUTPUT_DIRECTORY)
            print("Success video with ID: " + video_id)
        except:
            print("Failed")
            failed.append(video_id)
            continue

    print("***************************************************")
    print("FAILED: "+' '.join(failed))
