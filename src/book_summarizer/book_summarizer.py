from epub_parser import EPUB
from gpt_agent import GPTAgent
from concurrent.futures import ThreadPoolExecutor
import os, sys 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import constants

class BookSummarizer:

    def __init__(self, epub_file_path, agent_version, skip_titles, system_message, temperature, debug):
        self.epub = EPUB(epub_file_path)
        self.agent_config = {
            'version': agent_version,
            'debug': debug,
            'system_message': system_message,
            'temperature': temperature
        }
        self.skip_titles = skip_titles

    def should_skip(self, title):
        return any(title.startswith(skip_title) for skip_title in self.skip_titles)

    def _process_chapter(self, node):
        agent = GPTAgent(**self.agent_config)
        print('Processing:', node.title)
        print('Length of content:', len(node.content))
        return node.title, agent.simple_query(node.content)

    def summarize_chapters_sequential(self, num_chapters=None):
        chapter_summaries = {}
        processed_chapters = 0
        for node in self.epub.root_node.children:
            if self.should_skip(node.title):
                continue

            if num_chapters and processed_chapters >= num_chapters:
                break

            chapter, summary = self._process_chapter(node)
            chapter_summaries[chapter] = summary
            processed_chapters += 1

        return chapter_summaries

    def summarize_chapters_parallel(self, num_chapters=None, max_workers=5):
        chapter_summaries = {}
        nodes_to_process = [node for node in self.epub.root_node.children if not self.should_skip(node.title)]
        
        if num_chapters:
            nodes_to_process = nodes_to_process[:num_chapters]

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(self._process_chapter, nodes_to_process))
        
        for chapter, summary in results:
            chapter_summaries[chapter] = summary
        
        return chapter_summaries

    def integrate_summaries(self, chapter_summaries, supervisor_message):
        aggregated_summary = "\n\n".join(chapter_summaries.values())
        
        supervisor_agent_config = self.agent_config.copy()
        supervisor_agent_config["system_message"] = supervisor_message

        supervisor_agent = GPTAgent(**supervisor_agent_config)
        final_summary = supervisor_agent.simple_query(aggregated_summary)
        
        return final_summary


def summarize_complete_book(summarizer):
    agent = GPTAgent(**summarizer.agent_config)

    all_text = 'You are an expert summarizer. Summarize this book in 12 paragraphs giving me the most important and key ideas: \n\n\n'
    for node in summarizer.epub.root_node.children:
        all_text += node.content 

    response = agent.simple_query(all_text)
    print(response)

    file_name = 'response_script.txt'
    # Write the response to a text file
    with open(file_name, 'w') as file:
        file.write(response)

def summarize_chapters_separately(summarizer, num_chapters):
    
    summaries = summarizer.summarize_chapters_parallel(num_chapters=num_chapters)  
    
    for chapter, summary in summaries.items():
        print(f"\nChapter: {chapter}")
        print("--------------------------")
        print(summary)
        print("==========================")
    
    print("\nIntegrated Summary:")
    print("====================")
    
    final_summary = summarizer.integrate_summaries(summaries, constants.PROMPT_SUPERVISOR)
    print(final_summary)

if __name__ == "__main__":
    summarizer = BookSummarizer(
        epub_file_path=constants.EPUB_FILE_PATH,
        agent_version=constants.MODEL_VERSION,
        skip_titles=constants.SKIP_TITLES,
        system_message=constants.PROMPT_CHAPTER_SUMMARIZER,
        temperature=constants.TEMPERATURE,
        debug=constants.DEBUG
    )
    # summarize_complete_book(summarizer)
    summarize_chapters_separately(summarizer, constants.NUM_CHAPTERS_SUMMARIZED)
