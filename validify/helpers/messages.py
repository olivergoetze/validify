def get_message_by_id(message_id: str, lang: str="de") -> str:
    if lang == "de":
        if message_id == "0001":
            message_str = "Element {} enthält keine Subelemente, obwohl eines oder mehrere Subelemente erwartet."
        elif message_id == "0002":
            message_str = "Element {} enthält keinen Elementinhalt, obwohl das Element nicht leer sein darf."
        elif message_id == "0003":
            message_str = "Element {} enthält ein nicht erwartetes Attribut: {}"
        elif message_id == "0004":
            message_str = "Element {} enthält nicht das Pflicht-Attribut {}."
        elif message_id == "0005":
            message_str = "Element {} enthält ein nicht erwartetes Subelement: {}."
        elif message_id == "0006":
            message_str = "Element {} enthält nicht das Pflicht-Subelement {}."
        elif message_id == "0007":
            message_str = "Element {} ist {} mal vorhanden, erwartet wird jedoch nur {} Vorkommen."
        elif message_id == "0008":
            message_str = "Element {} should not contain text character content."
        elif message_id == "0009":
            message_str = "Element {} should not contain tail character content."
        elif message_id == "0010":
            message_str = "{} -- Element value not eqal to required value: '{}' != '{}'"
        elif message_id == "0011":
            message_str = "{}, attribute {} -- attribute value not eqal to required value: '{}' != '{}'"
        else:
            message_str = ""
    else:
        if message_id == "0001":
            message_str = ""
        else:
            message_str = ""

    return message_str
