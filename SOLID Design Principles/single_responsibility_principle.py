# Single Responsibility Principle (SRP) / Seperation of Concern (SOC)

from regex import P


class Journal:
    def __init__(self):
        self.entires = []
        self.count = 0
    
    def add_entry(self,text):
        self.count+=1
        self.entires.append(f'{self.count}: {text}')

    def remove_entry(self,pos):
        del self.entires[pos]
    
    def __str__(self) -> str:
        return '\n'.join(self.entires)

    # Breaks Single Responsibility Principle
    def save(self,filename):
        with open(filename,'w')as f:
            f.write(str(self))

# Seperation of Concern
class PersistenceManager:
    @staticmethod
    def save_to_file(journal,filename):
        with open(filename,'w')as f:
            f.write(str(journal))

j = Journal()
j.add_entry("I am happy today")
j.add_entry("I am sad today")
print(j)
PersistenceManager.save_to_file(j,"journal.txt")
    