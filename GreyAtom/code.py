# --------------
#Code starts here

#Function to read file
def read_file(path):
    file=open(path,'r')
    sentence=file.readline()

    file.close()
    return sentence
    print(sentence)
    #Opening of the file located in the path in 'read' mode
    
sample_message=read_file(file_path)
    #Reading of the first line of the file and storing it in a variable
    
    #Closing of the file    
    #Returning the first line of the file
message_1=read_file(file_path_1)
message_2=read_file(file_path_2)

print(message_1,message_2)
print(sample_message)    

#Calling the function to read file

#Printing the line of the file


#Function to fuse message
def fuse_msg(message_a,message_b):
    message_a=int(message_a)
    message_b=int(message_b)
    quotient=message_b//message_a
    str(quotient)
    return quotient    
    #Integer division of two numbers    
        #Returning the quotient in string format

secret_msg_1=fuse_msg(message_1,message_2)
#Calling the function to read file  

#Calling the function to read file


#Calling the function 'fuse_msg'


#Printing the secret message 
message_3=read_file(file_path_3)
print(message_3)

#Function to substitute the message
def substitute_msg(message_c):
    sub=''
    if (message_c=='Red'):
        sub='Army General'
    elif(message_c=='Green'):
        sub='Data Scientist'
    elif(message_c=='Blue'):
        sub='Marine Biologist'
    return sub
    #If-else to compare the contents of the file
    #Returning the substitute of the message
secret_msg_2=substitute_msg(message_3)

#Calling the function to read file
message_4=read_file(file_path_4)
message_5=read_file(file_path_5)

#Calling the function 'substitute_msg'
print(message_4,message_5)

#Printing the secret message

#Function to compare message
def compare_msg(message_d,message_e):
    a_list=message_d.split()
    b_list=message_e.split()
    c_list=a_list+b_list
    final_msg=" ".join(c_list)
    return final_msg
    #Splitting the message into a list
        
    #Splitting the message into a list
secret_msg_3=compare_msg(message_4,message_5)
    
    #Comparing the elements from both the lists
    
    
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    
    

#Calling the function to read file
message_6=read_file(file_path_6)
print(message_6)
#Calling the function to read file


#Calling the function 'compare messages'


#Printing the secret message


#Function to filter message
def extract_msg(message_f):
    a_list=message_f.split()
    even_word= lambda x:len(x)%2==0
    #Splitting the message into a list
    b_list=filter(even_word,a_list)
    final_msg=" ".join(b_list)
    return final_msg
    
    #Creating the lambda function to identify even length words    
    #Splitting the message into a list    
    #Combining the words of a list back to a single string sentence
    #Returning the sentence
secret_msg_4=extract_msg(message_6)

message_parts=['you','are','now','1','step','closer','to','become','Data','Scientist']

secret_msg=" ".join(message_parts)

def write_file(secret_msg,path):
    file=open(path,'a+')
    file.write(secret_msg)
    file.close()
final_path= user_data_dir + '/secret_message.txt'
write_file(secret_msg,final_path)

print(secret_msg)


