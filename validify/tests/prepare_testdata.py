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
    ruleset["allowed_patterns"] = ["^test-\\d{4}$", "^test-\\d{3}$"]
    ruleset["allowed_datatypes"] = []
    ruleset["attribute_def"] = []
    ruleset["attribute_def"].append({"attribute_name": "valid_optional_attribute_01", "allowed_values": ["valid_value_01", "valid_value_02"],
                                     "allowed_patterns": ["^test-\\d{4}$", "^test-\\d{3}$"]})
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


    rulesets_subelement = []
    ruleset = {}

    ruleset["element_content_optional"] = False
    ruleset["element_children_optional"] = False
    ruleset["optional_attributes"] = []
    ruleset["obligatory_attributes"] = []
    ruleset["optional_subelements"] = ["child_element"]
    ruleset["obligatory_subelements"] = []
    ruleset["max_occurence"] = None
    ruleset["text_character_content_allowed"] = True
    ruleset["tail_character_content_allowed"] = True

    ruleset["allowed_values"] = []
    ruleset["allowed_patterns"] = []
    ruleset["allowed_datatypes"] = []
    ruleset["attribute_def"] = []
    ruleset["rule_conditions"] = []

    rulesets_subelement.append(ruleset)
    validation_rules["subelement"] = rulesets_subelement


    rulesets_attribute_test = []
    ruleset = {}

    ruleset["element_content_optional"] = True
    ruleset["element_children_optional"] = True
    ruleset["optional_attributes"] = ["valid_optional_attribute"]
    ruleset["obligatory_attributes"] = ["obligatory_attribute"]
    ruleset["optional_subelements"] = []
    ruleset["obligatory_subelements"] = []
    ruleset["max_occurence"] = None
    ruleset["text_character_content_allowed"] = True
    ruleset["tail_character_content_allowed"] = True

    ruleset["allowed_values"] = []
    ruleset["allowed_patterns"] = []
    ruleset["allowed_datatypes"] = []
    ruleset["attribute_def"] = []
    ruleset["rule_conditions"] = []

    rulesets_attribute_test.append(ruleset)
    validation_rules["attribute_test"] = rulesets_attribute_test


    rulesets_parent_element = []
    ruleset = {}

    ruleset["element_content_optional"] = True
    ruleset["element_children_optional"] = True
    ruleset["optional_attributes"] = []
    ruleset["obligatory_attributes"] = []
    ruleset["optional_subelements"] = ["valid_optional_subelement"]
    ruleset["obligatory_subelements"] = ["obligatory_subelement"]
    ruleset["max_occurence"] = None
    ruleset["text_character_content_allowed"] = True
    ruleset["tail_character_content_allowed"] = True

    ruleset["allowed_values"] = []
    ruleset["allowed_patterns"] = []
    ruleset["allowed_datatypes"] = []
    ruleset["attribute_def"] = []
    ruleset["rule_conditions"] = []

    rulesets_parent_element.append(ruleset)
    validation_rules["parent_element"] = rulesets_parent_element


    rulesets_occurence_test = []
    ruleset = {}

    ruleset["element_content_optional"] = True
    ruleset["element_children_optional"] = True
    ruleset["optional_attributes"] = []
    ruleset["obligatory_attributes"] = []
    ruleset["optional_subelements"] = []
    ruleset["obligatory_subelements"] = []
    ruleset["max_occurence"] = 2
    ruleset["text_character_content_allowed"] = True
    ruleset["tail_character_content_allowed"] = True

    ruleset["allowed_values"] = []
    ruleset["allowed_patterns"] = []
    ruleset["allowed_datatypes"] = []
    ruleset["attribute_def"] = []
    ruleset["rule_conditions"] = []

    rulesets_occurence_test.append(ruleset)
    validation_rules["occurence_test"] = rulesets_occurence_test

    rulesets_character_content_test = []
    ruleset = {}

    ruleset["element_content_optional"] = True
    ruleset["element_children_optional"] = True
    ruleset["optional_attributes"] = []
    ruleset["obligatory_attributes"] = []
    ruleset["optional_subelements"] = []
    ruleset["obligatory_subelements"] = []
    ruleset["max_occurence"] = None
    ruleset["text_character_content_allowed"] = False
    ruleset["tail_character_content_allowed"] = False

    ruleset["allowed_values"] = []
    ruleset["allowed_patterns"] = []
    ruleset["allowed_datatypes"] = []
    ruleset["attribute_def"] = []
    ruleset["rule_conditions"] = []

    rulesets_character_content_test.append(ruleset)
    validation_rules["character_content_test"] = rulesets_character_content_test

    rulesets_value_test = []
    ruleset = {}

    ruleset["element_content_optional"] = True
    ruleset["element_children_optional"] = True
    ruleset["optional_attributes"] = ["defined_attribute"]
    ruleset["obligatory_attributes"] = []
    ruleset["optional_subelements"] = []
    ruleset["obligatory_subelements"] = []
    ruleset["max_occurence"] = None
    ruleset["text_character_content_allowed"] = True
    ruleset["tail_character_content_allowed"] = True

    ruleset["allowed_values"] = ["allowed value"]
    ruleset["allowed_patterns"] = []
    ruleset["allowed_datatypes"] = []
    ruleset["attribute_def"] = []
    ruleset["attribute_def"].append({"attribute_name": "defined_attribute", "allowed_values": ["allowed value 01", "allowed value 02"], "allowed_patterns": []})
    ruleset["rule_conditions"] = []

    rulesets_value_test.append(ruleset)
    validation_rules["value_test"] = rulesets_value_test

    rulesets_pattern_test = []
    ruleset = {}

    ruleset["element_content_optional"] = True
    ruleset["element_children_optional"] = True
    ruleset["optional_attributes"] = ["defined_attribute"]
    ruleset["obligatory_attributes"] = []
    ruleset["optional_subelements"] = []
    ruleset["obligatory_subelements"] = []
    ruleset["max_occurence"] = None
    ruleset["text_character_content_allowed"] = True
    ruleset["tail_character_content_allowed"] = True

    ruleset["allowed_values"] = []
    ruleset["allowed_patterns"] = ["^test-\\d{4}$", "^test-\\d{3}$"]
    ruleset["allowed_datatypes"] = []
    ruleset["attribute_def"] = []
    ruleset["rule_conditions"] = []

    rulesets_pattern_test.append(ruleset)
    ruleset["attribute_def"].append(
        {"attribute_name": "defined_attribute", "allowed_values": ["test-1234", "test-123"],
         "allowed_patterns": ["^test-\\d{4}$", "^test-\\d{3}$"]})
    validation_rules["pattern_test"] = rulesets_pattern_test

    return validation_rules