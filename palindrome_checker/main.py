with open('./input.txt', 'r') as f:
  input = f.read()
text=input.strip().replace(" ", "").lower().split("\n")
for i in text:
    words.append(i)
words=[]
alfanumeric="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".lower()
characters=[]
alfanumeric_count=[]

#palindrome check
same=0
palindromes=[]
for word in words:
    for i in range(len(word)):
        if word[i]==word[-i-1]:
            same+=1
    if same==len(word):
        palindromes.append(word)
    same=0

#alfanumerics count
for i in words:
    for x in range(len(i)):
        if i[x] in alfanumeric and i[x] not in characters:
            characters.append(i[x])
    alfanumeric_count.append(len(characters))
    characters=[]
for i in range(len(words)-1):
    if words[i] in palindromes:
        print(f"YES {alfanumeric_count[i]}")
    else:
        print(f"NO {alfanumeric_count[i]}")
