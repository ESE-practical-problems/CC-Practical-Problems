# --- Input Text ---
text = """
MapReduce is simple. MapReduce is powerful.
"""

# --- Map Step ---
words = text.lower().replace('.', '').split()
mapped = [(word, 1) for word in words]

# --- Shuffle Step ---
shuffled = {}
for word, count in mapped:
    if word not in shuffled:
        shuffled[word] = []
    shuffled[word].append(count)

# --- Reduce Step ---
reduced = {}
for word, counts in shuffled.items():
    reduced[word] = sum(counts)

# --- Output Step ---
for word, count in reduced.items():
    print(f"{word}: {count}")
