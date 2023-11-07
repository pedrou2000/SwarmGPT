from epub_parser import EPUB
from gpt_agent import GPTAgent
from concurrent.futures import ThreadPoolExecutor

class BookSummarizer:

    def __init__(self, epub_file_path, agent_version, agent_size, skip_titles, system_message, temperature, debug):
        self.epub = EPUB(epub_file_path)
        self.agent_config = {
            'version': agent_version,
            'size': agent_size,
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


def summarize_complete_book(summarizer, epub_file_path, agent_version, agent_size, skip_titles, system_message, temperature, debug, num_chapters):
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

def summarize_chapters_separately(summarizer, epub_file_path, agent_version, agent_size, skip_titles, system_message, temperature, debug, num_chapters):
    summaries = summarizer.summarize_chapters_parallel(num_chapters=num_chapters)  
    
    for chapter, summary in summaries.items():
        print(f"\nChapter: {chapter}")
        print("--------------------------")
        print(summary)
        print("==========================")
    
    # New code for Phase 2: Supervisor Integration
    final_paragraphs = 9
    supervisor_message = ("You have been given summaries of individual chapters. Your task is to integrate these "
                          "into a cohesive summary of the entire book without redundancy, ensuring it's concise "
                          "and captures the book's essence. The final summary be " + str(final_paragraphs) + " paragraphs long.")
    
    final_summary = summarizer.integrate_summaries(summaries, supervisor_message)
    print("\nIntegrated Summary:")
    print("====================")
    print(final_summary)

if __name__ == "__main__":
    # Initialize parameters
    epub_file_path = "../books/eat_that_frog.epub"
    agent_version = 4
    agent_size = "small"
    skip_titles = ['Cover', 'Title', 'Copyright', 'Dedication', 'Contents', 'Preface', 'Notes', 'Index', 'Learning Resources', 'About']
    system_message = "You are GPT agent in a system trying to summarize complete books. Your goal is to produce a chapter summary which will then be integrated with the output of other agents who have summarized their own chapter. Extract and convey the core ideas of the chapter in a concise and structured manner, without introductions or conclusions, ideally within three paragraphs."
    temperature = 1.0
    debug = False
    num_chapters = 5
    summarizer = BookSummarizer(epub_file_path, agent_version, agent_size, skip_titles, system_message, temperature, debug)

    # Choose which function to run based on your need
    summarize_complete_book(summarizer, epub_file_path, agent_version, agent_size, skip_titles, system_message, temperature, debug, num_chapters)
    # summarize_chapters_separately(summarizer, epub_file_path, agent_version, agent_size, skip_titles, system_message, temperature, debug, num_chapters)
