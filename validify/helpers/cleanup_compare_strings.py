from lxml import etree
from validify.helpers import normalize_space

def get_compare_value(compare_element: etree.Element) -> str:
    """Strip element from whitespace and embedded subelements for comparing two element contents and testing whether an element has empty content."""

    normalize_space.parse_xml_content(compare_element)  # Apply normalize-space so whitespace is not considered.

    if compare_element.text is not None:
        compare_string = compare_element.text
    else:
        compare_string = ""

    for embedded_element in compare_element:
        if embedded_element.text is not None:
            compare_string += embedded_element.text

            for embedded_lb_element in embedded_element:
                if embedded_lb_element.text is not None:
                    compare_string += embedded_lb_element.text
                if embedded_lb_element.tail is not None:
                    if not compare_string.endswith(" "):
                        compare_string += " "
                    compare_string += embedded_lb_element.tail

        if embedded_element.tail is not None:
            compare_string += embedded_element.tail

    compare_string = " ".join(compare_string.split())
    return compare_string
