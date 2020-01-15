from lxml import etree

def normalize_space(element: etree.Element, part: str):
    """Function for replacing whitespace in strings.

    Text is replaced inside elements (text) as well as in between elements (tail).
    """

    if part == "text":
        element_text = element.text.replace("\n", " ").replace("\t", " ").replace("\r", " ")
        element_text = " ".join(element_text.split())
        element.text = element_text
    elif part == "tail":
        element_tail = element.tail.replace("\n", " ").replace("\t", " ").replace("\r", " ")
        element_tail = " ".join(element_tail.split())
        element.tail = element_tail

def parse_xml_content(element: etree.Element):
    """Remove whitespace (redundant spaces, newlines, tabs, carriage returns) from element content and tail."""

    if element.text is not None:
        normalize_space(element, part="text")

    for sub_element in element:
        if sub_element.text is not None:
            normalize_space(sub_element, part="text")
        if sub_element.tail is not None:
            normalize_space(sub_element, part="tail")
