import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    # def test_eq(self):
    #     node1 = HTMLNode("<a>", "HTML value", ['obj1', 'obj2', 'obj3'], {"href": "https://www.google.com"})
    #     node2 = HTMLNode("<a>", "HTML value", ['obj1', 'obj2', 'obj3'],
    #                      {"href": "https://www.google.com","target": "_blank",})
    #     node3 = HTMLNode("<a>", "HTML value", ['obj1', 'obj2', 'obj3'], {"href": "https://www.yahoo.com"})
       
    #     # Tests (single quotes with props)
    #     self.assertEqual(node1.props_to_html(), ' href=https://www.google.com')
    #     self.assertEqual(node2.props_to_html(), ' href=https://www.google.com target=_blank')
    #     self.assertNotEqual(node3.props_to_html(), ' href=https://www.google.com target=_blank')
        
    # def test_leaf_to_html_p(self):
    #     node_leaf1 = LeafNode("p", "Hello, world!")
    #     node_leaf2 = LeafNode("b", "Hello, world!")
    #     node_leaf3 = LeafNode(None, "Hello, world!")
    #     node_leaf4 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        
    #     # Tests (single quotes with props)
    #     self.assertEqual(node_leaf1.to_html(), "<p>Hello, world!</p>")
    #     self.assertEqual(node_leaf2.to_html(), "<b>Hello, world!</b>")
    #     self.assertNotEqual(node_leaf2.to_html(), "<p>Hello, world!</p>")
    #     self.assertEqual(node_leaf3.to_html(), "Hello, world!")
    #     self.assertNotEqual(node_leaf3.to_html(), "<p>Hello, world!</p>")
    #     self.assertEqual(node_leaf4.to_html(), '<a href=https://www.google.com>Click me!</a>')
    #     # single quotes
    #     # self.assertEqual(node_leaf4.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
        
    # def test_leaf_to_html_p(self):
    #     node6 = ParentNode("p", 
    # [
    #     LeafNode("b", "Bold text"),
    #     LeafNode(None, "Normal text"),
    #     LeafNode("i", "italic text"),
    #     LeafNode(None, "Normal text"),
    # ])
    #     node7 = ParentNode("p", 
    # [
    #     LeafNode("i", "italic text"),
    #     LeafNode(None, "Normal text"),
    #     LeafNode("b", "Bold text"),
    #     LeafNode(None, "Normal text"),
    # ])
    
    #     self.assertEqual(node6.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
    #     self.assertNotEqual(node7.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
    #     self.assertEqual(node7.to_html(), '<p><i>italic text</i>Normal text<b>Bold text</b>Normal text</p>')
    
    def test_text(self):
        node_text = TextNode("This is a text node", TextType.TEXT)
        node_bold = TextNode("This is a bold node", TextType.BOLD)
        node_italic = TextNode("This is an italic node", TextType.ITALIC)
        node_code = TextNode("This is a code node", TextType.CODE)
        node_link = TextNode("This is a link node", TextType.LINK)
        node_image = TextNode("This is an image node", TextType.IMAGE)
        
        html_node = node_text.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertNotEqual(html_node.value, "This is a bold node")
        
        
    # def test_to_html_with_children(self):
    #     child_node = LeafNode("span", "child")
    #     parent_node = ParentNode("div", [child_node])
    #     self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    # def test_to_html_with_grandchildren(self):
    #     grandchild_node = LeafNode("b", "grandchild")
    #     child_node = ParentNode("span", [grandchild_node])
    #     parent_node = ParentNode("div", [child_node])
    #     self.assertEqual(
    #         parent_node.to_html(),
    #         "<div><span><b>grandchild</b></span></div>",
    # )


if __name__ == "__main__":
    unittest.main()