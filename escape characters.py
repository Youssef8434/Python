txt = "We are the so-called \"Vikings\" from the north."  
print(txt) 

txt = 'It\'s alright.'      #\'	 =   Single Quote
print(txt) 

txt = "This will insert one \\ (backslash)."
print(txt) 

txt = "Hello\nWorld!"       #\n   =  new line
print(txt) 

txt = "Hello\rWorld!"       #\r   =  carriage return 
print(txt) 

txt = "Hello\tWorld!"       #\t   =  tab
print(txt) 

#This example erases one character (backspace):
txt = "Hello \bWorld!"      #\b   =  backspace
print(txt) 

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"    #\ooo   =  octal value
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"    #\xhh   =  hex value
print(txt) 
