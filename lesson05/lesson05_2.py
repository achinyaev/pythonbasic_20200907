import json

data = {
    'one': 'HELLO',
    'TWO': [1,2,3,4,'ququ'],
    1: False,
    2: True,
    3: None,
    'tut': (1, 2, 3),
    'cyr_text': "ХЕЛЛО ЧУВАК",
    5: '7',
    6: {1:6,2:7,3:8,4:9} # set не трансформируется
}

j_data = json.dumps(data, ensure_ascii=False)

print(j_data)

enc_data = json.loads(j_data)
print((type(enc_data)))
print(enc_data)

j_data = json.dumps(data, ensure_ascii=False)
with open('test.json', 'w', encoding="UTF-8") as file:
    json.dump(data, file, ensure_ascii=False)
print(j_data)