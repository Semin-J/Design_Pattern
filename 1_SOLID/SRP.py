# SRP (Single Responsibility Principle) / SOC (Separation of Concern)

class Journal:
    # don't create data member outside of __init__
    # it can be shared by another object
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1
    
    def remove_enry(self, pos):
        del self.entries[pos]
        #delete object - list, variable etc.

    def __str__(self) :
        return '\n'.join(self.entries)

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

if __name__ == '__main__':
    j = Journal()
    j.add_entry('I am happy')
    j.add_entry('I am cheerful')
    print(f'Journal entries:\n{j}')
    
    # r means raw string
    file_name = r'./journal.txt'
    PersistenceManager.save_to_file(j, file_name)
    with open(file_name) as f:
        print(f.read())
