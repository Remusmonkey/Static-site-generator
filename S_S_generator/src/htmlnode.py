


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError 
    def props_to_html(self):
        html_attr = ""
        for i in self.props:
            html_attr += f' {self.props[key]}="{self.props[value]}"'
        return html_attr
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"