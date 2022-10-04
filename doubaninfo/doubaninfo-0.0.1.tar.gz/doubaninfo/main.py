from doubaninfo.doubaninfo import *

def main():
    args = readargs()
    if args.cookie:
        getdoubaninfo(url=args.url,cookie=args.cookie)
    else:
        getdoubaninfo(url=args.url)


if __name__ == '__main__':
    main()