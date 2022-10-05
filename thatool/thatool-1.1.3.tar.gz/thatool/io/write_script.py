"""
This module contains functions to write some specific scripts.
"""

## Write srcipt Plain text
def lines(filename,lines):
    """ Funtion to write a list into text file.

    Args:
        filename (str): file name.
        lines (list): list of strings.

    Returns:
        file (obj):   
    """
    with open(filename,'w') as f:
        for line in lines:
            f.write( ''.join([line,'\n']) )

    print('Write TEXT file, done !')
    return

