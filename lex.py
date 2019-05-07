#Lucas Carvalho Ribeiro - 201565554C

import sys
import sa 
import sb
import sc
import sd
import se
import sf
import sg
import si
import sl
import sm
import sn
import sp
import sr
import ss
import st
import sv
import sw
import sS2
separators = ['(', ')', '[', ']', '{', '}', ';', '.', ',', '=', '!', '&', '+', '-', '*', '/', '<']

def s0( character ):
    if(character=='a'):
        return 'a'
    if(character=='b'):
        return 'b'
    if(character=='c'):
        return 'c'
    if(character=='d'):
        return 'd'
    if(character=='e'):
        return 'e'
    if(character=='f'):
        return 'f'
    if(character=='g'):
        return 'g'
    if(character=='i'):
        return 'i'
    if(character=='l'):
        return 'l'
    if(character=='m'):
        return 'm'
    if(character=='n'):
        return 'n'
    if(character=='p'):
        return 'p'
    if(character=='r'):
        return 'r'
    if(character=='s'):
        return 's'
    if(character=='t'):
        return 't'
    if(character=='v'):
        return 'v'
    if(character=='w'):
        return 'w'
    if(character=='S'):
        return 'S'
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Num"
    for c in separators:
        if(character == c):
            return c
    return "bad" 

def sId(character):
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character=='_'):
        return "Id"
    if(character.isspace):
        return "Id"
    return "bad"    

def sNum(character):
    if(character.isnumeric()):
        return "Num"
    if(character.isspace):
        return "Num"
    return "bad"

def sBad(character):
    return 'bad'

def sAnd(character):
    if(character == '&'):
        return '&&'
    return 'bad'

def sNot(character):
    if(character == '='):
        return '!='
    return 'bad'

def sEqual(character):
    if(character == '='):
        return '=='
    return 'bad'

def sDone(state, character):
    if(character.isalpha()):
        return "Id"
    if(character.isnumeric()):
        return "Id"
    if(character.isspace()):
        return state    
    if(character=='_'):
        return "Id"
    return "bad"    

