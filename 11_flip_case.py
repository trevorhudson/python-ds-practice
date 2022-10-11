def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    letters = list(phrase)

    for letter in letters:
        if to_swap.lower() == letter.lower():
            if letter.lower() == letter:
                letter = letter.upper()
            else:
                letter = letter.lower()

    return "".join(letters)