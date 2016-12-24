di = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидемся"}

def get_answer(k,d):
	return d[k.lower()]

value = get_answer("ПОКА", di)
print(value)