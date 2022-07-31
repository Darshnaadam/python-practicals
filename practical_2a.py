def vowel(s):
    l=['a','e','i','o','u','A','E','I','O','u']
    for i in s:
        if i in l:
            print("True")
        else:
            print("False")
s = 'God is great'
vowel(s)
