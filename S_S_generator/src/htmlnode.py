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
        raise NotImplementedError 
    def props_to_html(self):
        x=self.props.items()
        html_attr = ""
        for i in x:
            html_attr += f' "{i[0]}"="{i[1]}"'
        return html_attr
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"