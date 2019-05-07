#Lucas Carvalho Ribeiro - 201565554C

def sw(character):
    if(character=='h'):
        return "wh"   
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad" 

def swh(character):
    if(character=='i'):
        return "whi"   
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad" 

def swhi(character):
    if(character=='l'):
        return "whil"   
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad" 

def swhil(character):
    if(character=='e'):
        return "while"   
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad" 
