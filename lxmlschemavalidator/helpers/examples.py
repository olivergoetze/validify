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