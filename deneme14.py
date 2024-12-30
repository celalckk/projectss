def re_verse (string):
 return string [::-1]

string = input ("enter the text you want to reverse :")

reverse_string = re_verse(string)
print(f"reverse of text :{reverse_string}")