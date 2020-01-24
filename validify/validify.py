"""Validify - rule-based validator for assessing the structure of an xml tree."""

from lxml import etree
import logging
import logzero
from logzero import logger
import collections
import re

from validify.helpers.cleanup_compare_strings import get_compare_value
from validify.helpers import normalize_space
from validify.helpers import messages
from validify.tests.prepare_testdata import compile_test_rules

logzero.loglevel(logging.INFO)

def log_message(message: str, level: str, log_to_console: bool):
    """Deliver log message to logger if console logging is enabled."""

    if log_to_console:
        if level == "debug":
            logger.debug(message)
        elif level == "info":
            logger.info(message)
        elif level == "warn":
            logger.warn(message)
        elif level == "error":
            logger.error(message)

def assess_element_structure(element: etree.Element, element_sourceline: int, xmlns_def: dict, validation_rules: dict, validation_messages: list, validation_results: list, message_lang: str) -> list:
    """Asssess the structure of an xml element, according to the provided validation rules.

    Takes an etree.Element, namespace definition and validation rules.
    If a rule's condition is not satisfied, a validation message is created as a dict, logged and added to a validation results list.

    Example output: [{'message_id': '0001', 'message_text ': 'Element example_element does not contain any subelements, although one or more subelements are expected.', 'element_name': '{namespace}example_element', 'local_name': 'example_element' 'element_sourceline': '23'}]
    """

    element_name = element.tag
    element_local_name = etree.QName(element).localname
    element_attributes = element.attrib
    element_subelements = [subelement.tag for subelement in element]


    if element_name in validation_rules:

        for validation_rules_set in validation_rules[element_name]:
            # Check if conditions for applying the validiation rule set are satisfied (validation_rules_set["rule_conditions"])
            condition_satisfied = {"text_values": True, "attribute_values": True, "reference_elements": True}

            for validation_rule_condition in validation_rules_set["rule_conditions"]:
                if len(validation_rule_condition["text_values"]) > 0:
                    if element.text not in validation_rule_condition["text_values"]:
                        condition_satisfied["text_values"] = False
                if len(validation_rule_condition["attribute_def"]) > 0:
                    for attribute in validation_rule_condition["attribute_def"]:
                        if attribute["attribute_name"] in element.attrib:
                            if element.attrib[attribute["attribute_name"]] not in attribute["allowed_values"]:
                                condition_satisfied["attribute_values"] = False
                        else:
                            condition_satisfied["attribute_values"] = False
                if len(validation_rule_condition["reference_elements"]) > 0:
                    for reference in validation_rule_condition["reference_elements"]:
                        reference_element = element
                        for step in range(reference["preceding_elements"]):
                            reference_element = reference_element.getparent()

                        if reference_element.tag != reference["element_name"]:
                            condition_satisfied["reference_elements"] = False
                        for attribute in reference["attribute_def"]:
                            if attribute["attribute_name"] in reference_element.attrib:
                                if reference_element.attrib[attribute["attribute_name"]] not in attribute["allowed_values"]:
                                    condition_satisfied["reference_elements"] = False
                            else:
                                condition_satisfied["reference_elements"] = False


            not_satisfied = [condition_key for condition_key, condition_value in condition_satisfied.items() if condition_value is False]
            if len(not_satisfied) > 0:
                logger.debug("Validation ruleset for element {} not applied because the following rule conditions are not satisfied: {}.".format(element_name, ", ".join(not_satisfied)))
                continue


            # element children optional
            if not validation_rules_set["element_children_optional"]:
                if len(element) == 0:
                    message_id = "0001"
                    message_text = messages.get_message_by_id(message_id, message_lang).format(element_name)
                    validation_messages.append(message_text)
                    validation_results.append({"message_id": message_id, "message_text": message_text, "element_name": element_name, "element_local_name": element_local_name, "element_sourceline": element_sourceline})

            # element content optional
            if not validation_rules_set["element_content_optional"]:
                if get_compare_value(element) == "":
                    message_id = "0002"
                    message_text = messages.get_message_by_id(message_id, message_lang).format(element_name)
                    validation_messages.append(message_text)
                    validation_results.append(
                        {"message_id": message_id, "message_text": message_text, "element_name": element_name, "element_local_name": element_local_name, "element_sourceline": element_sourceline})

            # optional attributes
            for element_attribute in element_attributes:
                if (element_attribute not in validation_rules_set["optional_attributes"]) and (element_attribute not in validation_rules_set["obligatory_attributes"]):
                    message_id = "0003"
                    message_text = messages.get_message_by_id(message_id, message_lang).format(element_name, element_attribute)
                    validation_messages.append(message_text)
                    validation_results.append(
                        {"message_id": message_id, "message_text": message_text, "element_name": element_name, "element_local_name": element_local_name, "element_sourceline": element_sourceline})

            # obligatory attributes
            for obligatory_attribute in validation_rules_set["obligatory_attributes"]:
                if obligatory_attribute not in element_attributes:
                    message_id = "0004"
                    message_text = messages.get_message_by_id(message_id, message_lang).format(element_name, obligatory_attribute)
                    validation_messages.append(message_text)
                    validation_results.append(
                        {"message_id": message_id, "message_text": message_text, "element_name": element_name, "element_local_name": element_local_name, "element_sourceline": element_sourceline})

            # optional subelements
            for element_subelement in element_subelements:
                if (element_subelement not in validation_rules_set["optional_subelements"]) and (element_subelement not in validation_rules_set["obligatory_subelements"]):
                    message_id = "0005"
                    message_text = messages.get_message_by_id(message_id, message_lang).format(element_name, element_subelement)
                    validation_messages.append(message_text)
                    validation_results.append(
                        {"message_id": message_id, "message_text": message_text, "element_name": element_name, "element_local_name": element_local_name, "element_sourceline": element_sourceline})

            # obligatory subelements
            for obligatory_subelement in validation_rules_set["obligatory_subelements"]:
                if obligatory_subelement not in element_subelements:
                    message_id = "0006"
                    message_text = messages.get_message_by_id(message_id, message_lang).format(element_name, obligatory_subelement)
                    validation_messages.append(message_text)
                    validation_results.append(
                        {"message_id": message_id, "message_text": message_text, "element_name": element_name, "element_local_name": element_local_name, "element_sourceline": element_sourceline})

            # max occurence
            if validation_rules_set["max_occurence"] is not None:  # max occurence nur prüfen, wenn das Element nicht unbegrenzt auftreten kann
                element_siblings = element.getparent().findall(element_name, namespaces=xmlns_def)
                if len(element_siblings) > validation_rules_set["max_occurence"]:
                    message_id = "0007"
                    message_text = messages.get_message_by_id(message_id, message_lang).format(element_name, len(element_siblings), validation_rules_set["max_occurence"])
                    validation_messages.append(message_text)
                    validation_results.append(
                        {"message_id": message_id, "message_text": message_text, "element_name": element_name, "element_local_name": element_local_name, "element_sourceline": element_sourceline})

            # character content allowed
            if validation_rules_set["text_character_content_allowed"] is False:
                if element.text is not None:
                    if element.text != "":
                        message_id = "0008"
                        message_text = messages.get_message_by_id(message_id, message_lang).format(element_name)
                        validation_messages.append(message_text)
                        validation_results.append(
                            {"message_id": message_id, "message_text": message_text, "element_name": element_name, "element_local_name": element_local_name, "element_sourceline": element_sourceline})
            if validation_rules_set["tail_character_content_allowed"] is False:
                if element.tail is not None:
                    if element.tail != "":
                        message_id = "0009"
                        message_text = messages.get_message_by_id(message_id, message_lang).format(element_name)
                        validation_messages.append(message_text)
                        validation_results.append(
                            {"message_id": message_id, "message_text": message_text, "element_name": element_name, "element_local_name": element_local_name, "element_sourceline": element_sourceline})

            # allowed values (xs:enumeration)
            if len(validation_rules_set["allowed_values"]) > 0:
                if element.text is not None:
                    if element.text not in validation_rules_set["allowed_values"]:
                        message_id = "0010"
                        message_text = messages.get_message_by_id(message_id, message_lang).format(element_name, element.text, ", ".join(validation_rules_set["allowed_values"]))
                        validation_messages.append(message_text)
                        validation_results.append({"message_id": message_id, "message_text": message_text, "element_name": element_name, "element_local_name": element_local_name, "element_sourceline": element_sourceline})

            # allowed patterns (xs:pattern)
            if len(validation_rules_set["allowed_patterns"]) > 0:
                valid_value = False
                if element.text is not None:
                    for pattern in validation_rules_set["allowed_patterns"]:
                        match_pattern = re.compile(pattern)
                        pattern_matches = match_pattern.match(element.text)
                        if pattern_matches:
                            valid_value = True
                            break
                if not valid_value:
                    message_id = "0011"
                    message_text = messages.get_message_by_id(message_id, message_lang).format(element_name, element.text, ", ".join(validation_rules_set["allowed_patterns"]))
                    validation_messages.append(message_text)
                    validation_results.append({"message_id": message_id, "message_text": message_text, "element_name": element_name, "element_local_name": element_local_name, "element_sourceline": element_sourceline})

            # Attribute definition
            for attribute_definition in validation_rules_set["attribute_def"]:
                if attribute_definition["attribute_name"] in element.attrib:
                    # allowed values (xs:enumeration)
                    if len(attribute_definition["allowed_values"]) > 0:
                        if element.attrib[attribute_definition["attribute_name"]] not in attribute_definition["allowed_values"]:
                            message_id = "0012"
                            message_text = messages.get_message_by_id(message_id, message_lang).format(element_name, attribute_definition["attribute_name"], element.attrib[attribute_definition["attribute_name"]], ", ".join(attribute_definition["allowed_values"]))
                            validation_messages.append(message_text)
                            validation_results.append({"message_id": message_id, "message_text": message_text, "element_name": element_name, "element_local_name": element_local_name, "element_sourceline": element_sourceline})

                    # allowed patterns (xs:pattern)
                    if len(attribute_definition["allowed_patterns"]) > 0:
                        valid_value = False
                        for pattern in attribute_definition["allowed_patterns"]:
                            match_pattern = re.compile(pattern)
                            pattern_matches = match_pattern.match(element.attrib[attribute_definition["attribute_name"]])
                            if pattern_matches:
                                valid_value = True
                                break
                        if not valid_value:
                            message_id = "0013"
                            message_text = messages.get_message_by_id(message_id, message_lang).format(element_name, attribute_definition["attribute_name"], element.attrib[attribute_definition["attribute_name"]], ", ".join(attribute_definition["allowed_patterns"]))
                            validation_messages.append(message_text)
                            validation_results.append({"message_id": message_id, "message_text": message_text, "element_name": element_name, "element_local_name": element_local_name, "element_sourceline": element_sourceline})




    return validation_results



