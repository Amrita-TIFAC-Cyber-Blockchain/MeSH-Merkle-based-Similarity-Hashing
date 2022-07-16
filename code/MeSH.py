# Authors       : Sathya Jothi SP & Ramaguru Radhakrishnan
# Date          : 12-JUL-2022
# Module Name   : MeSH - Merkle based Similarity Hashing
# Description   : The program accepts two files and splits into defined  chunk size. The files are then compared using a Merkle Tree with SHA256 as Hashing Algorithm.

from pymerkle import MerkleTree
import time 

'''
Function divides the program into smaller chunks 
'''
def chunk(content, start, end):
    filelist = []
    for i in range(len(content)//chunk_size):
        filelist.append(content[start:end])
        start = end
        end += chunk_size

    if temp2 != 0:
        filelist.append(content[temp1 * chunk_size : len(content)])
        
    return filelist

'''
Compares the merkle tree and returns the percentage of similarity
'''    
def compare(tree1, tree2):

    value = 0
    
    return value 

'''
Production Mode: Get the files from the User
'''
#filename1 = input("Enter file name 1 : ")
#filename2 = input("Enter file name 2 : ")
#chunk_size = input("Enter the chunk size of tree : ")

print("\n\n\t\t\t\t\t\t***** MeSH v0.5 **********")
print("\n\t\t\t\t\t\t***** Demo Mode **********")
time.sleep(2)

'''
Test Mode: Pre-determined files
'''
print("\n\nReading the input file 1......");
filename1 = "MeSH_TD1.txt"

print("\n\nReading the input file 2......");
filename2 = "MeSH_TD2.txt"

time.sleep(1)

'''
Configurable Chunk Size
'''
chunk_size = 7

print("\n\nChunk Size is fixed to ",chunk_size);

filename1_list = []
filename2_list = []

'''
Read the content from file
'''
with open(filename1, 'r') as file1, open(filename2, 'r') as file2:
    file1_content = file1.read()
    file2_content = file2.read()

'''
Dividing the file into chunks 
'''
temp1 = len(file1_content) // chunk_size
temp2 = len(file1_content) - temp1 * chunk_size

filename1_list = chunk(file1_content, 0, chunk_size)

print("\n\n[Developer Log] File 1 - Chunk List", filename1_list)

temp1 = len(file2_content) // chunk_size
temp2 = len(file2_content) - temp1 * chunk_size

filename2_list = chunk(file2_content, 0, chunk_size)

print("\n\n[Developer Log] File 2 - Chunk List", filename2_list)

'''
Construct Merkle Tree for file 1
'''
filetree1 = MerkleTree()

for content_f1 in filename1_list:
    filetree1.encrypt(content_f1)
    
print("\n\n[Log] Merkle Tree for File 1 \n", filetree1)

'''
Construct Merkle Tree for file 2
'''
filetree2 = MerkleTree()

for content_f2 in filename2_list:
    filetree2.encrypt(content_f2)
    
print("[Log] Merkle Tree for File 2 \n",filetree2)

'''
Calculate Similarity Hashing Score 
'''
print("\n\nComparing for Similarity......");

meshscore = compare(filetree1, filetree2)

print("\n\nMeSH Score ", meshscore);
