import sys
import requests
import re
from bs4 import BeautifulSoup
HEADERS = {"User-Agent": "Mozilla/5.0 (Educational crawler for SEIR course)"}

# Get body text from URL
def get_body_text(url):
    
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    if soup.body:
        return soup.body.get_text()
    return ""

# Extract words from text (Only alphanumeric words)
def extract_words(text):
    text = text.lower()
    words = re.findall(r"[a-z0-9]+", text)
    return words


# Count word frequencies
def word_freq(words):
    word_dict = {}
    for w in words:
        if w in word_dict:
            word_dict[w] += 1
        else:
            word_dict[w] = 1
    return word_dict

# Polynomial Rolling Hash (64-bit)
def word_hash(word):
    p = 53
    m = 2**64

    hash_value = 0
    power = 1
    for ch in word:
        hash_value += ord(ch) * power
        power *= p

    return hash_value % m


# Compute SimHash fingerprint
def simhash(word_dict):
    arr = [0] * 64   # vector of 64 positions

    for word, count in word_dict.items():
        hash_value = word_hash(word)

        for i in range(64):
            bit = (hash_value >> i) & 1
            if bit == 1:
                arr[i] += count
            else:
                arr[i] -= count

    # Build final fingerprint from vector
    fingerprint = 0
    for i in range(64):
        if arr[i] >= 0:
            fingerprint |= (1 << i)

    return fingerprint


# Count common bits between two hashes
def common_bits(hash1, hash2):
    count = 0

    for i in range(64):
        b1 = (hash1 >> i) & 1
        b2 = (hash2 >> i) & 1
        if b1 == b2:
            count += 1

    return count

# MAIN PROGRAM
if len(sys.argv) < 3:
    print("No valid url givel")
    sys.exit(1)

url1 = sys.argv[1]
url2 = sys.argv[2]

print("\nFetching documents...\n")

# Get body text
text1 = get_body_text(url1)
text2 = get_body_text(url2)

# Extract words
words1 = extract_words(text1)
words2 = extract_words(text2)

# Word frequency dictionaries
freq1 = word_freq(words1)
freq2 = word_freq(words2)

print("Document 1 total words:", len(words1))
print("Document 2 total words:", len(words2))

# Compute SimHash fingerprints
hash1 = simhash(freq1)
hash2 = simhash(freq2)

# Compare common bits
same_bits = common_bits(hash1, hash2)

# FINAL OUTPUT
print()
print("SIMHASH RESULTS")

print("\nURL 1:", url1)
print("SimHash 1:", hash1)

print("\nURL 2:", url2)
print("SimHash 2:", hash2)

print("\nCommon Bits (out of 64):", same_bits)
print("Similarity Percentage:", (same_bits / 64) * 100, "%")



# I download two webpages, extract words, count frequencies, compute SimHash fingerprints
# using rolling hash and weighted bit voting, then compare both documents by counting common bits.
