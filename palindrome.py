def is_palindrome(text):
    """

    :param text:
    :return:
    """
    # Function checks if given string 'text' is palindrome
    # It return True if given word is palindrome and False otherwise 
    
    # Replacing all characters except for alphanumeric:
    text = "".join(ch for ch in text if ch.isalpha()).lower()
    if text.replace(' ', '') == text.replace(' ', '')[::-1]:
        return True
    return False


if __name__ == '__main__':
    print(is_palindrome("oppo"))
