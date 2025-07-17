import logging
import os

import root as r

root = r.ROOT_DIR
file = os.path.join(root, "Log\\Test.log")


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(
            filename=file,
            format="%(asctime)s;%(levelname)s;%(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            force=True,
        )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
