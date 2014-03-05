def justify(string, width, justification):
    """
    string - desired string to print
    width - width (in characters) of the space to drop the string
    justification - Either 'left', 'right', or 'center'.
    """
    if string is None:
        string = ""

    string = str(string)
    justification = justification.lower()

    assert width>0
    assert justification in ['left', 'right', 'center']

    string_shorter = string[:width]
    if justification == 'right':
        string_shorter = string[-width:]

    lstr = len(string_shorter)
    spaces_needed = width - lstr

    if justification == 'right':
        return ' '*spaces_needed + string_shorter

    if justification == 'left':
        return string_shorter + ' '*spaces_needed

    left_spaces = int(spaces_needed/2)
    right_spaces = int(spaces_needed/2)

    if left_spaces+right_spaces < spaces_needed:
        right_spaces += 1

    return ' '*left_spaces +string_shorter+ ' '*right_spaces
