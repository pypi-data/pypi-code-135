import logging
from pathlib import Path
import sys
import time

from ftp_receiver.config import Config
from ftp_receiver.ftp_client import FTPClient
from ftp_receiver.publisher import KafkaPublisher


def main() -> None:
    config = Config()
    logging.basicConfig(stream=sys.stdout, level=config.log.level)
    publisher = KafkaPublisher(config=config)
    interval = config.download.interval_seconds
    while True:  # noqa: WPS457 infinite-while-loop
        logging.info(f"Running FTP Receiver v{config.version}")
        run(config=config, publisher=publisher)
        logging.info(f"Run completed, sleeping for {interval} seconds")
        time.sleep(interval)


def run(config: Config, publisher: KafkaPublisher) -> None:
    client = FTPClient(config=config)
    downloaded = filenames(output=config.download.directory)
    for filename in sorted(client.list()):
        if filename in downloaded:
            continue
        client.download(filename=filename)
        publisher.publish(filename=filename)
    client.quit()


def filenames(output: Path) -> set[str]:
    return {filepath.name for filepath in output.iterdir()}


if __name__ == "__main__":
    main()
