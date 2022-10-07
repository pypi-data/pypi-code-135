import getopt
import logging
import os
import sys

from videotools.video_text_clip import VideoTextClipProcessor
from videotools.common import Config, Stopwatch


def usage():
    print('main.py -i <inpath> -o <outpath> -f <inputfile> -d <outputfile>')


def init_logging(config: Config):
    if not os.path.exists(config.log_home):
        os.makedirs(config.log_home)

    logging.basicConfig(
        filename=f"{config.log_home}/videotools.log",
        filemode="a",
        encoding="UTF-8",
        format='%(asctime)s.%(msecs)03d [%(levelname)s] %(thread)s %(name)s - %(message)s',
        datefmt='%m-%d-%Y %I:%M:%S',
        level=logging.INFO,
    )


def process_path(logger,
                 processor: VideoTextClipProcessor,
                 in_path,
                 out_path):
    stopwatch = Stopwatch()
    logger.info(f"Start process with in_path: {in_path}, out_path: {out_path}")

    if not in_path:
        raise Exception(f"in_path: {in_path} not specified")
    if not os.path.exists(in_path):
        raise Exception(f"in_path: {in_path} not exists")
    if not os.path.isdir(in_path):
        raise Exception(f"in_path: {in_path} is not a directory")

    if in_path.endswith('/'):
        in_path = in_path[0:-1]
    if not out_path:
        out_path = f"{in_path}_out"

    try:
        result = processor.process_path(in_path, out_path)
        processor.close()

        logger.info(f"Finished process with in_path: {in_path}, out_path: {out_path}" +
                    f", result: {result}, spends: {stopwatch.stop()}")
    except Exception as ex:
        print(ex)
        logger.exception("Failed to process with in_path: {in_path}, out_path: {out_path}" +
                         f", spends: {stopwatch.stop()}")


def process_file(logger: logging.Logger,
                 processor: VideoTextClipProcessor,
                 in_file: str,
                 dest_file: str):
    stopwatch = Stopwatch()
    logger.info(
        f"Start process with in_file: {in_file}, dest_file: {dest_file}")

    if not in_file or not dest_file:
        raise Exception(
            f"in_file: {in_file} or dest_file: {dest_file} not specified")

    try:
        processor.process_file(in_file, dest_file)
        processor.close()

        logger.info(f"Finished process with in_file: {in_file}, dest_file: {dest_file}" +
                    f", spends: {stopwatch.stop()}")
    except Exception as ex:
        print(ex)
        logger.exception(f"Failed to process with in_file: {in_file}, dest_file: {dest_file}" +
                         f", spends: {stopwatch.stop()}")


def main():
    config = Config()
    init_logging(config)

    logger = logging.getLogger("main")

    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "hi:o:f:d:",
            ["inpath=", "outpath=", "file=", "dest="]
        )
    except getopt.GetoptError as ex:
        print(ex)
        usage()
        sys.exit(2)

    in_path = None
    out_path = None
    in_file = None
    dest_file = None
    for opt, arg in opts:
        if opt in ("-i", "--inpath"):
            in_path = arg
        elif opt in ("-o", "--outpath"):
            out_path = arg
        elif opt in ("-f", "--file"):
            in_file = arg
        elif opt in ("-d", "--dest"):
            dest_file = arg
        elif opt in ("-h"):
            usage()
            return
        else:
            usage()
            raise Exception(f"未识别的命令参数, 参数名: {opt}, arg: {arg}")

    processor = VideoTextClipProcessor(config)
    if in_path:
        process_path(logger, processor, in_path, out_path)
    else:
        process_file(logger, processor, in_file, dest_file)


if __name__ == "__main__":
    sys.argv = sys.argv[1:]
    main()
