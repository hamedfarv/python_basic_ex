message = input(">")
words = message.split(' ')
emojis = {
":)":"😊" ,
":(":"😢"
}
#print(words)
output = ""
for word in words:
    #emojis.get(word , word)  ## if nothing find in dic 
    output += emojis.get(word , word) + " " 
print(output)    

