class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __eq__(self,node):
        if (self.tag == node.tag and
            self.value == node.value and
            self.children == node.children and
            self.props == node.props):
            return True
        return False
    
    def to_html(self):
        raise NotImplementedError("not implemented yet")

    def props_to_html(self):
        if self.props:
            props_string=""
            for key in self.props:
                props_string += f' {key}="{self.props[key]}"'
            return props_string
        else:
            return ""
    
    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"

class LeafNode(HTMLNode):
    def __init__(self,tag=None,value=None,props=None):
        super().__init__(tag,value,None,props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("no value given")

        if self.tag is None:
            return str(self.value)

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self,tag=None,children=None,props=None):
        super().__init__(tag,None,children,props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: No tag")
        elif self.children is None:
            raise ValueError("Invalid HTML: No children")
        children_html = ""
        for childNode in self.children:
            children_html += childNode.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

