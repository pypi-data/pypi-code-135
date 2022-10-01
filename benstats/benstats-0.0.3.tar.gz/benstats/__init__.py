# SPDX-FileCopyrightText: 2022-present gv-sh <gv-sh@outlook.com>
#
# SPDX-License-Identifier: MIT

import os 
import cv2 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ls              = lambda dir        : [i for i in os.listdir(dir) if os.path.isfile(os.path.join(dir, i))]
read            = lambda dir, f     : cv2.imread(os.path.join(dir, f))

resize          = lambda M, s       : cv2.resize(M, (0, 0), fx=s, fy=s, interpolation=cv2.INTER_AREA)

itp             = lambda M, x, y    : np.interp(np.array(M), (M.min(), M.max()), (x, y)).astype(np.uint8)

first           = lambda x          : int(str(x)[0])
firsts          = lambda M          : np.array([first(i) for i in M.flatten()])
count           = lambda M, i       : len([j for j in M if j == i])
counts          = lambda M          : {str(i): count(M, i) for i in range(1, 10)}

prob            = lambda M, i       : M[i] / sum(M.values())
probs           = lambda M          : {str(i): 100*prob(M, str(i)) for i in range(1, 10)}
ben             = lambda            : {str(i): np.log10(1 + 1/i) * 100 for i in range(1, 10)}

write           = lambda D, fp      : pd.DataFrame(D).to_csv(fp, index=False)

log             = lambda msg        : print(msg, end='\r', flush=True)


def load_images(dir, fmts):
    """ Load all the images available in the given directory

        @param dir: Directory containing the images 
        @param fmts: List of image formats to load

        @return List of images
    """
    files = ls(dir)
    images = []

    for f in files:
        if f.split('.')[-1] in fmts:
            try: 
                img = read(dir, f)
                if img is not None:
                    images.append(img)
                else: 
                    raise NameError('UnsupportedImageFormat')
            except NameError as e:
                print(e)
                continue

    return images

def split(img, channels=['rgb'], scale=1, min=0, max=255):
    """ Split the image into its channels

        @param img: Image to split

        @return List of channels
    """
    data = {}

    if 'rgb' in channels:
        img_rgb = resize(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), scale)
        data['rgb'] = img_rgb
        data['rgb'] = {
            'r': itp(img_rgb[:, :, 0], min, max),
            'g': itp(img_rgb[:, :, 1], min, max),
            'b': itp(img_rgb[:, :, 2], min, max)
        }
    if 'hsv' in channels:
        img_hsv = resize(cv2.cvtColor(img, cv2.COLOR_BGR2HSV), scale)
        data['hsv'] = {
            'h': itp(img_hsv[:, :, 0], min, max),
            's': itp(img_hsv[:, :, 1], min, max),
            'v': itp(img_hsv[:, :, 2], min, max)
        }
    if 'gray' in channels:
        img_gray = resize(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), scale)
        data['gray'] = itp(img_gray, min, max)
        data['gray'] = {
            'gray': itp(img_gray, min, max)
        }
    if 'lab' in channels:
        img_lab = resize(cv2.cvtColor(img, cv2.COLOR_BGR2LAB), scale)
        data['lab'] = {
            'l': itp(img_lab[:, :, 0], min, max),
            'a': itp(img_lab[:, :, 1], min, max),
            'b': itp(img_lab[:, :, 2], min, max)
        }
    if 'luv' in channels:
        img_luv = resize(cv2.cvtColor(img, cv2.COLOR_BGR2LUV), scale)
        data['luv'] = {
            'l': itp(img_luv[:, :, 0], min, max),
            'u': itp(img_luv[:, :, 1], min, max),
            'v': itp(img_luv[:, :, 2], min, max)
        }
    if 'xyz' in channels:
        img_xyz = resize(cv2.cvtColor(img, cv2.COLOR_BGR2XYZ), scale)
        data['xyz'] = {
            'x': itp(img_xyz[:, :, 0], min, max),
            'y': itp(img_xyz[:, :, 1], min, max),
            'z': itp(img_xyz[:, :, 2], min, max)
        }
    if 'ycrcb' in channels:
        img_ycrcb = resize(cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb), scale)
        data['ycrcb'] = {
            'y': itp(img_ycrcb[:, :, 0], min, max),
            'cr': itp(img_ycrcb[:, :, 1], min, max),
            'cb': itp(img_ycrcb[:, :, 2], min, max)
        }

    return data

