sentence = """У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил."""

# print(len(sentence))

words = sentence.split()

# new_words = []
# for word in words:
#     word = word.lower().rstrip(".,!?;…:")
#     new_words.append(word)

words = [word.lower().rstrip(".,!?;…:") for word in words]
words = [word for word in words if word.isalpha()]


# walrus (:=) — моржовый оператор
# new_words = [nw for w in words if (nw := w.lower().rstrip(".,!?;…:")).isalpha()]


def has_double_letter(word):
    return any(letter * 2 in word for letter in set(word))


def has_three_consonants_in_a_row(word):
    for i in range(len(word) - 2):
        if all(c not in "ёуеыаоэяию" for c in word[i : i + 3]):
            return True
    return False


def has_three_consonants_in_a_row(word):
    return any(
        all(c not in "ёуеыаоэяию" for c in word[i : i + 3])
        for i in range(len(word) - 2)
    )


import re


def has_three_consonants_in_a_row(word):
    return bool(re.match("([^о]*о){3}[^о]*", word))


# ...о...о...о...

# def has_double_letter(word):
#     for i in range(len(word) - 1):
#         if word[i] == word[i + 1]:
#             return True
#     return False


one_letter_words = [word for word in words if len(word) == 1]
it_verbs = [w for w in words if w.endswith("ит")]
words_with_yo = [w for w in words if "ё" in w]
double_letter_words = [w for w in words if has_double_letter(w)]
double_letter_words_2 = list(filter(has_double_letter, words))
words_with_three_o = [w for w in words if w.count("о") == 3]
words_with_at_least_3_o = [w for w in words if w.count("о") >= 3]
words_with_3_consonants = [
    w for w in words if sum(letter not in "ёуеыаоэяию" for letter in w) == 3
]


# it_verbs = [w for w in words if w[-2:] == "ит"]

# print(words)
# print(one_letter_words)
# print(it_verbs)
# print(words_with_yo)
# print(double_letter_words)
# print(double_letter_words_2)
# print(words_with_three_o)
# print(words_with_at_least_3_o)
# print(words_with_3_consonants)
# print([w for w in words if has_three_consonants_in_a_row(w)])


def count_vowels(word):
    return sum(c in "ёуеаоэяию" for c in word)


def count_consonants(word):
    return sum(c not in "ёуеаоэяию" for c in word)


print(min(words))
print(max(words))
print(sorted(set(words)))
print(len(set(words)))
print(len(words))
print(max(words, key=len))
print(max(words, key=count_vowels))
print(max(words, key=count_consonants))
print(max(words, key=lambda word: len(set(word))))

print([w for w in words if len(set(w)) != len(w)])

print([w[::-1] for w in words[:10]])
print(" ".join(w[::-1] for w in words[:10]))
print("—".join(w[::-1] for w in words[:10]))
