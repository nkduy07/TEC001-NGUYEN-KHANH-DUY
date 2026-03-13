def check_word_frequency(text):
    words = text.lower().split()
    total_count = len(words)

    if total_count == 0:
        return "Empty"

    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    top_5 = sorted_items[:5]

    top_5_sum = sum(item[1] for item in top_5)

    proportion = (top_5_sum / total_count) * 100

    return dict(top_5), total_count, top_5_sum, proportion

text = input("Enter text: ")
result = check_word_frequency(text)
top_5_dict, total_words, top_5_sum, proportion = result

print(f"Top 5: {top_5_dict}")
print(f"Total number of words: {total_words}")
print(f"Proportion of 5 most common words: {top_5_sum} / {total_words} = {proportion:.2f}%")