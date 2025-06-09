# print("hello world") WORKS

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    node_text = TextNode("This is a text node", TextType.TEXT)
    # node_bold = TextNode("This is a bold node", TextType.BOLD)
    # node_italic = TextNode("This is an italic node", TextType.ITALIC)
    # node_code = TextNode("This is a code node", TextType.CODE)
    # node_link = TextNode("This is a link node", TextType.LINK)
    # node_image = TextNode("This is an image node", TextType.IMAGE)
    # node_text = TextNode("This is a garbage node", TextType._) # Problem
    # html_node = text_node_to_html_node(node_text)  
    print(node_text.text_node_to_html_node())   
    
    
if __name__ == "__main__":
    main()
 
 
 
 
 
    
# *****************************************************************************************
# SCRATCH

    # node1 = HTMLNode("a", "HTML value", ['obj1', 'obj2', 'obj3'], {"href": "https://www.google.com"})
    # node2 = HTMLNode("a", "HTML value", ['obj1', 'obj2', 'obj3'],
    #                      {"href": "https://www.google.com","target": "_blank",})
    # node3 = LeafNode("p", "Hello, world!", {"href": "https://www.google.com"})
    
    # print(f"These are some basic operations tests.")
    # print(TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev"))
    # print(HTMLNode("a", "HTML value", ['obj1', 'obj2', 'obj3'], {"href": "https://www.google.com"}))
    # print(LeafNode("p", "Hello, world!", {"href": "https://www.google.com"}))
    # print(node1.to_html())
    # print(node1.props_to_html())
    # print(node2.props_to_html())
    # print(node3.to_html())
    # node4 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    # print(node4.to_html()) 

#     node5 = ParentNode('a', ['obj1', 'obj2', 'obj3'], {"href": "https://www.google.com"})
#     node6 = ParentNode(
#     "p", 
#     [
#         LeafNode("b", "Bold text"),
#         LeafNode(None, "Normal text"),
#         LeafNode("i", "italic text"),
#         LeafNode(None, "Normal text"),
#     ],
# )
#     # print(ParentNode('a', ['obj1', 'obj2', 'obj3'], {"href": "https://www.google.com"}))
#     # print(node6)
#     print(node6.to_html())
