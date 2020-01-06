"""validify is a lxml-based validator for assessing the structure of an xml tree, seeking to cover a good
portion of the XML Schema 1.1 Definition. """

from .validify import (
  validate,
  assess_element_structure,
)

from .helpers import (
  examples,
  messages,
)