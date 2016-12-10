def get_vat(payment):
	try:
		payment = float(payment)
		vat = payment / 100 * 18
		vat = round(vat, 2)
		return 'Сумма НДС: {}'.format(vat)
	except (TypeError, ValueError):
		return "Не могу посчитать, проверьте вводимые данные"


result = get_vat('76')
print(result)

