"""validify"""

from lxml import etree
from logzero import logger
import collections

from validify.helpers.cleanup_compare_strings import get_compare_value
from validify.helpers import normalize_space
from validify.helpers import messages
from validify.helpers import examples


def assess_element_structure(element: etree.Element, element_sourceline: int, xmlns_def: dict, validation_rules: dict, validation_messages: list, validation_results: list) -> list:
    element_name = element.tag
    element_attributes = element.attrib
    element_subelements = [subelement.tag for subelement in element]


    if element_name in validation_rules:

        for validation_rules_set in validation_rules[element_name]:
            # TODO: Prüfen, ob Bedingungen zur Anwendung der Regel erfüllt werden (validation_rules_set["rule_conditions"])

            # element children optional
            if not validation_rules_set["element_children_optional"]:
                if len(element) == 0:
                    validation_messages.append("Element {} enthält keine Subelemente, obwohl eines oder mehrere Subelemente erwartet.".format(element_name))
                    validation_results.append({"message_id": "0001", "element_name": element_name, "element_sourceline": element_sourceline})

            # element content optional
            if not validation_rules_set["element_content_optional"]:
                if get_compare_value(element) == "":
                    validation_messages.append("Element {} enthält keinen Elementinhalt, obwohl das Element nicht leer sein darf.".format(element_name))
                    validation_results.append(
                        {"message_id": "0002", "element_name": element_name, "element_sourceline": element_sourceline})

            # optional attributes
            for element_attribute in element_attributes:
                if (element_attribute not in validation_rules_set["optional_attributes"]) and (element_attribute not in validation_rules_set["obligatory_attributes"]):
                    validation_messages.append("Element {} enthält ein nicht erwartetes Attribut: {}".format(element_name, element_attribute))
                    validation_results.append(
                        {"message_id": "0003", "element_name": element_name, "element_sourceline": element_sourceline})

            # obligatory attributes
            for obligatory_attribute in validation_rules_set["obligatory_attributes"]:
                if obligatory_attribute not in element_attributes:
                    validation_messages.append("Element {} enthält nicht das Pflicht-Attribut {}.".format(element_name, obligatory_attribute))
                    validation_results.append(
                        {"message_id": "0004", "element_name": element_name, "element_sourceline": element_sourceline})

            # optional subelements
            for element_subelement in element_subelements:
                if (element_subelement not in validation_rules_set["optional_subelements"]) and (element_subelement not in validation_rules_set["obligatory_subelements"]):
                    validation_messages.append("Element {} enthält ein nicht erwartetes Subelement: {}.".format(element_name, element_subelement))
                    validation_results.append(
                        {"message_id": "0005", "element_name": element_name, "element_sourceline": element_sourceline})

            # obligatory subelements
            for obligatory_subelement in validation_rules_set["obligatory_subelements"]:
                if obligatory_subelement not in element_subelements:
                    validation_messages.append("Element {} enthält nicht das Pflicht-Subelement {}.".format(element_name, obligatory_subelement))
                    validation_results.append(
                        {"message_id": "0006", "element_name": element_name, "element_sourceline": element_sourceline})

            # max occurence
            if validation_rules_set["max_occurence"] is not None:  # max occurence nur prüfen, wenn das Element nicht unbegrenzt auftreten kann
                element_siblings = element.getparent().findall(element_name, namespaces=xmlns_def)
                if len(element_siblings) > validation_rules_set["max_occurence"]:
                    validation_messages.append("Element {} ist {} mal vorhanden, erwartet wird jedoch nur {} Vorkommen.".format(element_name, len(element_siblings), validation_rules_set["max_occurence"]))
                    validation_results.append(
                        {"message_id": "0007", "element_name": element_name, "element_sourceline": element_sourceline})

            # character content allowed
            if validation_rules_set["text_character_content_allowed"] is False:
                if element.text is not None:
                    if element.text != "":
                        validation_messages.append("Element {} should not contain text character content.".format(element_name))
                        validation_results.append(
                            {"message_id": "0008", "element_name": element_name, "element_sourceline": element_sourceline})
            if validation_rules_set["tail_character_content_allowed"] is False:
                if element.tail is not None:
                    if element.tail != "":
                        validation_messages.append("Element {} should not contain tail character content.".format(element_name))
                        validation_results.append(
                            {"message_id": "0009", "element_name": element_name, "element_sourceline": element_sourceline})

            # level occurence  # TODO: EAD-spezifisch --> entfernen
            c_parents = element.iterancestors(tag="{urn:isbn:1-931666-22-9}c", )
            for c_parent in c_parents:
                if "level" in c_parent.attrib:
                    if c_parent.attrib["level"] not in validation_rules_set["level_occurence"]:
                        validation_messages.append("Element {} auf Ebene {} nicht erwartet.".format(element_name, c_parent.attrib["level"]))
                else:
                    validation_messages.append("Element {} - direkter c-Parent besitzt kein level-Attribut.".format(element_name))
                break

            # allowed values (xs:enumeration)
            if len(validation_rules_set["allowed_values"]) > 0:
                if element.text is not None:
                    if element.text not in validation_rules_set["allowed_values"]:
                        validation_messages.append("{} -- Element value not eqal to required value: '{}' != '{}'".format(element_name, element.text, ", ".join(validation_rules_set["allowed_values"])))

            # Attribute definition
            for attribute_definition in validation_rules_set["attribute_def"]:
                if attribute_definition["attribute_name"] in element.attrib:
                    if element.attrib[attribute_definition["attribute_name"]] not in attribute_definition["allowed_values"]:
                        validation_messages.append("{}, attribute {} -- attribute value not eqal to required value: '{}' != '{}'".format(element_name, attribute_definition["attribute_name"], element.attrib[attribute_definition["attribute_name"]], ", ".join(attribute_definition["allowed_values"])))




    return validation_results # TODO: Mapping der Meldungs-IDs auf Kategorien sollte im DPT selbst über eine Konkordanz erfolgen.)



def validate(input_file: str, xmlns_def=None, validation_rules=None):
    if xmlns_def is None:
        xmlns_def = {}
    if validation_rules is None:
        validation_rules = examples.compile_example_rules()
        logger.warn("No validation rules defined; using example rules for validation.")
    validation_messages = []
    validation_results = []

    try:
        xml_in = etree.parse(input_file)
        xml_elements = xml_in.findall("//{*}*")
        for xml_element in xml_elements:
            xml_element_sourceline = xml_element.sourceline  # get original source line before applying normalize-space
            normalize_space.parse_xml_content(xml_element)  # apply normalize-space so only actual character content is found
            validation_results = assess_element_structure(xml_element, xml_element_sourceline, xmlns_def, validation_rules, validation_messages, validation_results)
    except etree.XMLSyntaxError:
        logger.error("Input file {} is not a well-formed XML document.".format(input_file))

    # Aggregate and output validation messages
    if len(validation_messages) > 0:
        logger.info("Validation results for file '{}':".format(input_file))
        aggregated_validation_messages = collections.Counter(validation_messages)
        for validation_message in aggregated_validation_messages:
            logger.info(
                "{} ({} occurences)".format(validation_message, aggregated_validation_messages[validation_message]))
