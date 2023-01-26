number_words = {}
number_words[8] = "Eight"
number_words[41] = "FortyOne"
number_words[8] = "Ocho"
number_words[18] = "Eighteen"
number_words[50] = "Fifty"
number_words[132] = "OneThreeTwo"
number_words[28] = "TwentyEight"
number_words[79] = "SeventyNine"
del number_words[41]
del number_words[28]
if "Eight" in number_words:
    del number_words["Eight"]
number_words[50] = "FortyOne"
number_words[28] = "18"
del number_words[18]

for key in sorted(number_words):
     print("%s: %s" % (key, number_words[key]))

print(number_words)
