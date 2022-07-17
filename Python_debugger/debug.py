
import pdb

pdb.set_trace()
def vow_replace1(string, rep):
    for alpha in ["a","e","i","o","u"]: 
        string= string.replace(alpha,rep)
    return string

print(vow_replace1("apples and bananas", "u")  )