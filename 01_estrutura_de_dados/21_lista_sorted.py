frutas = ["morango", "uva", "laranja", "cereja", "banana", "mamão", "maçã"]

print(sorted(frutas, key=lambda x: len(x)))
print(sorted(frutas, key=lambda x: len(x), reverse=True))

#ordem alfabética
