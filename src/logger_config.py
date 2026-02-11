# import logging
# import os


# def setup_logger():
#     log_level = os.getenv("LOG_LEVEL", "INFO").upper()

#     numeric_level = getattr(logging, log_level, logging.INFO)

#     logger = logging.getLogger()
#     logger.setLevel(numeric_level)

#     if not logger.handlers:
#         formatter = logging.Formatter(
#             "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
#         )

#         file_handler = logging.FileHandler("app.log")
#         file_handler.setFormatter(formatter)

#         console_handler = logging.StreamHandler()
#         console_handler.setFormatter(formatter)

#         logger.addHandler(file_handler)
#         logger.addHandler(console_handler)

#     return logger
import logging

def setup_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger
