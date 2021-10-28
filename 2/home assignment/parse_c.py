import re
import sys

f = open("./sample.txt","r")
func_tab= []
comm_tab = []

for func in re.findall(r'(?<=(?<=int\s)|(?<=void\s)|(?<=string\s)|(?<=double\s)|(?<=float\s)|(?<=char\s)).*?(?=\s?\()', f.read()):

    func_tab.append(func)

f = open("./sample.txt","r")
pattern = re.compile('(?:/\*(.*?)\*/)|(?://(.*?)\n)',re.S)
comments = pattern.findall(f.read())

if __name__ == "__main__":

    if sys.argv[1] == "--wrap":

        prnt_str = "// "

        for line in comments:
            
            for newline in line:
                
                newline = newline.strip().replace("\n"," ")
                prnt_str += newline + " "
                
        print(prnt_str)

        print("\nWykryto definicje funkcji:",end="")
        
        for found_function in func_tab:
            print(f" {found_function}()",end=" ")


    if sys.argv[1] == "--dontwrap":

        for line in comments:

            line = list(line)[0].split('\n') #z is a tuple ("THIS WE WANT",""), hence why its converted to list, split with newlines and used only its first element
            line = [x for x in line if x != ""] #omit empty lines
            
            for printed_line in line:

                print(f"// {printed_line}",end="\n")

        print("\nWykryto definicje funkcji:",end="")
    
        for found_function in func_tab:

            print(f" {found_function}()",end=" ")
        print("\n")


