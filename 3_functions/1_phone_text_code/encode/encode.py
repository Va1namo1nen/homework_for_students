def encode_text(message: str) -> str | None:
    """Функция для кодирования текста в числовой формат."""
    char_to_code_map = build_char_to_code_map()

    encoded_message = []
    try:
        for char in message:
            encoded_message.append(char_to_code_map[char])
        return " ".join(encoded_message)
    except KeyError:
        return None


def build_char_to_code_map() -> dict[str, str]:
    """Создает отображение символов в коды."""
    characters = create_characters()
    codes = create_codes()
    return {char: code for char, code in zip(characters, codes)}


def create_codes() -> list[str]:
    """Генерирует все возможные коды для символов."""
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
    """Создает список символов для кодирования."""
    punctuation = [" ", ".", ",", "?", "!", ":", ";"]
    russian_letters = [chr(i) for i in range(1072, 1104)]  # Символы русского алфавита
    return punctuation + russian_letters