def is_palindrome(text):
    """
    This function checks if the given text is a palindrome.
    :param text: Input string to check if it is a palindrome.
    :return: Returns True if the text is a palidrome and False otherwise.
    """
    # Replacing all characters except for alphanumeric:
    text = "".join(ch for ch in text if ch.isalpha()).lower()
    if text.replace(' ', '') == text.replace(' ', '')[::-1]:
        return True
    return False


if __name__ == '__main__':
    print(is_palindrome("oppo"))
