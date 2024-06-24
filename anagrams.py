# Given a list of words, return the anagrams only.

# For example given ["HELLO", "STRAP", "WORLD", "CLOUD", "PINS", "SNIP", "PARTS", "COULD", "TRAPS", "STRAP", "NIPS", "SPAN"]

# we should get [["STRAP", "PARTS", "TRAPS"], ["CLOUD", "COULD"], ["PINS", "SNIP", "NIPS"]]

# The order in the individual lists or the full list is immaterial


words = ["HELLO", "STRAP", "WORLD", "CLOUD", "PINS", "SNIP",
         "PARTS", "COULD", "TRAPS", "STRAP", "NIPS", "SPAN"]

def keymaker(s: str) -> str:
    return ''.join(sorted(s))

def anagrams(words: list[str]) -> list[str]:
    candidates = dict()
    for word in words:
        key = keymaker(word)
        if key not in candidates:
            candidates[key] = {word}
        else:
            candidates[key].add(word)
    return [anags for anags in candidates.values() if len(anags)>1]

print(anagrams(words))
