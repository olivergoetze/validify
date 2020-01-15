def get_message_by_id(message_id: str, lang: str="de") -> str:
    """Return validation message string by id."""

    if lang == "de":
        if message_id == "0001":
            message_str = "Element {} enthält keine Subelemente, obwohl eines oder mehrere Subelemente erwartet."
        elif message_id == "0002":
            message_str = "Element {} enthält keinen Elementinhalt, obwohl das Element nicht leer sein darf."
        elif message_id == "0003":
            message_str = "Element {} enthält ein nicht erwartetes Attribut: {}."
        elif message_id == "0004":
            message_str = "Element {} enthält nicht das Pflicht-Attribut {}."
        elif message_id == "0005":
            message_str = "Element {} enthält ein nicht erwartetes Subelement: {}."
        elif message_id == "0006":
            message_str = "Element {} enthält nicht das Pflicht-Subelement {}."
        elif message_id == "0007":
            message_str = "Element {} ist {} mal vorhanden, erwartet wird jedoch nur {} Vorkommen."
        elif message_id == "0008":
            message_str = "Element {} darf keinen Text (Character Content) im Elementinhalt enthalten."
        elif message_id == "0009":
            message_str = "Element {} darf keinen Text (Character Content) vor dem Folgeelement (Tail) enthalten."
        elif message_id == "0010":
            message_str = "Element {}: Tatsächlicher Elementwert entspricht nicht den zulässigen Werten: '{}' != '{}'."
        elif message_id == "0011":
            message_str = "Element {}: Tatsächlicher Elementwert entspricht nicht den zulässigen Patterns: '{}' != '{}'."
        elif message_id == "0012":
            message_str = "Element {}, Attribut {}: Tatsächlicher Attributwert entspricht nicht den zulässigen Werten: '{}' != '{}'."
        elif message_id == "0013":
            message_str = "Element {}, Attribut {}: Tatsächlicher Attributwert entspricht nicht den zulässigen Patterns: '{}' != '{}'."
        else:
            message_str = ""
    else:
        if message_id == "0001":
            message_str = "Element {} does not contain any subelements, although one or more subelements are expected."
        elif message_id == "0002":
            message_str = "Element {} does not contain any text, although it is not expected to be empty."
        elif message_id == "0003":
            message_str = "Element {} contains an unexpected attribute: {}."
        elif message_id == "0004":
            message_str = "Element {} misses the mandatory attribute {}."
        elif message_id == "0005":
            message_str = "Element {} contains an unexpected subelement: {}."
        elif message_id == "0006":
            message_str = "Element {} misses the mandatory subelement {}."
        elif message_id == "0007":
            message_str = "Element {} occurs {} times, though it is expected to occur only {} times."
        elif message_id == "0008":
            message_str = "Element {} should not contain text character content."
        elif message_id == "0009":
            message_str = "Element {} should not contain tail character content."
        elif message_id == "0010":
            message_str = "Element {}: Element value not eqal to allowed values: '{}' != '{}'"
        elif message_id == "0011":
            message_str = "Element {}: Element value not valid according to allowed patterns: '{}' != '{}'"
        elif message_id == "0012":
            message_str = "Element {}, attribute {}: attribute value not eqal to required value: '{}' != '{}'"
        elif message_id == "0013":
            message_str = "Element {}, attribute {}: attribute value not valid according to allowed patterns: '{}' != '{}'"
        else:
            message_str = ""

    return message_str
