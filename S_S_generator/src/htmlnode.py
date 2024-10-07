html_tags = {
    "p": ("<p>", "</p>"),
    "div": ("<div>", "</div>"),
    "h1": ("<h1>", "</h1>"),
    "h2": ("<h2>", "</h2>"),
    "h3": ("<h3>", "</h3>"),
    "span": ("<span>", "</span>"),
    "a": ("<a href='#'>", "</a>"),
    "img": ("<img src='#' alt='", "' />"),  # No closing tag, this is self-closing
    "ul": ("<ul>", "</ul>"),
    "ol": ("<ol>", "</ol>"),
    "li": ("<li>", "</li>"),
    "strong": ("<strong>", "</strong>"),
    "em": ("<em>", "</em>"),
    "table": ("<table>", "</table>"),
    "tr": ("<tr>", "</tr>"),
    "th": ("<th>", "</th>"),
    "td": ("<td>", "</td>"),
    "br": ("<br />", ""),  # No closing tag for line breaks
    "hr": ("<hr />", ""),  # No closing tag for horizontal rules
    "blockquote": ("<blockquote>", "</blockquote>"),
    "code": ("<code>", "</code>"),
    "pre": ("<pre>", "</pre>"),
    "nav": ("<nav>", "</nav>"),
    "header": ("<header>", "</header>"),
    "footer": ("<footer>", "</footer>"),
    "section": ("<section>", "</section>"),
    "article": ("<article>", "</article>"),
    "aside": ("<aside>", "</aside>"),
    "form": ("<form>", "</form>"),
    "input": ("<input type='text' value='", "' />"),  # Self-closing input element
    "button": ("<button>", "</button>"),
    "label": ("<label>", "</label>"),
    "select": ("<select>", "</select>"),
    "option": ("<option>", "</option>")
}


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
    def __init__(self, tag=None, value, props=None):
        super().__init__(tag, value, props)
    def leaf_to_html(self):
        leafnode = LeafNode(self)


