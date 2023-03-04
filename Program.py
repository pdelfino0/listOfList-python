list = ["I study at PUCRS",
        "SQL is a programming language used in relational database",
        "a NoSQL or non-relational database, allow unstructured data to be manipulated"
        ]

tokens = []
for sentence in list:
    tokens.append(sentence.split())

for sentence in tokens:
    print(f"Words of the sentence: {sentence}")
    for word in sentence:
        print(word)

