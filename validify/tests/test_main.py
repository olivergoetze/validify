import validify
from validify.tests.prepare_testdata import compile_test_rules

class TestElementStructureAsssessment:
    """Test functions for execution with pytest.

    A test is provided for each xml rule assertion implemented in validify.py.
    Validation rules for testing are provided by validify.tests.prepare_testdata.compile_test_rules.
    For each test, a xml input file is provided in the 'tests' directory.
    To execute all tests, run 'pytest" command from the root directory.
    """

    def test_ruleset_condition_text_values(self):
        """Parse an xml element with an invalid text value and check if the validation rule is rightly skipped.

        These tests starting with "test_ruleset_condition" are meant to assert whether the conditions set for applying a ruleset are correctly evaluated.
        """

        validation_result = validify.validate("validify/tests/test_rule_condition_text_values.xml", validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 0

    def test_ruleset_condition_attribute_values(self):
        """Parse an xml element with an invalid attribute value and check if the validation rule is skipped correctly.

        These tests starting with "test_ruleset_condition" are meant to assert whether the conditions set for applying a ruleset are correctly evaluated.
        """

        validation_result = validify.validate("validify/tests/test_rule_condition_attribute_values.xml",
                                              validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 0

    def test_ruleset_condition_reference_elements(self):
        """Parse an xml element where the conditions for the defined reference element are not met and check if the validation rule is rightly skipped.

        These tests starting with "test_ruleset_condition" are meant to assert whether the conditions set for applying a ruleset are correctly evaluated.
        """

        validation_result = validify.validate("validify/tests/test_rule_condition_reference_elements.xml", validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 0

    def test_rule_element_children_optional(self):
        validation_result = validify.validate("validify/tests/test_rule_element_children_optional.xml", validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 1
        if len(validation_result) > 0:
            assert validation_result[0]["message_id"] == "0001"

    def test_rule_element_content_optional(self):
        validation_result = validify.validate("validify/tests/test_rule_element_content_optional.xml",
                                              validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 1
        if len(validation_result) > 0:
            assert validation_result[0]["message_id"] == "0002"

    def test_rule_optional_attributes(self):
        validation_result = validify.validate("validify/tests/test_rule_optional_attributes.xml", validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 1
        if len(validation_result) > 0:
            assert validation_result[0]["message_id"] == "0003"

    def test_rule_obligatory_attributes(self):
        validation_result = validify.validate("validify/tests/test_rule_obligatory_attributes.xml", validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 1
        if len(validation_result) > 0:
            assert validation_result[0]["message_id"] == "0004"

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