def is_palindrome(text):
    # Replacing all characters except for alphanumeric:
    text = "".join(ch for ch in text if ch.isalpha()).lower()
    if text.replace(' ', '') == text.replace(' ', '')[::-1]:
        return True
    return False


if __name__ == '__main__':
    print(is_palindrome("oppo"))
