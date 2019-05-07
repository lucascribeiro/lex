#Lucas Carvalho Ribeiro - 201565554C

def sf(character):
    if(character=='i'):
        return "fi"
    if(character=='l'):
        return "fl"
    if(character=='o'):
        return "fo"  
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad"   

def sfi(character):
    if(character=='n'):
        return "fin" 
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad"   

def sfin(character):
    if(character=='a'):
        return "fina" 
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad"   

def sfina(character):
    if(character=='l'):
        return "final" 
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad"   

def sfinal(character):
    if(character=='l'):
        return "finall" 
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "final"    
    if(character=='_'):
        return "Id"
    return "bad"   

def sfinall(character):
    if(character=='y'):
        return "finally" 
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad"   

def sfl(character):
    if(character=='o'):
        return "flo" 
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad"   

def sflo(character):
    if(character=='a'):
        return "floa" 
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad"   

def sfloa(character):
    if(character=='t'):
        return "float" 
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad"   

def sfo(character):
    if(character=='r'):
        return "for" 
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad" 
