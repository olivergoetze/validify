"""validify is a lxml-based validator for assessing the structure of an xml tree, seeking to cover a subset of the XML Schema 1.1 Definition. """

from .validify import (
  validate,
  assess_element_structure,
)

from .helpers.messages import (
  get_message_by_id,
)

from .tests.prepare_testdata import (
  compile_test_rules,
)