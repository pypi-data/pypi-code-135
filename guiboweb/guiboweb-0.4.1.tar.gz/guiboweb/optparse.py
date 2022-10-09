from optparse import OptionParser
from .guiboweb import add_num

usage1 = 'guiboweb --embed --pwd 1234 image.jpg "watermark text" embed.png'
usage2 = 'guiboweb --extract --pwd 1234 --wm_shape 111 embed.png'
optParser = OptionParser(usage=usage1 + '\n' + usage2)

optParser.add_option('--embed', dest='work_mode', action='store_const', const='embed'
                     , help='Embed watermark into images')
optParser.add_option('--extract', dest='work_mode', action='store_const', const='extract'
                     , help='Extract watermark from images')

optParser.add_option('-p', '--pwd', dest='password', help='password, like 1234')
optParser.add_option('--wm_shape', dest='wm_shape', help='Watermark shape, like 120')

(opts, args) = optParser.parse_args()


def main():
    if opts.work_mode == 'embed':
        if not len(args) == 3:
            print('Error! Usage: ')
            print(usage1)
            return
        else:
            print('Embed succeed! to file ', args[2])
            print('Put down watermark size:', '8899')

    if opts.work_mode == 'extract':
        if not len(args) == 1:
            print('Error! Usage: ')
            print(usage2)
            return

        else:
            print('Extract succeed! watermark is:args[2]')


'''
python -m blind_watermark.cli_tools --embed --pwd 1234 examples/pic/ori_img.jpeg "watermark text" examples/output/embedded.png
python -m blind_watermark.cli_tools --extract --pwd 1234 --wm_shape 111 examples/output/embedded.png


cd examples
blind_watermark --embed --pwd 1234 examples/pic/ori_img.jpeg "watermark text" examples/output/embedded.png
blind_watermark --extract --pwd 1234 --wm_shape 111 examples/output/embedded.png
'''
