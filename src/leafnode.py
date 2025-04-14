from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value.")
        html_string = ""
        if self.tag == None:
            html_string = self.value
        else:
            html_string = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return html_string