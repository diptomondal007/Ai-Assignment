import pandas as pd

df = pd.read_csv("dataset/next_word.csv")

input_word = input("type your word: ")

df_search = df.loc[df['word1'] == input_word]

new_df = pd.DataFrame(columns=["word1", "word2", "freqs"])
#print(new_df)

freqs_to_left = 0
freqs_to_right = 0

max_val = 0

result = ''

for index, row in df_search.iterrows():
    freqword = 0
    cols_for_word2 = df.loc[df['word2'] == row['word2']]
    for freq in cols_for_word2.freqs:
        freqword += freq
    freqs_to_right += freqword
    freqs_to_left += int(row['freqs'])

score = 0

for index, row in df_search.iterrows():
    looking_for_1 = df.loc[(df['word1'] == input_word) & (df['word2'] == row['word2'])]
    freq1 = 0
    for freq in looking_for_1.freqs:
        freq1 += int(freq)

    freq2 = 0
    looking_for_2 = df.loc[df['word2'] == row['word2']]
    for freq in looking_for_2.freqs:
        freq2 += int(freq)

    p1 = freq1 / freq2
    p2 = freq2 / freqs_to_right
    p3 = freqs_to_left / freqs_to_right

    score = (p1 * p2) / p3
    if score > max_val:
        max_val = score
        result = row['word2']

print(result)
print("With score:")
print(max_val)