"""lxmlschemavalidator"""

from lxml import etree
from logzero import logger
import collections

from lxmlschemavalidator.helpers.cleanup_compare_strings import get_compare_value
from lxmlschemavalidator.helpers import normalize_space


def assess_element_structure(element: etree.Element, element_sourceline: int, xmlns_def: dict, validation_rules: dict, validation_messages: list) -> list:
    element_name = element.tag
    element_attributes = element.attrib
    element_subelements = [subelement.tag for subelement in element]


    if element_name in validation_rules:

        # element children optional
        if not validation_rules[element_name]["element_children_optional"]:
            if len(element) == 0:
                validation_messages.append("Element {} enthält keine Subelemente, obwohl eines oder mehrere Subelemente erwartet.".format(element_name))

        # element content optional
        if not validation_rules[element_name]["element_content_optional"]:
            if get_compare_value(element) == "":
                validation_messages.append("Element {} enthält keinen Elementinhalt, obwohl das Element nicht leer sein darf.".format(element_name))

        # optional attributes
        for element_attribute in element_attributes:
            if (element_attribute not in validation_rules[element_name]["optional_attributes"]) and (element_attribute not in validation_rules[element_name]["obligatory_attributes"]):
                validation_messages.append("Element {} enthält ein nicht erwartetes Attribut: {}".format(element_name, element_attribute))

        # obligatory attributes
        for obligatory_attribute in validation_rules[element_name]["obligatory_attributes"]:
            if obligatory_attribute not in element_attributes:
                validation_messages.append("Element {} enthält nicht das Pflicht-Attribut {}.".format(element_name, obligatory_attribute))

        # optional subelements
        for element_subelement in element_subelements:
            if (element_subelement not in validation_rules[element_name]["optional_subelements"]) and (element_subelement not in validation_rules[element_name]["obligatory_subelements"]):
                validation_messages.append("Element {} enthält ein nicht erwartetes Subelement: {}.".format(element_name, element_subelement))

        # obligatory subelements
        for obligatory_subelement in validation_rules[element_name]["obligatory_subelements"]:
            if obligatory_subelement not in element_subelements:
                validation_messages.append("Element {} enthält nicht das Pflicht-Subelement {}.".format(element_name, obligatory_subelement))

        # max occurence
        if validation_rules[element_name]["max_occurence"] is not None:  # max occurence nur prüfen, wenn das Element nicht unbegrenzt auftreten kann
            element_siblings = element.getparent().findall(element_name, namespaces=xmlns_def)
            if len(element_siblings) > validation_rules[element_name]["max_occurence"]:
                validation_messages.append("Element {} ist {} mal vorhanden, erwartet wird jedoch nur {} Vorkommen.".format(element_name, len(element_siblings), validation_rules[element_name]["max_occurence"]))

        # character content allowed
        if validation_rules[element_name]["text_character_content_allowed"] is False:
            if element.text is not None:
                if element.text != "":
                    validation_messages.append("Element {} should not contain text character content.".format(element_name))
        if validation_rules[element_name]["tail_character_content_allowed"] is False:
            if element.tail is not None:
                if element.tail != "":
                    validation_messages.append("Element {} should not contain tail character content.".format(element_name))

        # level occurence  # TODO: EAD-spezifisch --> entfernen
        c_parents = element.iterancestors(tag="{urn:isbn:1-931666-22-9}c", )
        for c_parent in c_parents:
            if "level" in c_parent.attrib:
                if c_parent.attrib["level"] not in validation_rules[element_name]["level_occurence"]:
                    validation_messages.append("Element {} auf Ebene {} nicht erwartet.".format(element_name, c_parent.attrib["level"]))
            else:
                validation_messages.append("Element {} - direkter c-Parent besitzt kein level-Attribut.".format(element_name))
            break


    return validation_messages  # TODO: Weiteren Rückgabewert für weitere Verarbeitung implementieren (dict mit Meldungs-ID (Meldungen in externe Konkordanz auslagern), sourceline des Elements, Element-Kontext als String, ...?) - Mapping der Meldungs-IDs auf Kategorien sollte im DPT selbst über eine Konkordanz erfolgen.)


