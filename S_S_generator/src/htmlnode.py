# html_tags = {
#     "p": ("<p>", "</p>"),
#     "b": ("<b>", "</b>"),
#     "div": ("<div>", "</div>"),
#     "h1": ("<h1>", "</h1>"),
#     "h2": ("<h2>", "</h2>"),
#     "h3": ("<h3>", "</h3>"),
#     "span": ("<span>", "</span>"),
#     "a": ("<a href='{}'>", "</a>"),
#     "img": ("<img src='{}' alt='", "' />"),  # No closing tag, this is self-closing
#     "ul": ("<ul>", "</ul>"),
#     "ol": ("<ol>", "</ol>"),
#     "li": ("<li>", "</li>"),
#     "strong": ("<strong>", "</strong>"),
#     "em": ("<em>", "</em>"),
#     "table": ("<table>", "</table>"),
#     "tr": ("<tr>", "</tr>"),
#     "th": ("<th>", "</th>"),
#     "td": ("<td>", "</td>"),
#     "br": ("<br />", ""),  # No closing tag for line breaks
#     "hr": ("<hr />", ""),  # No closing tag for horizontal rules
#     "blockquote": ("<blockquote>", "</blockquote>"),
#     "code": ("<code>", "</code>"),
#     "pre": ("<pre>", "</pre>"),
#     "nav": ("<nav>", "</nav>"),
#     "header": ("<header>", "</header>"),
#     "footer": ("<footer>", "</footer>"),
#     "section": ("<section>", "</section>"),
#     "article": ("<article>", "</article>"),
#     "aside": ("<aside>", "</aside>"),
#     "form": ("<form>", "</form>"),
#     "input": ("<input type='text' value='", "' />"),  # Self-closing input element
#     "button": ("<button>", "</button>"),
#     "label": ("<label>", "</label>"),
#     "select": ("<select>", "</select>"),
#     "option": ("<option>", "</option>")
# }


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

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        #self.tag = tag
    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    # This was my original code. Keeping it here to remind me to think about it vs the code above this
    # The self.props_to_html part in the above code is important to remember.  I didn't fully consider it 
    # when I was thinking about my code below.  I thought I needed to create a master html tags list like at
    # the top of this code.
    # def to_html(self):
    #     if self.value == None:
    #         raise ValueError ("Invalid HTML: no value")
    #     if self.tag in html_tags:
    #         start_tag, end_tag = html_tags[self.tag]
    #         if self.tag == "a":
    #             for i in self.props:
    #             start_tag = start_tag.format(self.props[i])
        
    #     # Similarly, if the tag is "img" and a URL is provided for the src attribute
    #         elif tag == "img" and url:
    #             start_tag = start_tag.format(url)
    #         return f'{start_tag}{self.value}{end_tag}'
    #     else:
    #         return self.value
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag == None:
            raise ValueError ("Cannot Format: Tag required")
        if self.children == None:
            raise ValueError ("Node Children required")
        result = f"<{self.tag}>"
        for child in self.children:
            if isinstance(child, ParentNode):
                result += child.to_html()
            elif isinstance(child, LeafNode):
                result+= child.to_html()
            else:
                raise ValueError ("Invalid child type")
        result += f"</{self.tag}>"
        return result
        
        
        
        
        