def benstats(img, channels=['rgb'], scale=1, min=0, max=255):
    """ Calculate the Benford's Law statistics for the image

        @param img: Image to calculate the statistics for

        @return Dictionary of statistics
    """
    data = split(img, channels=channels, scale=scale, min=min, max=max)
    stats = {}

    if 'rgb' in channels:
        stats['rgb'] = {
            'r': {
                'counts'    : counts(firsts(data['rgb']['r'])),
                'probs'     : probs(counts(firsts(data['rgb']['r']))),
            },
            'g': {
                'counts'    : counts(firsts(data['rgb']['g'])),
                'probs'     : probs(counts(firsts(data['rgb']['g']))),
            },
            'b': {
                'counts'    : counts(firsts(data['rgb']['b'])),
                'probs'     : probs(counts(firsts(data['rgb']['b']))),
            }
        }
    if 'hsv' in channels:
        stats['hsv'] = {
            'h': {
                'counts'    : counts(firsts(data['hsv']['h'])),
                'probs'     : probs(counts(firsts(data['hsv']['h']))),
            },
            's': {
                'counts'    : counts(firsts(data['hsv']['s'])),
                'probs'     : probs(counts(firsts(data['hsv']['s']))),
            },
            'v': {
                'counts'    : counts(firsts(data['hsv']['v'])),
                'probs'     : probs(counts(firsts(data['hsv']['v']))),
            }
        }
    if 'gray' in channels:
        stats['gray'] = {
            'gray': {
                'counts'    : counts(firsts(data['gray']['gray'])),
                'probs'     : probs(counts(firsts(data['gray']['gray']))),
            }
        }
    if 'lab' in channels:
        stats['lab'] = {
            'l': {
                'counts'    : counts(firsts(data['lab']['l'])),
                'probs'     : probs(counts(firsts(data['lab']['l']))),
            },
            'a': {
                'counts'    : counts(firsts(data['lab']['a'])),
                'probs'     : probs(counts(firsts(data['lab']['a']))),
            },
            'b': {
                'counts'    : counts(firsts(data['lab']['b'])),
                'probs'     : probs(counts(firsts(data['lab']['b']))),
            }
        }
    if 'luv' in channels:
        stats['luv'] = {
            'l': {
                'counts'    : counts(firsts(data['luv']['l'])),
                'probs'     : probs(counts(firsts(data['luv']['l']))),
            },
            'u': {
                'counts'    : counts(firsts(data['luv']['u'])),
                'probs'     : probs(counts(firsts(data['luv']['u']))),
            },
            'v': {
                'counts'    : counts(firsts(data['luv']['v'])),
                'probs'     : probs(counts(firsts(data['luv']['v']))),
            }
        }
    if 'xyz' in channels:
        stats['xyz'] = {
            'x': {
                'counts'    : counts(firsts(data['xyz']['x'])),
                'probs'     : probs(counts(firsts(data['xyz']['x']))),
            },
            'y': {
                'counts'    : counts(firsts(data['xyz']['y'])),
                'probs'     : probs(counts(firsts(data['xyz']['y']))),
            },
            'z': {
                'counts'    : counts(firsts(data['xyz']['z'])),
                'probs'     : probs(counts(firsts(data['xyz']['z']))),
            }
        }
    if 'ycrcb' in channels:
        stats['ycrcb'] = {
            'y': {
                'counts'    : counts(firsts(data['ycrcb']['y'])),
                'probs'     : probs(counts(firsts(data['ycrcb']['y']))),
            },
            'cr': {
                'counts'    : counts(firsts(data['ycrcb']['cr'])),
                'probs'     : probs(counts(firsts(data['ycrcb']['cr']))),
            },
            'cb': {
                'counts'    : counts(firsts(data['ycrcb']['cb'])),
                'probs'     : probs(counts(firsts(data['ycrcb']['cb']))),
            }
        }

    return stats

