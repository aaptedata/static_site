class HTMLNode():
    
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # string
        self.value = value # string
        self.children = children # list
        self.props = props # dict
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None: # Add this check
            return ''
        props_string = ''
        for key, val in self.props.items():
            props_string += f' {key}={val}'
            
        return props_string
    
    def __repr__(self):
        return f'HTMLNode(Tag: <{self.tag}> Value: {self.value} Children: {self.children} Props: {self.props})'
            


class LeafNode(HTMLNode):
    
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)
        
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes must have a value")
        if self.tag is None:
            return self.value
        # Here's where you'll use self.props_to_html()
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"    
    
    def __repr__(self):
        if self.tag == None:
            return f'LeafNode(Tag: {self.tag} Value: {self.value} Props: {self.props})'
        return f'LeafNode(Tag: <{self.tag}> Value: {self.value} Props: {self.props})'
      
class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("A tag is required")
        parent_string = f'<{self.tag}>'
        for child in self.children:
            if child.value is None:
                raise ValueError("Leaf nodes must have a value")
            if child.tag == None:
                parent_string += f'{child.value}'
            else:
                parent_string += f'<{child.tag}>{child.value}</{child.tag}>'
        return parent_string + f'</{self.tag}>'
           
    def __repr__(self):
        return f"ParentNode(Tag: <{self.tag}> Value: {self.value} Children: {self.children} Props: {self.props})"
    
    
    
    
    # *****************************************************************************************************
    # SCRATCH
    # 
    # def props_to_html(self):
    #     if self.props is None: # Add this check
    #         return ""
    #     props_string = ''
    #     for key, val in self.props.items():
    #         props_string += f' {key}=\"{val}\"' # Also added quotes around the value
    #     return props_string
   
    # def to_html(self):
    #     if self.value == None:
    #         raise ValueError("All leaf nodes must have a value.")
    #     if self.tag == None:
    #         return str(self.value)
    #     else:
    #         if all([self.tag == 'a',
    #                 self.props is not None,
    #                 'href' in self.props
    #         ]):
    #             return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
    #         else:
    #             return f"<{self.tag}>{self.value}</{self.tag}>"