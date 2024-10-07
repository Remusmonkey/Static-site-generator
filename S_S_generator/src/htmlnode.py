html_hyperlink = "a"
html_paragraph = "p"
html_bold = "b"
html_italics = "i"
html_link = "a"
html_image = "img"
html_unordered_list = "ul"
html_ordered_list = "ol"
html_quote = "blockquote"
html_code = "code"


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError ("to_html method not implemented")
    def props_to_html(self):
        if self.props is None:
            return ""
        html_props = ""
        for i in self.props:
            html_props += f' {i}="{self.props[i]}"'
        return html_props
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"