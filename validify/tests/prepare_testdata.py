def compile_test_rules() -> dict:
    """Compile example validation rules.

    These rules are applied when no ruleset is given as a parameter to validify.validate.
    Also used as test rules for pytest functions in test_main.py
    """

    validation_rules = {"element": []}
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

    return validation_rules