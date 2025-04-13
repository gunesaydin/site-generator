class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props == None:
            return ""
        else:
            prop_string = ""
            for prop in self.props:
                prop_string = f"{prop_string} {prop}=\"{self.props[prop]}\""
            return prop_string

    def __repr__(self):
        print(f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})")

    def __eq__(self, value):
        if self.tag == value.tag and self.value == value.value and self.children == value.children and self.props == value.props:
            return True
        else:
            return False