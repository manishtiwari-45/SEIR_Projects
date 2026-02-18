import sys
import requests
import re
from bs4 import BeautifulSoup


def get_body_text(url):

    HEADERS = {"User-Agent": "Mozilla/5.0"}
    responses = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(responses.text, "html.parser")

    if soup.body:
        return soup.body.get_text()
    return ""


def extract_words(text):
    text = text.lower()
    words  = re.findall(r"[a-z0-9]+", text)
    return words

def word_freq(words):
    freq = {}
    for w in words:
        if w in freq:
            freq[w]+=1
        else:
            freq[w] = 1
    return freq


    
def word_hash(word):
    p = 53;
    m = 2**64

    hash_value = 0
    power = 1

    for ch in word:
        hash_value += ord(ch)*power
        power = power*p
    
    return hash_value % m


def simhash(freq_dict):
    vector = [0]*64

    for word, count in freq_dict.items():
        h = word_hash(word)

        for i in range(64):
            bit = (h >> i) & 1

            if bit == 1:
                vector[i] += count
            else:
                vector[i] -= count
    

    fingerprint = 0
    for i in range(64):
        if vector[i] >= 0:
            fingerprint |= (1 << i)
    
    return fingerprint

def common_bits(h1,h2):
    count = 0

    for i in range(64):
        b1 = (h1>>i) & 1
        b2 = (h2>>i) & 1

        if b1 == b2:
            count += 1
    return count

if len(sys.argv) < 3:
    print("No 2 url found!! Try again.")
    sys.exit(1)

url1 = sys.argv[1]
url2 = sys.argv[2]

text1 = get_body_text(url1)
text2 = get_body_text(url2)



words1 = extract_words(text1)
words2 = extract_words(text2)


freq1 = word_freq(words1)
freq2 = word_freq(words2)

hash1 = simhash(freq1)
hash2 = simhash(freq2)

print("Total text length of page 1:", len(text1), "and page 2:",len(text2))
print("Number of words in page 1:", len(words1), "and page 2:",len(words2))


print("SimHash 1:", hash1)
print("SimHash 2:", hash2)

print("Common bits:", common_bits(hash1, hash2))
