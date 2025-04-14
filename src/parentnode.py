from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("All ParentNodes must have a tag")
        
        if self.children == None or len(self.children) == 0:
            raise ValueError("All ParentNodes must have children")
        
        children_html = ""
        for child in self.children:
            children_html = f"{children_html}{child.to_html()}"

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        
