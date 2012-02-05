
test_nodes = [1,2,3,4,5,6]

test_links = { 1 : [2,3],
              2 : [1,3,5],
              3 : [1,2],
              5 : [2]
              } 


def is_complete(graph):
    pass

def makes_complete(graph, new_node, links):
    for node in graph:
        if node not in links or new_node not in links[node]:
            return False
    return True    

def find_complete_subgraphs(nodes, links, seed = None):
    complete_subgraphs = {}
    if seed == None:
        complete_subgraphs[1] = [set([node]) for node in nodes]
    else:
        complete_subgraphs[1] = [set([node]) for node in seed]
    k=2
    while True:
        complete_subgraphs[k] = []
        for graph in complete_subgraphs[k-1]:   
            for node in nodes: # make this right
                if node not in graph:
                    if makes_complete(graph, node, links) and graph.union(set([node])) not in complete_subgraphs[k]:
                        complete_subgraphs[k].append(graph.union(set([node])))
        if len(complete_subgraphs[k]) == 0:
            break
        k += 1
    return complete_subgraphs

def check_well_defined(nodes, links):
    for node in nodes:
        if not node in links:
            print "%s is isolated" % str(node)
    for node, linked_nodes in links.iteritems():
        if node not in nodes:
            print "Unrecognised node: %s" % node
        for linked_node in linked_nodes:
            if linked_node not in nodes:
                print "Unrecognised relative: %s" % linked_node
            if node not in links[linked_node]:
                print "asymmetric relation: %s and %s" %(node, linked_node)

def calc_similarity(node1, node2, links):
    same = len(set(links[node1]).intersection(set(links[node2])))
    diff = len(set(links[node1])) + len(set(links[node2]))
    return 1.0 * same / diff

def most_similar(nodes, links):
    best_similarity = 0
    best_nodes = None
    for ii in range(len(nodes)):
        for jj in range(ii):
            new_similarity = calc_similarity(nodes[ii], nodes[jj], links)
            if new_similarity > 0.3:
                print new_similarity
                print (nodes[ii], nodes[jj])
                
            if new_similarity > best_similarity:
                best_similarity = new_similarity
                best_nodes = (nodes[ii], nodes[jj])
    print best_similarity
    return best_nodes

flavours = ["alm",
            "anc",
            "ani",
            "app",
            "apr",
            "asp",
            "aub",
            "avo",
            "bac",
            "ban",
            "bas",
            "bef",
            "bet",
            "bel",
            "bbe",#blackberry
            "bcu",#blackcurrant
            "bpu",#black pudding
            "blb",#blueberry
            "blc",#blue cheese
            "bro",
            "but",
            "cab",
            "cap",
            "car",
            "crt",
            "cau",
            "cav",
            "cel",
            "chr",
            "chs",
            "chi",
            "chk",
            "cho",
            "cin",
            "clo",
            "coc",
            "cof",
            "cle",
            "cse",
            "cuc",
            "cum",
            "dil",
            "egg",
            "fig",
            "gar",
            "gin",
            "glo",
            "goa",
            "gra",
            "gfr",
            "har",
            "haz",
            "hor",
            "jun"]

