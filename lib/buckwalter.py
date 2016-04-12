buck2uni = {
"'": b"\\u0621", # hamza-on-the-line
"|": b"\\u0622", # madda
">": b"\\u0623", # hamza-on-'alif
"&": b"\\u0624", # hamza-on-waaw
"<": b"\\u0625", # hamza-under-'alif
"}": b"\\u0626", # hamza-on-yaa'
"A": b"\\u0627", # bare 'alif
"b": b"\\u0628", # baa'
"p": b"\\u0629", # taa' marbuuTa
"t": b"\\u062a", # taa'
"v": b"\\u062b", # thaa'
"j": b"\\u062c", # jiim
"H": b"\\u062d", # Haa'
"x": b"\\u062e", # khaa'
"d": b"\\u062f", # daal
"*": b"\\u0630", # dhaal
"r": b"\\u0631", # raa'
"z": b"\\u0632", # zaay
"s": b"\\u0633", # siin
"$": b"\\u0634", # shiin
"S": b"\\u0635", # Saad
"D": b"\\u0636", # Daad
"T": b"\\u0637", # Taa'
"Z": b"\\u0638", # Zaa' (DHaa')
"E": b"\\u0639", # cayn
"g": b"\\u063a", # ghayn
"_": b"\\u0640", # taTwiil
"f": b"\\u0641", # faa'
"q": b"\\u0642", # qaaf
"k": b"\\u0643", # kaaf
"l": b"\\u0644", # laam
"m": b"\\u0645", # miim
"n": b"\\u0646", # nuun
"h": b"\\u0647", # haa'
"w": b"\\u0648", # waaw
"Y": b"\\u0649", # 'alif maqSuura
"y": b"\\u064a", # yaa'
"F": b"\\u064b", # fatHatayn
"N": b"\\u064c", # Dammatayn
"K": b"\\u064d", # kasratayn
"a": b"\\u064e", # fatHa
"u": b"\\u064f", # Damma
"i": b"\\u0650", # kasra
"~": b"\\u0651", # shaddah
"o": b"\\u0652", # sukuun
"`": b"\\u0670", # dagger 'alif
"{": b"\\u0671", # waSla
}

uni2buck = dict()
for key, value in buck2uni.items():
    uni2buck[value] = key
