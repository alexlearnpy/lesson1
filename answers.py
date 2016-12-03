di = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидемся"}

def get_answer(k,d):
	return d[k]

value = get_answer("как дела", di)
print(value)