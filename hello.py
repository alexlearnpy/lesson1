catalog_item = {
	"type": "phone",
	"vendor": "Apple",
	"model": "iPhone 7 black",
	"price": 37.5
}
catalog_item['audio_jack'] = False
catalog_item['price'] = 70

del catalog_item['price']
print(catalog_item)