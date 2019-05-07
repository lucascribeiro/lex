#Lucas Carvalho Ribeiro - 201565554C

def sg(character):
    if(character=='o'):
        return "go" 
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad" 

def sgo(character):
    if(character=='t'):
        return "got" 
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad" 

def sgot(character):
    if(character=='o'):
        return "goto" 
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad"     
