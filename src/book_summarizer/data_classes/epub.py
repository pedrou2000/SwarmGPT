import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import constants
from langchain_core.pydantic_v1 import BaseModel, Field
import warnings

warnings.filterwarnings("ignore", message="In the future version we will turn default option ignore_ncx to True.")
# warnings.filterwarnings("ignore", message="This search incorrectly ignores the root element, and will be fixed in a future version.")


class Metadata():
    title: str
    author: str
    identifier: str
    language: str
    description: str
    
    def __init__(self, title, author, identifier, language, description):
        self.title = title
        self.author = author
        self.identifier = identifier
        self.language = language
        self.description = description

class ContentNode():
    title: str
    content: str
    children: list
    parent: 'ContentNode'
    content_item: ebooklib.epub.EpubItem

    def __init__(self, title, content, content_item=None):
        self.title = title
        self.content = content
        self.children = []
        self.parent = None  
        self.content_item = content_item  # This is the raw content item associated with the node

class EPUB():
    book: epub.EpubBook
    metadata: Metadata
    root_node: ContentNode

    def __init__(self, file_path):
        # Load the EPUB file
        self.book = epub.read_epub(file_path, options={'ignore_ncx': False})
        
        # Parse Metadata and Content
        self.metadata = self._parse_metadata()
        self.root_node = ContentNode("Root", "")  # Root node to hold the content tree
        self._populate_content_tree(self.book.toc, self.root_node)

    def _parse_metadata(self):
        """Extracts metadata from the book object."""
        title = self._get_metadata('DC', 'title')
        author = self._get_metadata('DC', 'creator')
        identifier = self._get_metadata('DC', 'identifier')
        language = self._get_metadata('DC', 'language')
        description = self._get_metadata('DC', 'description')

        return Metadata(title, author, identifier, language, description)

    def _get_metadata(self, namespace, name):
        """Utility function to fetch metadata values."""
        meta_item = self.book.get_metadata(namespace, name)
        return meta_item[0][0] if meta_item else None

    def _populate_content_tree(self, items, parent_node):
        """Populates the content tree using the book's table of contents."""
        for item in items:
            try:
                if isinstance(item, ebooklib.epub.Link):
                    self._add_content_node(item, parent_node)
                elif isinstance(item, tuple):
                    self._add_section_node(item, parent_node)
            except Exception as e:
                title = item.title if isinstance(item, ebooklib.epub.Link) else 'Tuple'
                print(f"Error while parsing item {title}. Error: {str(e)}")

    def _add_content_node(self, item, parent_node):
        """Adds a new content node to the tree."""
        title = item.title
        content_item = self.book.get_item_with_id(item.uid) or self.book.get_item_with_href(item.href)
        content_text = self._extract_content_text(content_item) if content_item else ""

        node = ContentNode(title, content_text)
        node.parent = parent_node
        parent_node.children.append(node)

    def _add_section_node(self, item, parent_node):
        """Adds a new section node and its children to the tree."""
        section_title = item[0].title if item[0] else "No Title"
        section_node = ContentNode(section_title, "")
        section_node.parent = parent_node
        parent_node.children.append(section_node)

        # Recursively add the nested TOC items
        self._populate_content_tree(item[1], section_node)

    def _extract_content_text(self, content_item):
        """Extracts text from the content item using BeautifulSoup."""
        content_soup = BeautifulSoup(content_item.content, 'html.parser')
        return content_soup.get_text()

    def display_high_level_info(self):
        """Displays metadata and a high-level view of the parsed TOC in the console."""
        # Display Metadata
        print("\n================== METADATA ==================")
        print(f"Title: {self.metadata.title}")
        print(f"Authors: {self.metadata.author}")
        print(f"Identifier: {self.metadata.identifier}")
        print(f"Language: {self.metadata.language}")
        print("==============================================")

        # Display high-level TOC
        print("\n================== TABLE OF CONTENTS ==================")
        self._display_toc_recursive(self.root_node, level=0)

    def _display_toc_recursive(self, node, level):
        """Recursive function to display the TOC."""
        indent = '    ' * level  # 4 spaces per level
        print(f"{indent}=> {node.title}")

        for child in node.children:
            self._display_toc_recursive(child, level + 1)


def generate_markdown_toc(node, content_length=100, level=0):
    """ 
    Recursively generate a markdown representation of the content with indentation
    to represent the hierarchy.
    """
    indent = '#' * (level + 1)  # For markdown headers. 
    content_snippet = node.content[:content_length] + "..." if len(node.content) > 50 else node.content

    markdown_content = f"{indent} {node.title}\n\n{content_snippet}\n\n"
    
    for child in node.children:
        markdown_content += generate_markdown_toc(child, content_length=content_length, level = level + 1)
    
    return markdown_content

def generate_full_markdown(epub_obj, content_length=constants.MARKDOWN_OUTPUT_MAX_LEN):
    """Generates markdown content for an EPUB's metadata and TOC."""
    markdown_toc = f"# Metadata:\n\n- Title: {epub_obj.metadata.title}\n- Authors: {epub_obj.metadata.author}\n\n"
    markdown_toc += "# TOC Content:\n\n"
    markdown_toc += generate_markdown_toc(epub_obj.root_node, content_length=content_length)
    return markdown_toc

def process_single_epub(epub_path, output_dir_path=constants.PARSED_BOOKS_DIR, content_length=constants.MARKDOWN_OUTPUT_MAX_LEN):
    """Processes a single EPUB file and saves the TOC as markdown."""

    # Create an EPUB object and parse the EPUB file
    epub_obj = EPUB(epub_path)

    # Display metadata and TOC
    epub_obj.display_high_level_info()

    # Generate markdown content for the EPUB's TOC
    markdown_content = generate_full_markdown(epub_obj, content_length)

    # Use the same base name as the EPUB for the output markdown file
    base_name = os.path.basename(epub_path)  # e.g., "sample.epub"
    output_file_name = os.path.join(output_dir_path, base_name.replace('.epub', '.md'))
    
    try:
        with open(output_file_name, 'w', encoding='utf-8') as md_file:
            md_file.write(markdown_content)
        print(f"TOC has been saved to {output_file_name}!")
    except Exception as e:
        print(f"Error writing to {output_file_name}. Reason: {e}")

if __name__ == "__main__":
    
    # Determine the output directory

    # Iterate through all EPUB files in the books directory and process them
    for epub_file in os.listdir(constants.BOOKS_DIR):
        if epub_file.endswith('.epub'):
            epub_path = os.path.join(constants.BOOKS_DIR, epub_file)
            process_single_epub(epub_path, constants.PARSED_BOOKS_DIR)



