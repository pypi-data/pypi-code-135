#
# pymax_c_major_scale.py
# by Daniel Brown - daniel@intelligentmusicsystems.com
#
# An example of using the pymax system.
# Use with the Max patch "pymax_c_major_scale.maxpat"


def c_major_scale_loop():

    c_major_scale   = [60, 62, 64, 65, 67, 69, 71, 72]    
    ontime          = 0.0
    i               = 0

    while True:

        yield [ontime, c_major_scale[i]]

        i       = (i + 1) % len(c_major_scale)
        ontime  += .5


if __name__ == "__main__":

    from pymaxmusic import pymax

    pymax.open_pymax()
    pymax.add_generator("c_maj_loop", c_major_scale_loop)
    pymax.run_pymax()