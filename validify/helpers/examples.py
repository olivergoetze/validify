def compile_example_rules() -> dict:
    """Compile example validation rules.

    These rules are applied when no ruleset is given as a parameter to validify.validate.
    """

    validation_rules = {}

    validation_rules["{urn:isbn:1-931666-22-9}c"] = []
    ruleset = {}

    ruleset["element_content_optional"] = True  # Element darf auch ohne Content auftreten
    ruleset["element_children_optional"] = False  # Element darf auch ohne Kindelemente auftreten
    ruleset["optional_attributes"] = ["audience"]
    ruleset["obligatory_attributes"] = ["id", "level"]
    ruleset["optional_subelements"] = ["{urn:isbn:1-931666-22-9}c", "{urn:isbn:1-931666-22-9}did", "{urn:isbn:1-931666-22-9}scopecontent", "{urn:isbn:1-931666-22-9}controlaccess", "{urn:isbn:1-931666-22-9}custodhist", "{urn:isbn:1-931666-22-9}arrangement", "{urn:isbn:1-931666-22-9}bibliography", "{urn:isbn:1-931666-22-9}odd", "{urn:isbn:1-931666-22-9}accessrestrict", "{urn:isbn:1-931666-22-9}userestrict", "{urn:isbn:1-931666-22-9}otherfindaid", "{urn:isbn:1-931666-22-9}altformavail", "{urn:isbn:1-931666-22-9}bioghist", "{urn:isbn:1-931666-22-9}dao", "{urn:isbn:1-931666-22-9}daogrp", "{urn:isbn:1-931666-22-9}phystech", "{urn:isbn:1-931666-22-9}index"]
    ruleset["obligatory_subelements"] = []
    ruleset["max_occurence"] = 2  # maximal erwartetes Auftreten des Elements (None = unbegrenzt)
    ruleset["text_character_content_allowed"] = False
    ruleset["tail_character_content_allowed"] = False

    # Erweiterung um Enumeration, Pattern, Datentyp und Attribut-Spezifizierung
    ruleset["allowed_values"] = ["a", "b"]
    ruleset["allowed_patterns"] = ["^DE-\d{4}$", "regex-pattern 2"]
    ruleset["allowed_datatypes"] = ["xs:ID", "xs:TOKEN"]
    ruleset["attribute_def"] = []
    ruleset["attribute_def"].append({"attribute_name": "id", "allowed_values": ["a", "b"], "allowed_patterns": ["regex-pattern 1", "regex-pattern 2"]})
    ruleset["attribute_def"].append({"attribute_name": "level", "allowed_values": ["collection", "class", "series", "file", "item"], "allowed_patterns": []})

    # Erweiterung um Bedingung zur Anwendung der Regeln
    ruleset["rule_conditions"] = []
    # ruleset["rule_conditions"].append({"text_values": ["DE-1234"], "attribute_def": [{"attribute_name": "name 1", "allowed_values": ["value 1"]}], "reference_elements": [{"element_name": "{urn:isbn:1-931666-22-9}c", "attribute_def": [{"attribute_name": "level", "allowed_values": ["class", "series"]}],"preceding_elements": 2}]})  # mit preceding_elements wird angegeben, wie viele Ebenen das referezierte Element vom zu prüfenden Element entfernt ist. z.B. 2, wenn c/did/unitid geprüft wird und ermittelt werden soll, ob in c das Attribut "level" den Wert "file" enthält.

    validation_rules["{urn:isbn:1-931666-22-9}c"].append(ruleset)



    return validation_rules