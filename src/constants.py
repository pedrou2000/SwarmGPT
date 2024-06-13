import os 

# GPT Constants
MODEL_VERSION = 3
TEMPERATURE = 1
MODEL_MAP = {
    3: "gpt-3.5-turbo",
    4:  "gpt-4-turbo"
}
DEBUG = False

DEFAULT_SYSTEM_MESSAGE = "You are a helpful assistant."
DEFAULT_TEMPERATURE = 1
DEFAULT_MODEL = 3

# Epub Parser Constants 
MARKDOWN_OUTPUT_MAX_LEN = 1000
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
BOOKS_DIR = os.path.join(DATA_DIR, "books")
PARSED_DIR = os.path.join(DATA_DIR, "parsed_epubs")
ENV_FILE_PATH = os.path.join(ROOT_DIR, ".env")

# Epub Summarizer Constants
NUM_CHAPTERS_SUMMARIZED = 5
NUM_PARAGRAPHS_FINAL_SUMMARY = 9
EPUB_NAME = "eat_that_frog"
EPUB_FILE_PATH = f"{BOOKS_DIR}/{EPUB_NAME}.epub"
SKIP_TITLES = ['Cover', 'Title', 'Copyright', 'Dedication', 'Contents', 'Preface', 'Notes', 'Index', 'Learning Resources', 'About']

# Book Summarizer Prompts
PROMPT_CHAPTER_SUMMARIZER = "You are GPT agent in a system trying to summarize complete books. Your goal is to produce a chapter summary which \
    will then be integrated with the output of other agents who have summarized their own chapter. Extract and convey the core ideas \
    of the chapter in a concise and structured manner, without introductions or conclusions, ideally within three paragraphs."

PROMPT_SUPERVISOR = "You have been given summaries of individual chapters. Your task is to integrate these into a cohesive summary of the \
    entire book without redundancy, ensuring it's concise and captures the book's essence. The final summary be \
    " + str(NUM_PARAGRAPHS_FINAL_SUMMARY) + " paragraphs long."

print("ROOT_DIR: ", BOOKS_DIR)