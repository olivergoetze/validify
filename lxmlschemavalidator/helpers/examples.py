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

    # Erweiterung um Enumeration, Pattern, Datentyp und Attribut-Spezifizierung
    validation_rules["{urn:isbn:1-931666-22-9}c"]["allowed_values"] = ["a", "b"]
    validation_rules["{urn:isbn:1-931666-22-9}c"]["allowed_patterns"] = ["regex-pattern 1", "regex-pattern 2"]
    validation_rules["{urn:isbn:1-931666-22-9}c"]["allowed_datatypes"] = ["xs:ID", "xs:TOKEN"]
    validation_rules["{urn:isbn:1-931666-22-9}c"]["attribute_def"] = []
    validation_rules["{urn:isbn:1-931666-22-9}c"]["attribute_def"].append(
        {"attribute_name": "id", "allowed_values": ["a", "b"],
         "allowed_patterns": ["regex-pattern 1", "regex-pattern 2"]})

    # Erweiterung um Bedingung zur Anwendung der Regeln
    validation_rules["{urn:isbn:1-931666-22-9}c"]["rule_conditions"] = {"text_value": "", "attribute_values": [
        {"attribute 1": "value 1", "attribute 2": "value 2"}], "reference_element": {
        "element_name": "{urn:isbn:1-931666-22-9}c", "element_attrib": {"level": "file", "type": "dao"},
        "preceding_elements": 2}}  # mit preceding_elements wird angegeben, wie viele Ebenen das referezierte Element vom zu prüfenden Element entfernt ist. z.B. 2, wenn c/did/unitid geprüft wird und ermittelt werden soll, ob in c das Attribut "level" den Wert "file" enthält.


    return validation_rules