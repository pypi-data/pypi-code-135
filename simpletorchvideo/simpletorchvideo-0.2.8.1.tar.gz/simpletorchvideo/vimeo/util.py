import os

def parse_video_list_from_image_list(image_list: [str], frame_pad=None) -> [[str]]:
    """_summary_

    Args:
        image_list (str]): _description_
        frame_pad (_type_, optional): _description_. Defaults to None.

    Returns:
        [[str]]: 2D array containing different images in different fragments
                 if frame_pad is None ,then fragments is set as vimeo's folder name e.g. 00001/XXXX/im%d.png
                 which may contain different number of 7-pictures group.
                 if frame_pad is set, each fragment group contains n-pictures, where n is frame_pad
    """
    video_last = ''
    video_list = []
    if frame_pad is None:
        for path in sorted(image_list):
            video = os.path.dirname(os.path.dirname(path))
            if not video == video_last:
                video_list.append([])
                video_last = video
            video_list[-1].append(path)
    else:
        idx = 0
        for path in sorted(image_list):
            if idx%frame_pad==0:
                video_list.append([])
            video_list[-1].append(path)
            idx+=1
    return video_list