def compile_example_rules() -> dict:
    # create example validation rules for testing
    validation_rules = {}

    validation_rules["{urn:isbn:1-931666-22-9}c"] = {}
    validation_rules["{urn:isbn:1-931666-22-9}c"][
        "element_content_optional"] = True  # Element darf auch ohne Content auftreten
    validation_rules["{urn:isbn:1-931666-22-9}c"][
        "element_children_optional"] = False  # Element darf auch ohne Kindelemente auftreten
    validation_rules["{urn:isbn:1-931666-22-9}c"]["optional_attributes"] = ["audience"]
    validation_rules["{urn:isbn:1-931666-22-9}c"]["obligatory_attributes"] = ["id", "level"]
    validation_rules["{urn:isbn:1-931666-22-9}c"]["optional_subelements"] = ["{urn:isbn:1-931666-22-9}c",
                                                                             "{urn:isbn:1-931666-22-9}did",
                                                                             "{urn:isbn:1-931666-22-9}scopecontent",
                                                                             "{urn:isbn:1-931666-22-9}controlaccess",
                                                                             "{urn:isbn:1-931666-22-9}custodhist",
                                                                             "{urn:isbn:1-931666-22-9}arrangement",
                                                                             "{urn:isbn:1-931666-22-9}bibliography",
                                                                             "{urn:isbn:1-931666-22-9}odd",
                                                                             "{urn:isbn:1-931666-22-9}accessrestrict",
                                                                             "{urn:isbn:1-931666-22-9}userestrict",
                                                                             "{urn:isbn:1-931666-22-9}otherfindaid",
                                                                             "{urn:isbn:1-931666-22-9}altformavail",
                                                                             "{urn:isbn:1-931666-22-9}bioghist",
                                                                             "{urn:isbn:1-931666-22-9}dao",
                                                                             "{urn:isbn:1-931666-22-9}daogrp",
                                                                             "{urn:isbn:1-931666-22-9}phystech",
                                                                             "{urn:isbn:1-931666-22-9}index"]
    validation_rules["{urn:isbn:1-931666-22-9}c"]["obligatory_subelements"] = []
    validation_rules["{urn:isbn:1-931666-22-9}c"][
        "max_occurence"] = 2  # maximal erwartetes Auftreten des Elements (None = unbegrenzt)
    validation_rules["{urn:isbn:1-931666-22-9}c"]["text_character_content_allowed"] = False
    validation_rules["{urn:isbn:1-931666-22-9}c"]["tail_character_content_allowed"] = False
    validation_rules["{urn:isbn:1-931666-22-9}c"]["level_occurence"] = ["collection", "class", "series",
                                                                        "subseries", "file", "item"]  # TODO: EAD-spezifisch --> generisch umsetzen (indem etwa eine Attributwert-Bedingung für das Auftreten festgelegt werden kann)

    return validation_rules


def validate(input_file: str, xmlns_def=None, validation_rules=None):
    if xmlns_def is None:
        xmlns_def = {}
    if validation_rules is None:
        validation_rules = compile_example_rules()
        logger.warn("No validation rules defined; using example rules for validation.")
    validation_messages = []

    try:
        xml_in = etree.parse(input_file)
        xml_elements = xml_in.findall("//{*}*")
        for xml_element in xml_elements:
            xml_element_sourceline = xml_element.sourceline  # get original source line before applying normalize-space
            normalize_space.parse_xml_content(xml_element)  # apply normalize-space so only actual character content is found
            assess_element_structure(xml_element, xml_element_sourceline, xmlns_def, validation_rules, validation_messages)
    except etree.XMLSyntaxError:
        logger.error("Input file {} is not a well-formed XML document.".format(input_file))

    # Aggregate and output validation messages
    if len(validation_messages) > 0:
        logger.info("Validation results for file '{}':".format(input_file))
        aggregated_validation_messages = collections.Counter(validation_messages)
        for validation_message in aggregated_validation_messages:
            logger.info(
                "{} ({} occurences)".format(validation_message, aggregated_validation_messages[validation_message]))
