from tkinter import *
root = Tk()
root.title("Test Run")

global number_entry
global message_entry

ceaser_shift_string = ""
alphabet= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s","t", "u", "v", "w", "x", "y", "z", " ", ".", "?", "!", ",","@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", ":", ";", "\'", "\"", "\\","[","]","{","}","|", "/", "<", ">","`", "~"]



number_entry = Entry(root)
number_entry.grid(row = 0)
number_entry.insert(0, "Insert Number Here")


message_entry = Entry(root)
message_entry.grid(row=1)
message_entry.insert(1, "Insert Message Here")







def caeser_Shift():
	

	list_of_index = []#list_of_new_index This is the index of each letter from message according to the aplhabet list
	list_of_coded_index = []# list_of_coded_index represents the list of new coded letters 
	list_of_coded_message=[] 


	shift_number = int(number_entry.get()) #number that shifts message
	message = message_entry.get()
	message = message.lower()
	list_of_message = return_individual_letter(message) #the list of each seperated letter 
	print("This is a list of every individual letter from message: ")		
	print(list_of_message) #- works

	#for loop converts all letters to the index of alphabet 
	for element in list_of_message:
		list_of_index.append(alphabet.index(element)) 

	print("\nThis is the index of each letter from message according to the aplhabet list: ")	
	print(list_of_index)#works




	#for loop converts all indexs to fit the new "coded" index 
	for element in list_of_index:
		#If the letter's index + shift fits into the aplhabet list then we make that new index
		number = int(element)
		if(number==58):
			list_of_coded_index.append(number)
		elif(number==57):
			list_of_coded_index.append(number)
		elif(number==56):
			list_of_coded_index.append(number)			
		elif(number==55):
			list_of_coded_index.append(number)
		elif(number==54):
			list_of_coded_index.append(number)
		elif(number==53):
			list_of_coded_index.append(number)
		elif(number==52):
			list_of_coded_index.append(number)
		elif(number==51):
			list_of_coded_index.append(number)
		elif(number==50):
			list_of_coded_index.append(number)
		elif(number==49):
			list_of_coded_index.append(number)
		elif(number==48):
			list_of_coded_index.append(number)
		elif (number==47):
			list_of_coded_index.append(number)
		elif(number==46):
			list_of_coded_index.append(number)
		elif(number==45):
			list_of_coded_index.append(number)
		elif(number==44):
			list_of_coded_index.append(number)
		elif(number==43):
			list_of_coded_index.append(number)
		elif(number==42):
			list_of_coded_index.append(number)
		elif(number==41):
			list_of_coded_index.append(number)
		elif(number==40):
			list_of_coded_index.append(number)
		elif(number==39):
			list_of_coded_index.append(number)
		elif(number==38):
			list_of_coded_index.append(number)
		elif(number==37):
			list_of_coded_index.append(number)
		elif(number==36):
			list_of_coded_index.append(number)
		elif(number==35):
			list_of_coded_index.append(number)
		elif(number==34):
			list_of_coded_index.append(number)
		elif(number==33):
			list_of_coded_index.append(number)
		elif(number==32):
			list_of_coded_index.append(number)
		elif (number==31):
			list_of_coded_index.append(number)
		elif(number==30):
			list_of_coded_index.append(number)
		elif(number==29):
			list_of_coded_index.append(number)
		elif(number==28):
			list_of_coded_index.append(number)
		elif (number ==27):
			list_of_coded_index.append(number)
		elif (number ==26):
			list_of_coded_index.append(number)
		elif (number + shift_number <= 25):
			list_of_coded_index.append(number + shift_number) 
			
		#If the letter's index + shift is longer than the alphabet we start from the begging and make that the new index
		else :#(number + shift_number> alphabet.length()):
			list_of_coded_index.append(number+shift_number-26) 
		
	print("\n This is the new coded index of message: ")		
	print(list_of_coded_index)
		#for loop to change the index to letter
	
	for element in list_of_coded_index:
		number = int(element)
		#print(alphabet[number])
		list_of_coded_message.append(alphabet[number])
	print("\nThis is the final coded message")
	print(''.join(list_of_coded_message))
	print("\n ")
	ceaser_shift_string = ''.join(list_of_coded_message)

	print(ceaser_shift_string)

	myLabel = Label(root, text = "Coded Message: \n" + ceaser_shift_string)
	myLabel.grid(row =3, column = 0)
	
	



def return_individual_letter(message): #Goes through each letter and returns a list of each individual letter 
	return [ch for ch in message]



enterButton = Button(root, text = "Enter", command = caeser_Shift)
enterButton.grid(row = 4, column = 0)





root.mainloop()