def word_frequency(text):
    freq = {}

    words = text.split()

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq
text = "apple banana apple orange banana apple"

result = word_frequency(text)

print(result)
