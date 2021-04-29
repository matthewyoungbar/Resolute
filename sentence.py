'''
~ represents 'not'
-> represents 'implies'
v represents 'or'
^ represents 'and'
<-> represents 'iff'
'''


class sentence:
    def __init__(self):
        self.statements = []
        
    def printStatements(self):
        for i in self.statements:
            print()
            for j in i:
                print(j.getString())
        
    def addStatement(self,s):
        terms = []
        counter = 0
        para = True
        
        if "(" not in s:
            terms.append(term(s))
            para = False
        
        while (counter < len(s)) and para == True:
            current = s[counter]
            if current == "(":
                temp = ""
                while s[counter] != ")" and counter < len(s):
                    temp += s[counter]
                    counter += 1
                terms.append(term(temp+")"))
                counter += 1
            else:
                terms.append(term(current))
                counter += 1
                
        counter = 0
        while counter < len(terms):
            if terms[counter].getString() == "~":
                terms.pop(counter)
                terms[counter].negate()
            counter += 1
            
        self.statements.append(terms)

    def solve(self):
        return None
        
        
     
class term:
    def __init__(self,s):
        self.string = s
        if "<" in self.string:
            self.convertIff()
        elif "-" in self.string:
            self.convertImplies()
        
    def getString(self):
        return self.string
    
    def convertIff(self):
        if "<" not in self.string:
            return None
        
        if self.string[0] == "(":
            self.string = self.string[1::]
        if self.string[len(self.string) - 1] == ")":
            self.string = self.string[0:len(self.string)-1]
        
        counter = 0
        while counter < len(self.string):
           if self.string[counter] == "<":
               break
           counter += 1
           
        newString = "( ~" + self.string[0:counter] + "^ ~" + self.string[counter+3::] + ") v (" + self.string[0:counter] + "^" + self.string[counter+3::] + ")"
        
        self.string = newString
        return newString
    
    def convertImplies(self):
        return None
    
    def negate(self):        
        count = 0
        alreadyNegated = False
        if self.string[0] == "~":
            self.string = self.string[1::]
            return self.string
        while count < len(self.string):
            # these characters don't really matter
            if self.string[count] == "~":
                #print()
                #print(self.string)
                self.string = self.string[0:count] + self.string[count+1:]
                alreadyNegated = True
                #print(self.string)
            elif self.string[count] == "(" or self.string[count] == ")" or self.string[count] == " ":
                count += 1
                continue
            else:
                if self.string[count] == "^":
                    self.string = self.string[0:count] + "v" + self.string[count+1::]
                    count +=1
                    
                elif self.string[count] == "v":
                    self.string = self.string[0:count] + "^" + self.string[count+1::]
                    count += 1
                    
                else:
                    if alreadyNegated:
                        alreadyNegated = False
                        count += 1
                        continue
                    self.string = self.string[0:count] + "~" + self.string[count::]
                    count += 2
        
        return self.string
    
    
    
    
t = term("(Q <-> R)")
#print(t.negate())
temp = sentence()
temp.addStatement("P ^ Q")  
temp.addStatement("~(Q <-> R)")  
temp.addStatement("~(P v R)")  
temp.printStatements()






















