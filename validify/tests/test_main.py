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
        """Parse an xml element without subelements and ensure that the correct validiation message is applied."""

        validation_result = validify.validate("validify/tests/test_rule_element_children_optional.xml", validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 1
        if len(validation_result) > 0:
            assert validation_result[0]["message_id"] == "0001"

    def test_rule_element_content_optional(self):
        """Parse an xml element without element content and ensure that the correct validation message is applied."""

        validation_result = validify.validate("validify/tests/test_rule_element_content_optional.xml",
                                              validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 1
        if len(validation_result) > 0:
            assert validation_result[0]["message_id"] == "0002"

    def test_rule_optional_attributes(self):
        """Parse an xml element with a non-valid attribute and ensure that the correct validation message is applied."""

        validation_result = validify.validate("validify/tests/test_rule_optional_attributes.xml", validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 1
        if len(validation_result) > 0:
            assert validation_result[0]["message_id"] == "0003"

    def test_rule_obligatory_attributes(self):
        """Parse an xml element with a missing obligatory attribute and ensure that the correct validation message is applied."""

        validation_result = validify.validate("validify/tests/test_rule_obligatory_attributes.xml", validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 1
        if len(validation_result) > 0:
            assert validation_result[0]["message_id"] == "0004"

    def test_rule_optional_subelements(self):
        """Parse an xml element with an invalid subelement and ensure that the correct validation message is applied."""

        validation_result = validify.validate("validify/tests/test_rule_optional_subelements.xml",
                                              validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 1
        if len(validation_result) > 0:
            assert validation_result[0]["message_id"] == "0005"

    def test_rule_obligatory_subelements(self):
        """Parse an xml element with a missing obligatory subelement and ensure that the correct validation message is applied."""

        validation_result = validify.validate("validify/tests/test_rule_obligatory_subelements.xml",
                                              validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 1
        if len(validation_result) > 0:
            assert validation_result[0]["message_id"] == "0006"

    def test_rule_max_occurence(self):
        """Parse an xml element which occurs more often than allowed, and ensure that the correct validation message is applied."""

        validation_result = validify.validate("validify/tests/test_rule_max_occurence.xml",
                                              validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 3
        if len(validation_result) == 3:
            assert validation_result[0]["message_id"] == "0007"
            assert validation_result[1]["message_id"] == "0007"
            assert validation_result[2]["message_id"] == "0007"

    def test_rule_character_content_allowed(self):
        """Parse an xml element which has character content (while not allowed in the rule definition) and ensure that the correct validation message is applied."""

        validation_result = validify.validate("validify/tests/test_rule_character_content_allowed.xml",
                                              validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 2
        if len(validation_result) == 2:
            assert validation_result[0]["message_id"] == "0008"
            assert validation_result[1]["message_id"] == "0009"


    def test_rule_allowed_values(self):
        """Parse an xml element which has an invalid text value and ensure that the correct validation message is applied."""

        validation_result = validify.validate("validify/tests/test_rule_allowed_values.xml",
                                              validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 1
        if len(validation_result) > 0:
            assert validation_result[0]["message_id"] == "0010"

    def test_rule_allowed_patterns(self):
        """Parse an xml element with a text value not compliant to the provided regexpattern, and ensure that the correct validation message is applied."""

        validation_result = validify.validate("validify/tests/test_rule_allowed_patterns.xml",
                                              validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 0

    def test_attribute_definition_allowed_values(self):
        """Parse an xml element with a non-allowed attribute value, and ensure that the correct validation message is applied."""

        validation_result = validify.validate("validify/tests/test_attribute_definition_allowed_values.xml",
                                              validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 1
        if len(validation_result) > 0:
            assert validation_result[0]["message_id"] == "0012"


    def test_attribute_definition_allowed_patterns(self):
        """Parse an xml element with an attribute value not compliant to the provided regexpattern, and ensure that the correct validation message is applied."""

        validation_result = validify.validate("validify/tests/test_attribute_definition_allowed_patterns.xml",
                                              validation_rules=compile_test_rules(), log_to_console=False)
        assert len(validation_result) == 2
        if len(validation_result) == 2:
            assert validation_result[0]["message_id"] == "0012"
            assert validation_result[1]["message_id"] == "0013"