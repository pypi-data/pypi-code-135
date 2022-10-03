import logging

logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="a",
                    format="%(asctime)s [%(levelname)s] [%(name)s] [%(message)s]")

log = logging.getLogger(__name__)

log.debug("debug")
log.info("info")
log.warning("warning")
log.error("error")
log.critical("critical")
