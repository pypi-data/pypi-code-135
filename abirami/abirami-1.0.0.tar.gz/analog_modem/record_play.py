import argparse

def initiate():
    print("initiating")
def call(n):
    print("calling**","mobilenumber:",n)

def answer():
    print("answering**")

def record():
    print("recording**")

def play():
    print("playing**")

def close():
    print("closing")


def main():
    parser = argparse.ArgumentParser(prog='gfg',
                                     description='This a voice modem testing script.')


    parser.add_argument('-o', default=False,help="call/answer",required=True)
    parser.add_argument('-number', type=int, nargs='+',
                        help='a mobile number')
    parser.add_argument('-f', help='record/play')

    args = parser.parse_args()
    n=args.number

    if args.o:
        print("Welcome to voice Modem testing !")
        initiate()
        if args.o == "call":
            call(n)

        elif args.o == "answer":
            answer()

    if args.f:
        if args.f == "record":
            record()
        elif args.f == "play":
            play()

    close()

if __name__ == "__main__":
    main()
