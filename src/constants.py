import os 

# Directories
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
BOOKS_DIR = os.path.join(DATA_DIR, "books/")
PARSED_DIR = os.path.join(DATA_DIR, "parsed_epubs/")
ENV_FILE_PATH = os.path.join(ROOT_DIR, ".env")
RESULTS_DIR = os.path.join(ROOT_DIR, "results/")
BOOK_SUMMARIES_DIR = os.path.join(RESULTS_DIR, "book_summaries/")

# GPT Constants
MODEL_VERSION = 3
MODEL_MAP = {
    3: "gpt-3.5-turbo",
    4:  "gpt-4o"
}
MODEL_NAME = MODEL_MAP[MODEL_VERSION]
TEMPERATURE = 1

MARKDOWN_OUTPUT_MAX_LEN = 1000
DEFAULT_SYSTEM_MESSAGE = "You are a helpful assistant."
DEFAULT_TEMPERATURE = 1
DEFAULT_MODEL = 3

# Epub Summarizer Constants
BOOK_NAME = "eat_that_frog"
BOOK_PATH = BOOKS_DIR + BOOK_NAME + ".epub"
NUM_CHAPTERS_TO_SUMMARIZE = 2
VERBOSE = 0
