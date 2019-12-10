from pythainlp import word_tokenize, Tokenizer
text = "กฎหมายแรงงานฉบับปรับปรุงใหม่ประกาศใช้แล้ว"

'''
Options for engine
newmm (default) - dictionary-based, Maximum Matching + Thai Character Cluster
longest - dictionary-based, Longest Matching
deepcut - wrapper for deepcut, language-model-based
icu - wrapper for ICU (International Components for Unicode, using PyICU), dictionary-based
ulmfit - for thai2fit

see more: https://thainlp.org/pythainlp/docs/2.0/api/tokenize.html
'''

print("newmm:", word_tokenize(text))  # default engine is "newmm"
print("longest:", word_tokenize(text, engine="longest"))

words = ["กฎ", "งาน"]
custom_tokenizer = Tokenizer(words)
print("custom:", custom_tokenizer.word_tokenize(text))


