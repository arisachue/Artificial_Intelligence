# -*- coding: utf-8 -*-

from math import log
import random
import sys

alpha_index = {"A": 0,
               "B": 1,
               "C": 2,
               "D": 3,
               "E": 4,
               "F": 5,
               "G": 6,
               "H": 7,
               "I": 8,
               "J": 9,
               "K": 10,
               "L": 11,
               "M": 12,
               "N": 13,
               "O": 14,
               "P": 15,
               "Q": 16,
               "R": 17,
               "S": 18,
               "T": 19,
               "U": 20,
               "V": 21,
               "W": 22,
               "X": 23,
               "Y": 24,
               "Z": 25}
ngram_freq = dict()

POPULATION_SIZE = 500
NUM_CLONES = 1
TOURNAMENT_SIZE = 20
TOURNAMENT_WIN_PROBABILITY = .75
CROSSOVER_LOCATIONS = 5
MUTATION_RATE = .8

def get_key(dic, val):
    for k, v in dic.items():
        if val == v:
            return k

def encode(source, cipher_alpha):
    source = source.upper()
    encoded = ""
    for s in source:
        if s.isalpha():
            i = alpha_index[s]
            encoded += cipher_alpha[i]
        else:
            encoded += s
    return encoded

def decode(cipher, cipher_alpha):
    decoded = ""
    for s in cipher:
        if s.isalpha():
            i = cipher_alpha.index(s)
            decoded += get_key(alpha_index, i)
        else:
            decoded += s
    return decoded

def store_ngram_freq(s):
    global ngram_freq
    with open(s) as f:
        for line in f:
            line = line.strip()
            l = line.split()
            ngram_freq[l[0]] = int(l[1])
    return ngram_freq

def fitness_ngram(n, encoded, cipher_alpha):
    decoded = decode(encoded, cipher_alpha)
    score = 0
    for i in range(0, len(decoded)-n+1):
        gram = decoded[i:i+n]
        if gram.isalpha() and gram in ngram_freq:
            freq = ngram_freq[gram]
            score += log(freq, 2)
    return score

def swap(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp
    return l

def hill_climbing(encoded):
    random_cipher = random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 26)
    score = fitness_ngram(4, encoded, random_cipher)
    print(decode(encoded, random_cipher))
    while True:
        r1 = random.randrange(0, 26)
        r2 = random.randrange(0, 26)
        l_cipher = list(random_cipher)
        l_cipher = swap(l_cipher, r1, r2)
        temp_cipher = "".join(l_cipher)
        new_score = fitness_ngram(4, encoded, temp_cipher)
        if new_score > score:
            score = new_score
            random_cipher = temp_cipher
            print(decode(encoded, random_cipher))
            
def population():
    pop = []
    while len(pop) < POPULATION_SIZE:
        pop.append("".join(random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 26)))
    return pop

def choose_parent(tournament):
    while True:
        if random.random() < TOURNAMENT_WIN_PROBABILITY or len(tournament) == 1:
            return tournament[0]
        else:
            tournament = tournament[1:]

def breed(p1, p2):
    if random.random() < 0.5:
        temp = p1
        p1 = p2
        p2 = temp
    child = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    crossover_index = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], CROSSOVER_LOCATIONS)
    for i in crossover_index:
        child[i] = p1[i]
    for s in p2:
        if s not in child:
            child[child.index("-")] = s
    return child

def mutate(child):
    if random.random() < MUTATION_RATE:
        r1 = random.randrange(0, 26)
        r2 = random.randrange(0, 26)
        child = swap(child, r1, r2)
    return child

def selection(encoded, current_gen):
    next_gen = []
    next_gen_storage = set()
    gen_score = dict()
    for s in current_gen:
        sc = fitness_ngram(4, encoded, s)
        gen_score[s] = sc
    ranked_scores = sorted(gen_score, key=gen_score.get, reverse=True)
    for i in range(NUM_CLONES):
        next_gen.append(ranked_scores[i])
        next_gen_storage.add(ranked_scores[i])
    while len(next_gen) < POPULATION_SIZE:
        tour = random.sample(current_gen, 2*TOURNAMENT_SIZE)
        tour1 = tour[:TOURNAMENT_SIZE]
        tour2 = tour[TOURNAMENT_SIZE:]
        ranked_tour1 = sorted(tour1, key=lambda c: gen_score[c], reverse=True)
        ranked_tour2 = sorted(tour2, key=lambda c: gen_score[c], reverse=True)
        parent1 = choose_parent(ranked_tour1)
        parent2 = choose_parent(ranked_tour2)
        child = breed(parent1, parent2)
        child = mutate(child)
        child = "".join(child)
        if child not in next_gen_storage:
            next_gen.append(child)
            next_gen_storage.add(child)
    return next_gen, ranked_scores

