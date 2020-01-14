import validify
from validify.tests.prepare_testdata import compile_test_rules

class TestElementStructureAsssessment:

    def test_rule_condition_text_values(self):
        validation_result = validify.validate("validify/tests/test_rule_condition_text_values.xml", validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 0

    def test_rule_condition_attribute_values(self):
        validation_result = validify.validate("validify/tests/test_rule_condition_attribute_values.xml",
                                              validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 0

    def test_rule_condition_reference_elements(self):
        validation_result = validify.validate("validify/tests/test_rule_condition_reference_elements.xml", validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 0


    def test_rule_element_children_optional(self):
        pass

    def test_rule_element_content_optional(self):
        pass


    def test_rule_optional_attributes(self):
        pass

    def test_rule_obligatory_attributes(self):
        pass


    def test_rule_optional_subelements(self):
        pass

    def test_rule_obligatory_subelements(self):
        pass


    def test_rule_max_occurence(self):
        pass

    def test_rule_character_content_allowed(self):
        pass

    def test_rule_allowed_values(self):
        pass

    def test_rule_allowed_patterns(self):
        pass



    def test_attribute_definition_allowed_values(self):
        pass

    def test_attribute_definition_allowed_patterns(self):
        pass