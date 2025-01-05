def decode_numbers(codes: str) -> str | None:
    code_to_char_map = build_code_to_char_map()

    decoded_chars = []
    try:
        for code in codes.split():
            decoded_chars.append(code_to_char_map[code])
        return ''.join(decoded_chars)
    except KeyError:
        return None

def build_code_to_char_map() -> dict[str, str]:
    number_codes = create_codes()
    characters = create_characters()
    return {code: char for code, char in zip(number_codes, characters)}

def create_codes() -> list[str]:
    codes = ["0"]
    for num in range(1, 10):
        if num == 1:
            for length in range(1, 7):
                codes.append(str(num) * length)
        else:
            for length in range(1, 5):
                codes.append(str(num) * length)
    return codes

def create_characters() -> list[str]:
    punctuation = [" ", ".", ",", "?", "!", ":", ";"]
    russian_letters = [chr(i) for i in range(1072, 1104)]  # Символы русского алфавита
    return punctuation + russian_letters