def d(state, character):
    states = {
        '0':s0(character),
        'a':sa.sa(character),
        'ab':sa.sab(character),
        'abs':sa.sabs(character),
        'abst':sa.sabst(character),
        'abstr':sa.sabstr(character),
        'abstra':sa.sabstra(character),
        'abstrac':sa.sabstrac(character),
        'abstract':sDone(state, character),
        'as':sa.sas(character),
        'ass':sa.sass(character),
        'asse':sa.sasse(character),
        'asser':sa.sasser(character),
        'assert':sDone(state, character),
        'b':sb.sb(character),
        'bo':sb.sbo(character),
        'boo':sb.sboo(character),
        'bool':sb.sbool(character),
        'boole':sb.sboole(character),
        'boolea':sb.sboolea(character),
        'boolean':sDone(state, character),
        'br':sb.sbr(character),
        'bre':sb.sbre(character),
        'brea':sb.sbrea(character),
        'break':sDone(state, character),
        'by':sb.sby(character),
        'byt':sb.sbyt(character),
        'byte':sDone(state, character),
        'c':sc.sc(character),
        'ca':sc.sca(character),
        'cas':sc.scas(character),
        'case':sDone(state, character),
        'cat':sc.scat(character),
        'catc':sc.scatc(character),
        'catch':sDone(state, character),
        'ch':sc.sch(character),
        'cha':sc.scha(character),
        'char':sDone(state, character),
        'cl':sc.scl(character),
        'cla':sc.scla(character),
        'clas':sc.sclas(character),
        'class':sDone(state, character),
        'co':sc.sco(character),
        'con':sc.scon(character),
        'cons':sc.scons(character),
        'const':sDone(state, character),
        'cont':sc.scont(character),
        'conti':sc.sconti(character),
        'contin':sc.scontin(character),
        'continu':sc.scontinu(character),
        'continue':sDone(state, character),
        'd':sd.sd(character),
        'de':sd.sde(character),
        'def':sd.sdef(character),
        'defa':sd.sdefa(character),
        'defau':sd.sdefau(character),
        'defaul':sd.sdefaul(character),
        'default':sDone(state, character),
        'd':sd.sd(character),
        'do':sd.sdo(character),
        'dou':sd.sdou(character),
        'doub':sd.sdoub(character),
        'doubl':sd.sdoubl(character),
        'double':sDone(state, character),
        'e':se.se(character),
        'el':se.sel(character),
        'els':se.sels(character),
        'else':sDone(state, character),
        'en':se.sen(character),
        'enu':se.senu(character),
        'enum':sDone(state, character),
        'ex':se.sex(character),
        'ext':se.sext(character),
        'exte':se.sexte(character),
        'exten':se.sexten(character),
        'extend':se.sextend(character),
        'extends':sDone(state, character),
        'f':sf.sf(character),
        'fi':sf.sfi(character),
        'fin':sf.sfin(character),
        'fina':sf.sfina(character),
        'final':sf.sfinal(character),
        'finall':sf.sfinall(character),
        'finally':sDone(state, character),
        'fl':sf.sfl(character),
        'flo':sf.sflo(character),
        'floa':sf.sfloa(character),
        'float':sDone(state, character),
        'fo':sf.sfo(character),
        'for':sDone(state, character),
        'g':sg.sg(character),
        'go':sg.sgo(character),
        'got':sg.sgot(character),
        'goto':sDone(state, character),
        'i':si.si(character),
        'if':sDone(state, character),
        'im':si.sim(character),
        'imp':si.simp(character),
        'impl':si.simpl(character),
        'imple':si.simple(character),
        'implem':si.simplem(character),
        'impleme':si.simpleme(character),
        'implemen':si.simplemen(character),
        'implement':si.simplement(character),
        'implements':sDone(state, character),
        'impo':si.simpo(character),
        'impor':si.simpor(character),
        'import':sDone(state, character),
        'in':si.sin(character),
        'ins':si.sins(character),
        'inst':si.sinst(character),
        'insta':si.sinsta(character),
        'instan':si.sinstan(character),
        'instanc':si.sinstanc(character),
        'instance':si.sinstance(character),
        'instanceo':si.sinstanceo(character),
        'instanceof':sDone(state, character),
        'int':si.sint(character),
        'inte':si.sinte(character),
        'inter':si.sinter(character),
        'interf':si.sinterf(character),
        'interfa':si.sinterfa(character),
        'interfac':si.sinterfac(character),
        'interface':sDone(state, character),
        'l':sl.sl(character),
        'le':sl.sle(character),
        'len':sl.slen(character),
        'leng':sl.sleng(character),
        'lengt':sl.slengt(character),
        'length':sDone(state, character),
        'lo':sl.slo(character),
        'lon':sl.slon(character),
        'long':sDone(state, character),
        'm':sm.sm(character),
        'ma':sm.sma(character),
        'mai':sm.smai(character),
        'main':sDone(state, character),
        'n':sn.sn(character),
        'na':sn.sna(character),
        'nat':sn.snat(character),
        'nati':sn.snati(character),
        'nativ':sn.snativ(character),
        'native':sDone(state, character),
        'ne':sn.sne(character),
        'new':sDone(state, character),
        'p':sp.sp(character),
        'pa':sp.spa(character),
        'pac':sp.spac(character),
        'pack':sp.spack(character),
        'packa':sp.spacka(character),
        'packag':sp.spackag(character),
        'package':sDone(state, character),
        'pr':sp.spr(character),
        'pri':sp.spri(character),
        'priv':sp.spriv(character),
        'priva':sp.spriva(character),
        'privat':sp.sprivat(character),
        'private':sDone(state, character),
        'pro':sp.spro(character),
        'prot':sp.sprot(character),
        'prote':sp.sprote(character),
        'protec':sp.sprotec(character),
        'protect':sp.sprotect(character),
        'protecte':sp.sprotecte(character),
        'protected':sDone(state, character),
        'pu':sp.spu(character),
        'pub':sp.spub(character),
        'publ':sp.spubl(character),
        'publi':sp.spubli(character),
        'public':sDone(state, character),
        'r':sr.sr(character),
        're':sr.sre(character),
        'ret':sr.sret(character),
        'retu':sr.sretu(character),
        'retur':sr.sretur(character),
        'return':sDone(state, character),
        's':ss.ss(character),
        'sh':ss.ssh(character),
        'sho':ss.ssho(character),
        'shor':ss.sshor(character),
        'short':sDone(state, character),
        'st':ss.sst(character),
        'sta':ss.ssta(character),
        'stat':ss.sstat(character),
        'stati':ss.sstati(character),
        'static':sDone(state, character),
        'str':ss.sstr(character),
        'stri':ss.sstri(character),
        'stric':ss.sstric(character),
        'strict':ss.sstrict(character),
        'strictf':ss.sstrictf(character),
        'strictfp':sDone(state, character),
        'su':ss.ssu(character),
        'sup':ss.ssup(character),
        'supe':ss.ssupe(character),
        'super':sDone(state, character),
        'sw':ss.ssw(character),
        'swi':ss.sswi(character),
        'swit':ss.sswit(character),
        'switc':ss.sswitc(character),
        'switch':sDone(state, character),
        'sy':ss.ssy(character),
        'syn':ss.ssyn(character),
        'sync':ss.ssync(character),
        'synch':ss.ssynch(character),
        'synchr':ss.ssynchr(character),
        'synchro':ss.ssynchro(character),
        'synchron':ss.ssynchron(character),
        'synchroni':ss.ssynchroni(character),
        'synchroniz':ss.ssynchroniz(character),
        'synchronize':ss.ssynchronize(character),
        'synchronized':sDone(state, character),
        't':st.st(character),
        'th':st.sth(character),
        'thi':st.sthi(character),
        'this':sDone(state, character),
        'thr':st.sthr(character),
        'thro':st.sthro(character),
        'throw':st.sthrow(character),
        'throws':sDone(state, character),
        'tr':st.str(character),
        'tra':st.stra(character),
        'tran':st.stran(character),
        'trans':st.strans(character),
        'transi':st.stransi(character),
        'transie':st.stransie(character),
        'transien':st.stransien(character),
        'transient':sDone(state, character),
        'try':sDone(state, character),
        'v':sv.sv(character),
        'vo':sv.svo(character),
        'voi':sv.svoi(character),
        'void':sDone(state, character),
        'vol':sv.svol(character),
        'vola':sv.svola(character),
        'volat':sv.svolat(character),
        'volati':sv.svolati(character),
        'volatil':sv.svolatil(character),
        'volatile':sDone(state, character),
        'w':sw.sw(character),
        'wh':sw.swh(character),
        'whi':sw.swhi(character),
        'whil':sw.swhil(character),
        'while':sDone(state, character),
        'S':sS2.sS(character),
        'St':sS2.sSt(character),
        'Str':sS2.sStr(character),
        'Stri':sS2.sStri(character),
        'Strin':sS2.sStrin(character),
        'String':sDone(state, character),
        'Sy':sS2.sSy(character),
        'Sys':sS2.sSys(character),
        'Syst':sS2.sSyst(character),
        'Syste':sS2.sSyste(character),
        'System':sId(character),
        '&':sAnd(character),
        '!':sNot(character),
        '=':sEqual(character),
        'Id':sId(character),
        'Num':sNum(character),
        'bad': sBad(character)
    }
    if (states.get(state) == None):
        return 'bad'
    return states[state]


