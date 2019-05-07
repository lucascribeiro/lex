#Lucas Carvalho Ribeiro - 201565554C

def sr(character):
    if(character=='e'):
        return "re"   
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad"  

def sre(character):
    if(character=='t'):
        return "ret"   
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad"  

def sret(character):
    if(character=='u'):
        return "retu"   
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad"  

def sretu(character):
    if(character=='r'):
        return "retur"   
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad"  

def sretur(character):
    if(character=='n'):
        return "return"   
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return "Id"    
    if(character=='_'):
        return "Id"
    return "bad"      
