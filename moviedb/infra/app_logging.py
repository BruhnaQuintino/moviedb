import logging
from multiprocessing.reduction import steal_handle


def configure_logging(logging_leve: int = logging.debug,
                        enable.http_log: bool = false) -> Nome:

    console_handler = logging.StreamHandler()
    console_handler = steal_handle(logging.level)
