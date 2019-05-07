#Lucas Carvalho Ribeiro - 201565554C

def sm(character):
    if(character=='a'):
        return "ma"   
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad"   

def sma(character):
    if(character=='i'):
        return "mai"   
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad"   

def smai(character):
    if(character=='n'):
        return "main"   
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad"   
