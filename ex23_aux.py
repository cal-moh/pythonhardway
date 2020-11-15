# bytearray = "Afrikaans"
with open("languages4.txt", 'wb') as f:
	f.write(bytearray("Afrikaans", encoding='utf-8'))
