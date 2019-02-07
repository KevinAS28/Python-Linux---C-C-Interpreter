#C++ Interpreter v 0.1
#by kevin agusto
import subprocess
import sys
import os
import re
spab = lambda x: [print(" ") for i in range(x)]
class Interpreter:
    mode = 0
    yes = 1;
    def __init__(self):
        self.__start_message = "C++ Interpreter v 0.1\nby Kevin Agusto 15/Dec/2017\n"
        self.__exsymb = r">>> "
        print(self.__start_message)
        
        print(self.mode)
    command = b""
    def about(self):
        print(self.__start_message)
    def add_command(self, *command):
        for i in command:
            self.command += b"\n"
            self.command += i.encode("utf-8")
    def clear(self):
        self.command = b""
        if self.mode:
         self.add_command("#include <iostream>", "using namespace std;", "int main(int argc, char** argv)", "{\n")
         self.yes = 1;
        try:
         os.system("clear")
        except:
         pass
        print("Command cleared\n")
    def exit(self):
        print("\nExitting....\n")
        sys.exit(0)
        exit()
    def run(self):
        file_name = "temp.cpp"
        try:
         os.remove(file_name)
        except:
          pass
        open(file_name, "w+")
        if self.mode:

         self.add_command("}")
        with open(file_name, "wb") as okay:
            okay.write(self.command)
        try:
         output = subprocess.check_output("run -f %s -rm false"  %(file_name), shell=True).decode("utf-8")
        except:
         output = subprocess.check_output("run -f %s -rm false" %(file_name), shell=True)
        print("%s" %(output))
        os.system
        if self.yes:
         self.command = bytes(list(self.command)[0:-1])
         #self.yes = 0;
        #os.remove(file_name)
    def show_command(self):
        print(self.special_command)
    def show_script(self):
        print(self.command.decode("utf-8"))
    def undo(self):
        pattern = b"((.+)(\n))+"
        akhir = re.search(pattern, self.command).span()[1]
        self.command = bytes(list(self.command[:akhir]))
    def include(self):#just in fast mode
        self.command = b"\n" + b"#include " + input("To include: ").encode("utf-8") + self.command + b"\n"
    def get_input(self):
        #write some basic command
        self.add_command("#include <iostream>", "using namespace std;")
        if self.mode:
         self.add_command("int main(int argc, char** argv)", "{\n")
        try:
            while True:
                temp_command = str(input(self.__exsymb))
                #handling special command

                special_command = ["run", "clear", "about", "show_command", "exit", "show_script", "undo", "include"]
                self.special_command = special_command
                if temp_command in special_command:
                    exec("self.%s()" %(temp_command))
                    continue
                self.add_command(temp_command)
        except KeyboardInterrupt:
            self.exit()

 
cppInt = Interpreter
if len(sys.argv)>1:
 cppInt.mode = 1
cppInt().get_input()
