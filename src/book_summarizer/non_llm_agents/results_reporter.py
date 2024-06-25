import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import constants, json
from data_classes.book_summarizer_state import BookSummarizerState

class AgentResultsReporter():
    def __call__(self, state: BookSummarizerState) -> BookSummarizerState:
        print("State: ", state, "\n SHOWING RESULTS") if state.verbose == 1 else None
        for i, response in enumerate(state.chapter_summaries):
            print("Chapter: ", response.chapter.title)
            print("Summary: ", response.chapter_summary)
            print("\n\n")
        
        content = {state.book_name.replace(" ", "_"): state.final_summary}
        # Save the dictionary to a JSON file
        os.makedirs(constants.FINAL_BOOK_SUMMARY_DIR, exist_ok=True)

        with open(constants.FINAL_BOOK_SUMMARY_PATH, 'w') as json_file:
            json.dump(content, json_file, indent=4)

        print("\n\nFinal Summary: ", state.final_summary)