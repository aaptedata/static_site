from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    
class TextNode():
    
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other):
        return all([self.text == other.text,
                    self.text_type == other.text_type,
                    self.url == other.url])
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def text_node_to_html_node(self):
        match(self.text_type):
            case(TextType.TEXT):
                return LeafNode(None, self.text)
            case(TextType.BOLD):
                return LeafNode('b', self.text)
            case(TextType.ITALIC):
                return LeafNode('i', self.text)
            case(TextType.CODE):
                return LeafNode('code', self.text)
            case(TextType.LINK):
                return LeafNode('a', self.text, {"href": self.url})
            case(TextType.IMAGE):
                return LeafNode('img', None, {"src": "image_url", "alt": "alt_text"})
            case _:
                raise Exception("invalid type")
 
    
# class Bender(Enum):
#     AIR_BENDER = "air"
#     WATER_BENDER = "water"
#     EARTH_BENDER = "earth"
#     FIRE_BENDER = "fire"
    
# from enum import Enum

# Doctype = Enum('Doctype', ['PDF', 'TXT', 'DOCX', 'MD', 'HTML'])

# class DocFormat(Enum):
#     PDF = 1
#     TXT = 2
#     MD = 3
#     HTML = 4

# def convert_format(content, from_format, to_format):
#     match(from_format, to_format):
#         case(DocFormat.MD, DocFormat.HTML):
#             content = content.replace("# ", "<h1>")
#             content = content + '</h1>'
#             return content
            
#         case(DocFormat.TXT, DocFormat.PDF):
#             content = "[PDF] " + content + " [PDF]"
#             return content

#         case(DocFormat.HTML, DocFormat.MD):
#             content = content.replace("<h1>","# ")
#             content = content.replace("</h1>",'')
#             return content

#         # default case
#         case _:
#             raise Exception("invalid type") 