def benplot(img, channels=['rgb'], scale=1, min=0, max=255):
    stats = benstats(img, channels=channels, scale=scale, min=min, max=max)

    # Make two plots side by side
    fig, axes = plt.subplots(1, 2, figsize=(15, 5), gridspec_kw={'width_ratios': [1, 1]})

    fig.tight_layout()

    axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axes[0].set_title('Image')

    axes[1].bar(range(1, 10), [100*np.log10(1 + 1/d) for d in range(1, 10)], color='gainsboro', label='Benford\'s Law')
    axes[1].grid(axis='both', alpha=0.75)
    
    if 'rgb' in channels:
        axes[1].plot(range(1, 10), stats['rgb']['r']['probs'].values(), 'r-', label='RGB-Red')
        axes[1].plot(range(1, 10), stats['rgb']['g']['probs'].values(), 'g-', label='RGB-Green')
        axes[1].plot(range(1, 10), stats['rgb']['b']['probs'].values(), 'b-', label='RGB-Blue')
    
    if 'hsv' in channels:
        axes[1].plot(range(1, 10), stats['hsv']['h']['probs'].values(), 'k-', label='HSV-Hue')
        axes[1].plot(range(1, 10), stats['hsv']['s']['probs'].values(), 'k--', label='HSV-Saturation')
        axes[1].plot(range(1, 10), stats['hsv']['v']['probs'].values(), 'k:', label='HSV-Value')
    
    if 'gray' in channels:
        axes[1].plot(range(1, 10), stats['gray']['gray']['probs'].values(), '-', color='gray', label='Gray')
    
    if 'lab' in channels:
        axes[1].plot(range(1, 10), stats['lab']['l']['probs'].values(), 'c-.', label='LAB-L')
        axes[1].plot(range(1, 10), stats['lab']['a']['probs'].values(), 'c--', label='LAB-A')
        axes[1].plot(range(1, 10), stats['lab']['b']['probs'].values(), 'c:', label='LAB-B')
    
    if 'luv' in channels:
        axes[1].plot(range(1, 10), stats['luv']['l']['probs'].values(), 'm-.', label='LUV-L')
        axes[1].plot(range(1, 10), stats['luv']['u']['probs'].values(), 'm--', label='LUV-U')
        axes[1].plot(range(1, 10), stats['luv']['v']['probs'].values(), 'm:', label='LUV-V')

    if 'xyz' in channels:
        axes[1].plot(range(1, 10), stats['xyz']['x']['probs'].values(), 'y-.', label='XYZ-X')
        axes[1].plot(range(1, 10), stats['xyz']['y']['probs'].values(), 'y--', label='XYZ-Y')
        axes[1].plot(range(1, 10), stats['xyz']['z']['probs'].values(), 'y:', label='XYZ-Z')
    
    if 'ycrcb' in channels:
        axes[1].plot(range(1, 10), stats['ycrcb']['y']['probs'].values(), 'r-.', label='YCrCb-Y')
        axes[1].plot(range(1, 10), stats['ycrcb']['cr']['probs'].values(), 'r--', label='YCrCb-Cr')
        axes[1].plot(range(1, 10), stats['ycrcb']['cb']['probs'].values(), 'r:', label='YCrCb-Cb')

    axes[1].set_title('Comparison with Benford\'s Law')
    axes[1].set_xlabel('Digit')
    axes[1].set_ylabel('Probability(%)')
    axes[1].set_xticks(range(1, 10))
    axes[1].legend(loc='upper right')

    plt.show()    