def genetic_algorithm(encoded):
    pop = population()
    for i in range(500):
        pop, rs = selection(encoded, pop)
        print(decode(encoded, rs[0]))
    gen_score = dict()
    for s in pop:
        sc = fitness_ngram(4, encoded, s)
        gen_score[s] = sc
    ranked_scores = sorted(gen_score, key=gen_score.get, reverse=True)
    return decode(encoded, ranked_scores[0])
        
    
    
store_ngram_freq("ngrams.txt")
# tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# tour_dic = {0: 1,
#             1: 2,
#             2: 3,
#             3: 4,
#             4: 5,
#             5: 6,
#             6: 7,
#             7: 8,
#             8: 9,
#             9: 10}
# tour1 = tour[:5]
# tour2 = tour[5:]
# ranked_tour1 = sorted(tour1, key=lambda c: tour_dic[c], reverse=True)
# ranked_tour2 = sorted(tour2, key=lambda c: tour_dic[c], reverse=True)
# print(ranked_tour1, ranked_tour2)
  
# print(fitness_ngram(3, "XMTP CGPQR BWEKNJB GQ OTGRB EL BEQX BWEKNJB, G RFGLI. GR GQ BEQX ABSETQB RFGQ QBLRBLSB TQBQ EJJ RBL KMQR SMKKML VMPYQ GL BLDJGQF: 'G FEUB RM AB E DMMY QRTYBLR GL RFER SJEQQ GL RFB PMMK MC RFER RBESFBP.'"))
# print(fitness_ngram(4, "XMTP CGPQR BWEKNJB GQ OTGRB EL BEQX BWEKNJB, G RFGLI. GR GQ BEQX ABSETQB RFGQ QBLRBLSB TQBQ EJJ RBL KMQR SMKKML VMPYQ GL BLDJGQF: 'G FEUB RM AB E DMMY QRTYBLR GL RFER SJEQQ GL RFB PMMK MC RFER RBESFBP.'"))
# string = """PF HACYHTTRQ VF N PBYYRPGVBA BS SERR YRNEAVAT NPGVIVGVRF GUNG 
#             GRNPU PBZCHGRE FPVRAPR GUEBHTU RATNTVAT TNZRF NAQ CHMMYRF GUNG
#             HFR PNEQF, FGEVAT, PENLBAF NAQ YBGF BS EHAAVAT NEBHAQ. JR
#             BEVTVANYYL QRIRYBCRQ GUVF FB GUNG LBHAT FGHQRAGF PBHYQ QVIR URNQ-
#             SVEFG VAGB PBZCHGRE FPVRAPR, RKCREVRAPVAT GUR XVAQF BS DHRFGVBAF
#             NAQ PUNYYRATRF GUNG PBZCHGRE FPVRAGVFGF RKCREVRAPR, OHG JVGUBHG
#             UNIVAT GB YRNEA CEBTENZZVAT SVEFG. GUR PBYYRPGVBA JNF BEVTVANYYL
#             VAGRAQRQ NF N ERFBHEPR SBE BHGERNPU NAQ RKGRAFVBA, OHG JVGU GUR
#             NQBCGVBA BS PBZCHGVAT NAQ PBZCHGNGVBANY GUVAXVAT VAGB ZNAL
#             PYNFFEBBZF NEBHAQ GUR JBEYQ, VG VF ABJ JVQRYL HFRQ SBE GRNPUVAT.
#             GUR ZNGREVNY UNF ORRA HFRQ VA ZNAL PBAGRKGF BHGFVQR GUR PYNFFEBBZ
#             NF JRYY, VAPYHQVAT FPVRAPR FUBJF, GNYXF SBE FRAVBE PVGVMRAF, NAQ
#             FCRPVNY RIRAGF. GUNAXF GB TRAREBHF FCBAFBEFUVCF JR UNIR ORRA
#             NOYR GB PERNGR NFFBPVNGRQ ERFBHEPRF FHPU NF GUR IVQRBF, JUVPU NER
#             VAGRAQRQ GB URYC GRNPUREF FRR UBJ GUR NPGVIVGVRF JBEX (CYRNFR
#             QBA’G FUBJ GURZ GB LBHE PYNFFRF – YRG GURZ RKCREVRAPR GUR
#             NPGVIVGVRF GURZFRYIRF!). NYY BS GUR NPGVIVGVRF GUNG JR CEBIVQR
#             NER BCRA FBHEPR – GURL NER ERYRNFRQ HAQRE N PERNGVIR PBZZBAF
#             NGGEVOHGVBA-FUNERNYVXR YVPRAPR, FB LBH PNA PBCL, FUNER NAQ ZBQVSL
#             GUR ZNGREVNY. SBE NA RKCYNANGVBA BA GUR PBAARPGVBAF ORGJRRA PF
#             HACYHTTRQ NAQ PBZCHGNGVBANY GUVAXVAT FXVYYF, FRR BHE
#             PBZCHGNGVBANY GUVAXVAT NAQ PF HACYHTTRQ CNTR. GB IVRJ GUR GRNZ
#             BS PBAGEVOHGBEF JUB JBEX BA GUVF CEBWRPG, FRR BHE CRBCYR CNTR.
#             SBE QRGNVYF BA UBJ GB PBAGNPG HF, FRR BHE PBAGNPG HF CNTR. SBE
#             ZBER VASBEZNGVBA NOBHG GUR CEVAPVCYRF ORUVAQ PF HACYHTTRQ, FRR
#             BHE CEVAPVCYRF CNTR."""
# string = "XMTP CGPQR BWEKNJB GQ OTGRB EL BEQX BWEKNJB, G RFGLI. GR GQ BEQX ABSETQB RFGQ QBLRBLSB TQBQ EJJ RBL KMQR SMKKML VMPYQ GL BLDJGQF: 'G FEUB RM AB E DMMY QRTYBLR GL RFER SJEQQ GL RFB PMMK MC RFER RBESFBP.'"
# hill_climbing(string)
# string = """W CTZV VYQXDVD MCWJ IVJJTHV, TYD VYQXDVD WM BVAA, FXK WM QXYMTWYJ MCV JVQKVM XF MCV PYWZVKJV! YX
# KVTAAS, WM DXVJ! SXP DXY'M NVAWVZV IV? BCS BXPAD SXP YXM NVAWVZV MCTM MCWJ RVKFVQMAS QKXIPAVYM JVQKVM
# MVGM QXYMTWYJ MCV NV TAA, VYD TAA, HKTYDVJM JVQKVM XF TAA MCV QXJIXJ? YXB W FVVA DWJKVJRVQMVD! CTZV
# SXP DWJQXZVKVD SXPK XBY NVMMVK PAMWITMV MKPMC XF VZVKSMCWYH? W DWDY'M MCWYL JX. JX BCS TKV SXP HVMMWYH
# TAA PRRWMS TM IV? CXYVJMAS. YX XYV CTJ TYS ITYYVKJ MCVJV DTSJ. ...BCTM'J MCTM? SXP BTYM IV MX MVAA
# SXP MCV JVQKVM? YXM TFMVK MCWJ LWYD XF DWJKVJRVQM! HXXDYVJJ HKTQWXPJ IV. NTQL BCVY W BTJ T SXPMC W
# BTJ YXM JX QTAAXPJ. BCVY JXIVXYV BVAA KVJRVQMVD TYD WIRXKMTYM MXAD IV MCTM MCVS CTD JXIVMCWYH BXKMC
# MVAAWYH IV, W OPJM AWJMVYVD! W DWDY'M DXPNM MCVI! JX KPDV, CXYVJMAS. OPJM PYTQQVRMTNAV."""
string = sys.argv[1]  
print(genetic_algorithm(string))