from typing import List, Optional, Dict


class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[List["HTMLNode"]] = None,
        props: Optional[Dict[str, str]] = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        """Render node as HTML. To be implemented by subclasses."""
        raise NotImplementedError("to_html must be implemented by subclasses")

    def props_to_html(self) -> str:
        """Render HTML attributes as a string."""
        if not self.props:
            return ""
        # join all key="value" pairs, with a leading space
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return (
            f"HTMLNode(tag={self.tag!r}, value={self.value!r}, "
            f"children={self.children!r}, props={self.props!r})"
        )

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: Optional[dict] = None):
        # LeafNode cannot have children
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            # raw text if no tag
            return self.value
        # return HTML string with props if any
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag={self.tag!r}, value={self.value!r}, props={self.props!r})"

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: Optional[dict] = None):
        if children is None:
            raise ValueError("ParentNode requires a children list")
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have at least one child")

        # recursively render all children
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode(tag={self.tag!r}, children={self.children!r}, props={self.props!r})"
