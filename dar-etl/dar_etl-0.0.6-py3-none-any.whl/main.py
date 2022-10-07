import logging
from pathlib import Path
import sys
from zipfile import ZipFile

from dar_etl.config import Config
from dar_etl.consumer import NewDarFileNotificationConsumer
from dar_etl.parsing.parser_factory import ParserFactory
from dar_etl.publisher import DarEntryPublisher


class DarEtl:
    def __init__(self, config: Config) -> None:
        self.publisher = DarEntryPublisher(config=config)
        self.consumer = NewDarFileNotificationConsumer(config=config)
        self.json_directory = config.app.json_directory
        self.parsers = ParserFactory.create_all()

    def run(self) -> None:
        for filepath in self.consumer.consume():
            json_file = self._unzip(filepath=filepath)
            for parser in self.parsers:
                logging.info(f"[PARSING] {parser.root_key} | {json_file.name}")
                for entry in parser.parse(filepath=json_file):
                    self.publisher.publish(dar_entry=entry, topic=parser.root_key)
            logging.info(f"[COMPLETED] {json_file.name}")
            json_file.unlink()

    def _unzip(self, filepath: Path) -> Path:
        logging.info(f"[EXTRACTING] {filepath.name}")
        member = filepath.name.replace(".zip", ".json")
        with ZipFile(file=filepath, mode="r") as dar_zip_file:
            dar_zip_file.extract(member=member, path=self.json_directory)
        logging.info(f"[EXTRACTED] {filepath.name}")
        return self.json_directory.joinpath(member)


def main() -> None:
    config = Config()
    logging.basicConfig(stream=sys.stdout, level=config.log.level)
    dar_etl = DarEtl(config=config)
    dar_etl.run()


if __name__ == "__main__":
    main()