pairings = {"alm" : ["ani", "app", "apr", "asp", "ban", "bbe", "bcu", "blb",
                     "but", "car", "cau", "chr", "chk", "chi", "cho", "cin",
                     "coc", "cof", "fig", "gar", "gin", "gra", "har", "haz"],
            "anc" : ["bef", "bet", "bro", "cap", "cau", "chi", "coc", "egg",
                     "gar", "har"],
            "ani" : ["alm", "app", "asp", "bac", "ban", "bas", "bef", "bcu",
                     "crt", "chk", "chi", "cho", "cin", "coc", "cuc", "egg",
                     "fig", "goa", "gra", "har"],
            "app" : ["alm", "ani", "bac", "bet", "bbe", "bpu", "blb", "but",
                     "cab", "crt", "cel", "cin", "clo", "cse", "har", "haz",
                     "hor"],
            "apr" : ["alm", "car", "cho", "cin", "cum", "gin", "goa", "har"],
            "asp" : ["alm", "ani", "egg", "har"],
            "aub" : ["bel", "chi", "gar", "gin"],
            "avo" : ["bac", "blc", "chk", "chi", "cho", "cof", "cle", "cuc",
                     "dil", "gra", "gfr", "haz"],
            "bac" : ["ani", "app", "avo", "ban", "bef", "bel", "bpu", "blc",
                     "bro", "but", "cab", "car", "chk", "chi", "cho", "clo",
                     "egg", "glo", "har", "hor"],
            "ban" : ["alm", "ani", "bac", "car", "cav", "chr", "chk", "cho",
                     "cin", "coc", "cof", "egg", "har", "haz"],
            "bas" : ["ani", "chk", "clo", "coc", "egg", "gar", "goa", "har"],
            "bef" : ["anc", "ani", "bac", "bet", "bel", "bbe", "blc", "bro",
                     "cab", "cap", "crt", "cel", "chi", "cin", "clo", "coc",
                     "cof", "dil", "egg", "gar", "gin", "har", "hor", "jun"],
            "bet" : ["anc", "app", "bef", "cap", "cho", "coc", "cum", "dil",
                     "egg", "goa", "hor"],
            "bel" : ["aub", "bac", "bef", "chk", "chi", "egg"],
            "bbe" : ["alm", "app", "bef", "goa"],
            "bcu" : ["alm", "ani", "cho", "cof", "jun"],
            "bpu" : ["app", "bac", "cho", "egg"],
            "blb" : ["alm", "app", "blc", "cin", "cse"],
            "blc" : ["avo", "bac", "bef", "blb", "bro", "but", "cab", "cel",
                     "chk", "fig", "gra", "gfr"],
            "bro" : ["anc", "bac", "bef", "blc", "cau", "chi", "gar", "har"],
            "but" : ["alm", "app", "bac", "blc", "chs", "chi", "cin", "gin",
                     "goa"],
            "cab" : ["app", "bac", "bef", "blc", "crt", "chs", "chk", "chi",
                     "egg", "gar", "gin", "jun"],
            "cap" : ["anc", "bef", "bet", "cau", "cuc", "goa"],
            "car" : ["alm", "apr", "bac", "ban", "crt", "cho", "cin", "coc",
                     "cof", "cse", "gin"],
            "crt" : ["ani", "app", "bef", "cab", "car", "cel", "cin", "coc",
                     "cuc", "cum", "haz"],
            "cau" : ["alm", "anc", "bro", "cap", "cav", "chi", "cho", "cum",
                     "gar", "har"],
            "cav" : ["ban", "cau", "chk", "egg", "haz"],
            "cel" : ["app", "bef", "blc", "crt", "chs", "chk", "egg", "hor"],
            "chr" : ["alm", "ban", "cho", "cin", "coc", "cof", "goa", "haz"],
            "chs" : ["but", "cab", "cel", "chk", "cho"],
            "chk" : ["alm", "ani", "avo", "bac", "ban", "bas", "bel", "blc",
                     "cab", "cav", "cel", "chs", "chi", "coc", "cle", "egg",
                     "gar", "gra", "har", "haz"],
            "chi" : ["alm", "anc", "ani", "aub", "avo", "bac", "bef", "bel",
                     "bro", "but", "cab", "cau", "chk", "cho", "coc", "cle",
                     "egg", "gar", "gin", "goa", "har"],
            "cho" : ["alm", "ani", "apr", "avo", "bac", "ban", "bet", "bcu",
                     "bpu", "car", "cau", "chr", "chs", "chi", "cin", "coc",
                     "cof", "fig", "gin", "goa", "haz"],
            "cin" : ["alm", "ani", "app", "apr", "ban", "bef", "blb", "but",
                     "car", "crt", "chr", "cho", "clo", "coc", "cof", "fig",
                     "gin", "gfr"],
            "clo" : ["app", "bac", "bas", "bef", "cin", "cof", "gin", "har"],
            "coc" : ["alm", "anc", "ani", "ban", "bas", "bef", "bet", "car",
                     "crt", "chr", "chk", "chi", "cho", "cin", "cle", "dil",
                     "egg"],
            "cof" : ["alm", "avo", "ban", "bef", "bcu", "car", "chr", "cho",
                     "cin", "clo", "cse", "gin", "goa", "haz"],
            "cle" : ["avo", "chk", "chi", "coc", "cse", "cum", "gar", "goa"],
            "cse" : ["app", "blb", "car", "cof", "cle", "cum", "gar", "goa"],
            "cuc" : ["ani", "avo", "cap", "crt", "cum", "dil", "gar", "goa"],
            "cum" : ["apr", "bet", "crt", "cau", "cle", "cse", "cuc", "egg"],
            "dil" : ["avo", "bef", "bet", "coc", "cuc", "egg"],
            "egg" : ["anc", "ani", "asp", "bac", "ban", "bas", "bef", "bet",
                     "bel", "bpu", "cab", "cav", "cel", "chk", "chi", "coc",
                     "cum", "dil", "gin"],
            "fig" : ["alm", "ani", "blc", "cho", "cin", "goa", "har", "haz"],
            "gar" : ["alm", "anc", "aub", "bas", "bef", "bro", "cab", "cau",
                     "chk", "chi", "cle", "cse", "cuc", "gin", "goa", "haz"],
            "gin" : ["alm", "apr", "aub", "bef", "but", "cab", "car", "chi",
                     "cho", "cin", "clo", "cof", "egg", "gar"],
            "glo" : ["bac", "har"],
            "goa" : ["ani", "apr", "bas", "bet", "bbe", "but", "cap", "chr",
                     "chi", "cho", "cof", "cle", "cse", "cuc", "fig", "gar"],
            "gra" : ["alm", "ani", "avo", "blc", "chk", "har"],
            "gfr" : ["avo", "blc", "cin", "jun"],
            "har" : ["alm", "anc", "ani", "app", "apr", "asp", "bac", "ban",
                     "bas", "bef", "bro", "cau", "chk", "chi", "clo", "fig",
                     "glo", "gra", "jun"],
            "haz" : ["alm", "app", "avo", "ban", "crt", "cav", "chr", "chk",
                     "cho", "cof", "fig", "gar"],
            "hor" : ["app", "bac", "bef", "bet", "cel"],
            "jun" : ["bef", "bcu", "cab", "gfr", "har"],
            }

print len(flavours)
check_well_defined(flavours, pairings)

comp_subs = find_complete_subgraphs(flavours, pairings, ["hor"])

print comp_subs

print most_similar(flavours, pairings)
