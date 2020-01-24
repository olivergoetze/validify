![PyPI - Python Version](https://img.shields.io/pypi/pyversions/validify) 
![PyPI - Status](https://img.shields.io/pypi/status/validify)
![PyPI - License](https://img.shields.io/pypi/l/validify)

`validify` is a rule-based validation module for assessing the structure of an xml tree, written in Python and built on top of the [lxml](https://lxml.de/) library. It currently covers a subset of the XML Schema 1.1 Definition.

### Requirements
- Python 3.5+
- [lxml](https://pypi.org/project/lxml/)
- [logzero](https://pypi.org/project/logzero/)

### Installation
The `validify` module can be found on [PyPI](https://pypi.org/project/validify/).
It can be installed by using pip:

`pip install validify`

Dependencies will be automatically fetched by pip.

### Basic usage
```python
import validify
validation_result = validify.validate(input_file="validify/test.xml", xmlns_def=None, validation_rules=None, message_lang=None, log_to_console=True)
```

#### Parameters
- input_file (required): path to xml file which should be validated.
- xmlns_def (default: `None`): a namespace definition can be supplied as a python dictionary object (`{None: "default_namespace", "namespace_prefix": "another_namespace"}}`). 
- validation_rules (default: `None`): a python dictionary object containing the validation rules (see "Defining validation rules" below for an example.). An example rules dictionary is used if no value is supplied here.
- message_lang (default: `de`): language for validation message strings. Supported values are `en` and `de`.
- log_to_console (default: `True`): if `True`, validation and status messages are logged to console. If false, validation messages are only added to the results dict returned by `validfy`. 

#### Defining validation rules
Validation rules are defined in a dictionary object (JSON-like structure):
```python
validation_rules = {}

validation_rules["element"] = []
ruleset = {}

ruleset["element_content_optional"] = False
ruleset["element_children_optional"] = False
ruleset["optional_attributes"] = ["valid_optional_attribute_01", "valid_optional_attribute_02"]
ruleset["obligatory_attributes"] = ["obligatory_attribute_01", "obligatory_attribute_02"]
ruleset["optional_subelements"] = ["optional_subelement_01", "optional_subelement_02"]
ruleset["obligatory_subelements"] = ["obligatory_subelement_01", "obligatory_subelement_02"]
ruleset["max_occurence"] = 2
ruleset["text_character_content_allowed"] = True
ruleset["tail_character_content_allowed"] = False

ruleset["allowed_values"] = ["valid_value_01", "valid_value_02"]
ruleset["allowed_patterns"] = ["^test-\d{4}$", "^test-\d{3}$"]
ruleset["allowed_datatypes"] = []
ruleset["attribute_def"] = []
ruleset["attribute_def"].append({"attribute_name": "valid_optional_attribute_01", "allowed_values": ["valid_value_01", "valid_value_02"],
                                 "allowed_patterns": ["^test-\d{4}$", "^test-\d{3}$"]})
ruleset["attribute_def"].append(
    {"attribute_name": "obligatory_attribute_01", "allowed_values": ["valid_value_01", "valid_value_02"],
     "allowed_patterns": []})


ruleset["rule_conditions"] = []
ruleset["rule_conditions"].append(
    {"text_values": ["valid_text_value"],
     "attribute_def": [{"attribute_name": "valid_attribute_name", "allowed_values": ["valid_value"]},
                       {"attribute_name": "another_valid_attribute_name", "allowed_values": ["valid_value"]}],
     "reference_elements": [{"element_name": "reference_element", "attribute_def": [{"attribute_name": "reference_test", "allowed_values": ["valid_value"]}],"preceding_elements": 1}]})


validation_rules["element"].append(ruleset)
```
Each element can be provided with one or more rulesets.
The `rule_conditions` definiton can be used when the ruleset should only be applied if the validated element contains the defined attribute(s) and attribute value(s). Besides the validated element, a reference element can also be defined and checked for attribute values. Currently, it must be a parent element of the validated element (parent level defined by `preceding_elements`).

#### Validation output
`validify.validate` returns a list containing the validation messages as dictionaries:
```python
[{'message_id': '0001', 'message_text ': 'Element example_element does not contain any subelements, although one or more subelements are expected.', 'element_name': '{namespace}example_element', 'local_name': 'example_element', 'element_sourceline': '23'}]
```

### XML Schema feature coverage
For now, a small subset of the [XML Schema](https://www.w3.org/TR/xmlschema11-1/) features is provided:
- Test if a ruleset applies by checking a reference element's text and attribute values
- Define if element childen and content are optional
- Define optional and obligatory attributes
- Define optional and obligatory subelements
- Define maximum occurence of an element
- Define if character content is allowed
- Define an element's allowed values (~ xs:enumeration)
- Define an element's allowed patterns (~ xs:pattern)
- Define an attribute's allowed values and patterns

This module is currently used for validating data deliveries in the [EAD XML application profile](https://wiki.deutsche-digitale-bibliothek.de/pages/viewpage.action?pageId=19010180), which are processed for ingesting in the metadata portals [Deutsche Digitale Bibliothek](https://www.ddb.de) and [Archivportal-D](https://www.archivportal-d.de). Therefore, supported features currently are nowhere near those provided by the XML Schema standard. Feature support is supposed to be gradually expanded, however.

The following features are planned for a future release:
- checking max/min text and attribute values
- validating string length
- support for pre-defined data types (i.e. `xs:ID`, `xs:NMTOKEN`)
- rule conditions: direct support for XPath and lxml's `itersiblings` and `iterancestors` methods.

### Development status
This package is in an early development stage. It should already work reliably for intended use cases, but documentation and stability of API are still lacking.