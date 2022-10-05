from doubaninfo.doubaninfo import *

def main():
    args = readargs()
    if args.json:
        if args.cookie:
            getdoubaninfo_json(url=args.url,cookie=args.cookie)
        else:
            getdoubaninfo_json(url=args.url)
    else:
        if args.cookie:
            getdoubaninfo(url=args.url,cookie=args.cookie)
        else:
            getdoubaninfo(url=args.url)


if __name__ == '__main__':
    main()