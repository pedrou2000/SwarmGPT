import os 


# GPT Constants
MODEL_VERSION = 4
MODEL_MAP = {
    # 3: "gpt-3.5-turbo",
    3: "gpt-4o-mini",
    # 4:  "gpt-4-1106-preview"
    # 4: "gpt-4-turbo"
    4: "gpt-4o"
}
MODEL_NAME = MODEL_MAP[MODEL_VERSION]
TEMPERATURE = 1

MARKDOWN_OUTPUT_MAX_LEN = 1000
DEFAULT_SYSTEM_MESSAGE = "You are a helpful assistant."
DEFAULT_TEMPERATURE = 1
DEFAULT_MODEL = 3

# Epub Summarizer Constants
BOOK_NAME = "eat_that_frog"
# BOOK_NAME = "reminiscences-of-pioneer-days-in-st-paul"
# BOOK_NAME = "siddhartha"
# BOOK_NAME = "a_brief_history_of_time"
# BOOK_NAME = "ai"
NUM_CHAPTERS_TO_SUMMARIZE = None
VERBOSE = 1

# Directories
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_FILE_PATH = os.path.join(ROOT_DIR, ".env")
DATA_DIR = os.path.join(ROOT_DIR, "data")
RESULTS_DIR = os.path.join(ROOT_DIR, "results/")
BENCHMARKS_DIR = os.path.join(DATA_DIR, "datasets/")

# Code Generation Directories
HUMAN_EVAL_DIR = RESULTS_DIR + "human_eval/" + MODEL_NAME + "/"
HUMAN_EVAL_SINGLE_AGENT_DIR = HUMAN_EVAL_DIR + "single_agent/"
HUMAN_EVAL_AGENT_CODER_DIR = HUMAN_EVAL_DIR + "agent_coder/"
HUMAN_EVAL_AGENT_CODER_PLUS_DIR = HUMAN_EVAL_DIR + "agent_coder_plus/"

# Math Problem Solver Directories
MATH_DATASET_DIR = os.path.join(BENCHMARKS_DIR, "MATH/test/")

# Epub Summarizer Directories
BOOKS_DIR = os.path.join(DATA_DIR, "books/")
PARSED_BOOKS_DIR = os.path.join(DATA_DIR, "parsed_epubs/")
FULL_CONTENT_PARSED_BOOKS_DIR = os.path.join(DATA_DIR, "full_content_parsed_epubs/")
BOOK_SUMMARIES_DIR = os.path.join(RESULTS_DIR, "book_summaries/")
BOOOOKSCORE_DIR = os.path.join(RESULTS_DIR, "booookscore/")
BOOOOKSCORE_RESULTS_DIR = os.path.join(BOOOOKSCORE_DIR, MODEL_NAME + "/" + BOOK_NAME + "/")
FINAL_BOOK_SUMMARY_DIR = os.path.join(BOOK_SUMMARIES_DIR, MODEL_NAME + "/")
FINAL_BOOK_SUMMARY_PATH = FINAL_BOOK_SUMMARY_DIR + BOOK_NAME + ".json"
BOOK_PATH = BOOKS_DIR + BOOK_NAME + ".epub"