def validate(input_file: str, xmlns_def=None, validation_rules=None, message_lang=None, log_to_console=True):
    """Validate a given xml file according to the supplied validation rules and return validation messages as a dictionary.

    All elements in the xml file will be processed.
    For a documentation of parameters, see https://github.com/olivergoetze/validify.
    """

    if xmlns_def is None:
        xmlns_def = {}
    if validation_rules is None:
        validation_rules = compile_test_rules()
        log_message("No validation rules defined; using example rules for validation.", "warn", log_to_console)
    message_lang_options = ["de", "en"]
    if message_lang is None:
        message_lang = "de"
        log_message("No message language option delivered; using standard value 'de'.", "info", log_to_console)
    elif message_lang not in message_lang_options:
        message_lang = "de"
        log_message("Non-valid message language option delivered; using standard value 'de'.", "warn", log_to_console)

    validation_messages = []
    validation_results = []

    try:
        xml_in = etree.parse(input_file)
        xml_elements = xml_in.findall("//{*}*")
        for xml_element in xml_elements:
            xml_element_sourceline = xml_element.sourceline  # get original source line before applying normalize-space
            normalize_space.parse_xml_content(xml_element)  # apply normalize-space so only actual character content is found
            validation_results = assess_element_structure(xml_element, xml_element_sourceline, xmlns_def, validation_rules, validation_messages, validation_results, message_lang)
    except etree.XMLSyntaxError:
        log_message("Input file {} is not a well-formed XML document.".format(input_file), "error", log_to_console)

    # Aggregate and output validation messages
    if len(validation_messages) > 0:
        log_message("Validation results for file '{}':".format(input_file), "info", log_to_console)
        aggregated_validation_messages = collections.Counter(validation_messages)
        for validation_message in aggregated_validation_messages:
            log_message("{} ({} occurences)".format(validation_message, aggregated_validation_messages[validation_message]), "info", log_to_console)

    return validation_results
