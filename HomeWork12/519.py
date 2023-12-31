string = "Project Gutenberg offers over 59,000 free eBooks"
letters = 0
digits = 0

for i in string:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1

print("LETTERS", letters)
print("DIGITS", digits)

# Я почав називати зміни нормально
# а не однією буквою і я це кажу щоб
# ви не подумали що я використовую ChatGPT