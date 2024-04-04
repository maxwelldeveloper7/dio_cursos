"""implements text formatting"""
def own_name(full_name: str) -> str:
    """
    Format a full name according to the established rules.

    Parameters:
        full_name (str): The full name to be formatted.

    Returns:
        str: The formatted name.

    Description:
        This function converts the full name to lowercase and then applies the title()
        method to capitalize the first letter of each word, and replaces the occurrences
        of prepositions with the same words in lowercase, preserving the originality
        of the proper name.

    Example:
        >>> own_name("JOÃO DA SILVA")
        'João da Silva'
        >>> own_name("MARIA DOS SANTOS")
        'Maria dos Santos'
    """
    name_formated = full_name.lower().title()
    name_formated = (
        name_formated.replace(" De ", " de ")
        .replace(" Da ", " da ")
        .replace(" Das ", " das ")
        .replace(" Do ", " do ")
        .replace(" Dos ", " dos ")
    )
    return name_formated

if __name__ == '__main__':
    pass
