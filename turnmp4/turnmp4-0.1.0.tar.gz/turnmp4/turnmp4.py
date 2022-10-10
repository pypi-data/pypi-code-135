import click
import glob
from shutil import copytree, ignore_patterns, copy, rmtree
import os
from pathlib import Path


@click.group()
def cli():
    pass


@cli.command()
def merge():
    '''
    将文件夹中的mp4文件合并，在合并前请先确认txt中的文件顺序
    '''
    if not Path('确认完毕后将文件名改为a.txt').exists():
        rmtree('out_dir', ignore_errors=True)
        os.mkdir('out_dir')
        mp4_list = glob.glob("*.mp4")
        for i in mp4_list:
            copy(i, 'out_dir')
        mp4_list = [f"file 'out_dir/{i}'" for i in mp4_list]
        final_list = '\n'.join(mp4_list)
        click.echo('确认完毕后将out.txt复制，并修改名为a.txt')
        with open('out.txt', 'w', encoding='utf-8') as file:
            file.write(final_list)

    if Path('a.txt').exists():
        cmd = os.popen(
            'ffmpeg -y -f concat -safe 0 -i a.txt -c copy output.mp4')
        data = cmd.read()
        cmd.close()
        rmtree('out_dir', ignore_errors=True)
        os.remove('a.txt')
        os.remove('out.txt')


@cli.command()
def dropdb():
    '''
    删除数据库
    :return:
    '''
    click.echo('Dropped the database')


if __name__ == '__main__':
    cli()
