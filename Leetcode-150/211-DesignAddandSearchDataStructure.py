"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.class WordDictionary:


class WordDictionary:

    def __init__(self):
        self.word_set = set()
        self.word_list = []
        self.word_dict = {}
        

    def addWord(self, word: str) -> None:
        if word in self.word_set:
            pass
        else:
            le = len(word)
            self.word_set.add(word)
            if le in self.word_dict:
                self.word_dict[le].append(word)
            else:
                self.word_dict[le] = [word]
        

    def search(self, word: str) -> bool:
        if not "." in word:
            if word in self.word_set:
                return True
            else:
                return False
            
        else:
            positions = []
            le = len(word)
            if le not in word_dict:
                return False
            leList = self.word_dict[le]
            for i in range(le):
                letter =  word[i]
                if letter == ".":
                    positions.append(i)

            if len(positions)==1:
                pos = positions[0]
                targetString = word[:pos]+word[pos+1:]
                for potentialWord in leList:
                    potentialString = potentialWord[:pos]+potentialWord[pos+1:]
                    if targetString == potentialString:
                        return True
                    
            if len(positions)==2:
                pos1 = positions[0]
                pos2 = positions[1]

                targetString = word[:pos1]+word[pos1+1:pos2]+word[pos2+1:]
                for potentialWord in leList:
                    potentialString = potentialWord[:pos1]+potentialWord[pos1+1:pos2]+potentialWord[pos2+1:] 
                    if targetString == potentialString:
                        return True

            return False    



        
        """



'''
class WordDictionary:

    def __init__(self):
        self.word_list = set()
        

    def addWord(self, word: str) -> None:
        self.word_list.append(word)
        for i in range(len(word)):
            self.word_list.append()
        

    def search(self, word: str) -> bool:

'''