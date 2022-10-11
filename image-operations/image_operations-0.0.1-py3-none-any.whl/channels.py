from PIL import Image

def channels(path,channel):
    
    pic = Image.open(path)
    
    #spliting image channels
    red, green, blue = pic.split()
    
    if channel == "green":
        ch = green
    elif channel == "blue":
        ch = blue
    elif channel == "red":
        ch = red          
    else:
        return print(f"Error: {channel} is Invalid channel. Try 'green', 'blue' or 'red'")
    
    #match the original image and its channel    
    match = Image.new('RGB', (pic.width + ch.width, pic.height))
    match.paste(pic, (0, 0))
    match.paste(ch, (pic.width, 0))
    return match