filename = sys.argv[1]
file = open(filename, "r")
output = open("output.txt", "w")
state = '0'
lex = ""
set = enumerate(file, 1)
while state != "done":
    for index, line in set:
        i = 0
        while i < len(line):    
            for c in separators:
                if(i < len(line) and line[i]==c):
                    if(c=='.'):
                        if(state == "System"):
                            if(len(line) > i+11 and line[i:i+12]==".out.println" and (len(line) == i+12 or line[i+13].isspace or line[i+13] in separators)):
                                output.write("System.out.println\n")
                                state = '0'
                                lex = ''   
                                i = i+13
                                continue                        
                    
                    if(c=='/'):
                        if(len(line) >= i+1 and line[i+1] == '/'):
                            if(lex != ''):
                                state = d(state, ' ')
                                if(state=='Id'):
                                    output.write("ID:")
                                if(state=='Num'):
                                    output.write("NUM:")      
                                output.write(lex + "\n")
                            state = '0'
                            lex = ''    
                            (index, line) = next(set)
                            i = 0
                            continue
                        if(len(line) > i+1 and line[i+1] == '*'):
                            if(lex != ''):
                                state = d(state, ' ')
                                if(state=='Id'):
                                    output.write("ID:")
                                if(state=='Num'):
                                    output.write("NUM:")      
                                output.write(lex + "\n")
                            state = '0'
                            lex = ''
                            i = i+1
                            if(len(line) < i+2):
                                (index, line) = (next(set))
                                i = 0
                            while(line[i:i+2] != '*/'):
                                i = i + 1
                                if(len(line) < i+2):
                                    (index, line) = next(set)
                                    i = 0
                            i = i+2
                            continue


                    state = d(state, ' ')
                    if(lex != ''):
                        if(state=='Id'):
                            output.write("ID:")
                        if(state=='Num'):
                            output.write("NUM:")      
                        output.write(lex + "\n")
                    state = '0'
                    lex = ''
                    if(line[i]=='&'):
                        if(i+1 < len(line) and line[i+1]=='&'):
                            output.write('&&\n')
                            i = i+2
                        else:
                            output.write("Error in line " + str(index))   
                            sys.exit(0)     
                        continue
                    
                    elif(line[i]=='!' or line[i]=='='):
                        if(i+1 < len(line) and line[i+1]=='='):
                            output.write(line[i] + '=\n')
                            i = i+2
                        else:
                            output.write(line[i] + '\n')
                            i = i+1
                        continue    
                    else:
                        output.write(line[i] + '\n')
                        i = i+1       
                        continue

            if (i < len(line) and line[i].isspace()):
                if(lex == ''):
                    i = i+1
                    continue
                state = d(state, line[i])
                if(state=='bad'):
                    output.write("Error in line " + str(index))
                    sys.exit()
                if(state=='Id'):
                    output.write("ID:")
                if(state=='Num'):
                    output.write("NUM:")  
                output.write(lex + "\n")
                state = '0'
                lex = ''
                i = i+1
                continue
            elif (i < len(line) and line[i] not in separators):   
                state = d(state, line[i])
                if(state == 'bad'):
                    output.write("Error in line " + str(index))
                    sys.exit(0)
                lex = lex + line[i]
                i = i+1        
    if(lex!=''):
        if(state=='Id'):
            output.write("ID:")
        if(state=='Num'):
            output.write("NUM:")  
        if(state=='bad'):
            output.write("Error in line " + str(index))
        else:
            output.write(lex)    
    state = "done"        
        
