# Document Similarity Detection Using SimHash

## Project Description

This project implements the SimHash technique to measure the similarity
between two web documents.

The program downloads two webpages, processes their content,
and generates a 64-bit fingerprint (SimHash) for each document.
It then compares both fingerprints to determine how similar the documents are.

---

## Purpose

The aim of this project is to understand:

- How document similarity is calculated
- How hashing is used in Information Retrieval
- How near-duplicate pages can be detected

---

## Major Steps Involved

### 1. Fetch Webpage Content
The body text of both URLs is extracted.

### 2. Word Processing
- Convert text to lowercase
- Extract alphanumeric words
- Count frequency of each word

### 3. Rolling Hash
Each word is converted into a 64-bit hash using
polynomial rolling hash with:
- p = 53
- m = 2^64

### 4. SimHash Generation
- Initialize a vector of size 64
- For each word:
  - Add frequency if bit is 1
  - Subtract frequency if bit is 0
- Convert vector into final binary fingerprint

### 5. Similarity Comparison
Compare both 64-bit fingerprints bit-by-bit.
Count how many bits are identical.

---

## How Similarity is Measured

If two documents are similar, their SimHash values will differ
only in a few bit positions.

More matching bits = Higher similarity.

---

## Sample Output
