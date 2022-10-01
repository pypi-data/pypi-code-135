import sys

from .marcownpack import main


if __name__ == '__main__':
    sys.argv[0] = 'python -m marcownpack'
    sys.exit(main())
