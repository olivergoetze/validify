from lxml import etree

def get_rules_from_xml(input_file: str) -> dict:
    # TODO dict-Struktur so beibehalten (allerdings mit validation_rules als list, in das die Rulesets als dict appended werden), allerdings aus XML beziehen und on the fly aufbauen
    rules_in = etree.parse(input_file)
    validation_rules = {}


    return validation_rules
