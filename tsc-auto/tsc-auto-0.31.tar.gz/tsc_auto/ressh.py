import argparse
import os
import time


def main():
    parser = argparse.ArgumentParser(description='断线自动重连ssh, 格式: ressh [自带参数] ssh参数',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--tmux', action='store_true', help='是否自动进入tmux')
    parser.add_argument('--try_times', type=int, default=24*3600, help='断线重连接的尝试次数,超过这个次数就不再自动连接')
    parser.add_argument('--interval', type=float, default=1, help='断线重连接的间隔时间,单位秒')
    parser.add_argument('--password', type=str, default=None, help='ssh连接的密码(先正常登录一次)')
    args, cmd_ = parser.parse_known_args()
    # 构建命令
    cmd_ = ['-o ServerAliveInterval=15 -o ServerAliveCountMax=3'] + cmd_
    if args.tmux:
        cmd_ = ['-t -o RemoteCommand="tmux a||~/tmux a||tmux||~/tmux"'] + cmd_
    cmd = 'ssh ' + ' '.join(cmd_)
    if args.password:
        cmd = """expect -c 'spawn {}; expect "*password:"; send "{}\\r"; interact'""".format(cmd, args.password)
    # 循环运行
    for i in range(args.try_times):
        if os.system(cmd):
            print('第{}/{}次中断,{}秒后重新连接...'.format(i+1, args.try_times, args.interval))
            time.sleep(args.interval)
        else:
            break


if __name__ == "__main__":
    main()
