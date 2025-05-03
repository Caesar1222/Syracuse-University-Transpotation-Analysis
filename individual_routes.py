import networkx as nx
import matplotlib.pyplot as plt


def south_campus_Loop():
    south_loop = nx.DiGraph()
    # weighted_edges1 =[('College Place', 'Comstock Lot', 6), ('Comstock Lot', 'Colvin Lot', 2), 
    #                 ('Colvin Lot', 'Small & Lambreth', 6), ('Small & Lambreth', 'Slocum & Lambreth', 2),
    #                 ('Slocum & Lambreth', 'Winding Ridge', 2), ('Winding Ridge', 'Skytop Offices', 2), 
    #                 ('Skytop Offices', 'Goldstein', 2), ('Goldstein', 'College Place', 20)]   
    weighted_edges1 =[('CP', 'CL', 6), ('CL', 'Colvin', 2), 
                ('Colvin', 'Sm&L', 6), ('Sm&L', 'Sl&L', 2),
                ('Sl&L', 'WR', 2), ('WR', 'Sky', 2), 
                ('Sky', 'Gld', 2), ('Gld', 'CP', 20)]   
    south_loop.add_weighted_edges_from(weighted_edges1)
    pos = nx.kamada_kawai_layout(south_loop)
    nx.draw(south_loop, pos, with_labels=True, edge_color='red', node_size=700, node_color='lightgrey')
    edge_labels1 = nx.get_edge_attributes(south_loop, 'weight')
    nx.draw_networkx_edge_labels(south_loop, pos, edge_labels=edge_labels1)
    return south_loop


def warehouse_loop():
    coms = nx.DiGraph()
    # weighted_edges2 = [('College Place', 'BBB', 2), ('BBB', 'Syracuse Stage',3), ('SStage', 'Peck Hall', 5), 
    #                    ('Peck Hall','Warehouse',5),('Warehouse', 'Peck Hall', 9), ('Peck Hall', 'Syracuse Stage', 3), 
    #                    ('Syracuse Stage', 'Schine Student Center', 3), ('Schine Student Center', 'College Place', 5)]
    weighted_edges2 = [('CP', 'BBB', 2), ('BBB', 'SStage',3), ('SStage', 'PeckH', 5), 
                    ('PeckH','WH',5),('WH', 'PeckH', 9), ('PeckH', 'SStage', 3), 
                    ('SStage', 'SSC', 3), ('SSC', 'CP', 5)]
    coms.add_weighted_edges_from(weighted_edges2)
    pos = nx.kamada_kawai_layout(coms)
    nx.draw(coms, pos, with_labels=True, edge_color='grey', node_size=700, node_color='lightgrey')
    edge_labels1 = nx.get_edge_attributes(coms, 'weight')
    nx.draw_networkx_edge_labels(coms, pos, edge_labels=edge_labels1)
    return coms


def orange_loop():
    G = nx.DiGraph()
    # weighted_edges=[("College Place","Flint Hall",4),("Flint Hall","Shaw Hall",2),("Shaw Hall","Barnes Center",2),
    #                  ("Barnes Center","Forestry Gate",3),("Forestry Gate","BBB",2),("BBB","Campus West",1),
    #                  ("Campus West","Henry St.",1),("Henry St.","Lawrinson Garage",1),("Lawrinson Garage","Irving Garage",5),
    #                  ("Irving Garage","Quad Lot ",5),("Quad Lot","N.V.C",3),("N.V.C","University Ave",2),
    #                  ("University Ave","Schine Student Center",2),  ("Schine Student Center","Comstock Ave",2),("Comstock Ave","Dellplain",2),("Dellplain","College Place",1)]
    weighted_edges=[("CP","FlintH",4),("FlintH","ShawH",2),("ShawH","Barnes",2),
                     ("Barnes","FGate",3),("FGate","BBB",2),("BBB","CWest",1),
                     ("CWest","HSt",1),("HSt","LG",1),("LG","IG",5),
                     ("IG","Quad",5),("Quad","N.V.C",3),("N.V.C","UniAve",2),
                     ("UniAve","SSC",2),  ("SSC","ComAve",2),("ComAve","Dell",2),("Dell","CP",1)]
   
    G.add_weighted_edges_from(weighted_edges)
    pos= nx.kamada_kawai_layout(G)
    nx.draw(G,pos,with_labels=True,edge_color="orange", node_size=400, node_color='lightgrey')
    edge_labels = nx.get_edge_attributes(G,"weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    return G


def blue_loop():
    G = nx.DiGraph()
    # weighted_edges= [("College Place","Flint Hall",5),("Flint Hall","Shaw Hall",5),("Shaw Hall","Life Sciences",2),
    #                 ("Life Sciences","Comstock Ave Garage",3),("Comstock Ave Garage","Waverly Ave. Lot",2),("Waverly Ave. Lot","Walnut Ave",2),
    #                 ("Walnut Ave","University Ave",1),("University Ave","N.V.C",2),("N.V.C","Quad Lot",2),
    #                 ("Quad Lot","BBB",4),("BBB","Campus West",1),("Campus West","Henry St.",1),("Henry St.","irving Garage",5),  
    #                 ("irving Garage","Sadler Hall",1),("Sadler Hall","Barnes Center",3),("Barnes Center","College Place",1)]
    weighted_edges= [("CP","FlintH",5),("FlintH","ShawH",5),("ShawH","LifeSci",2),
                    ("LifeSci","ComAve",3),("ComAve","Waverly",2),("Waverly","Walnut",2),
                    ("Walnut","UniAve",1),("UniAve","N.V.C",2),("N.V.C","Quad",2),
                    ("Quad","BBB",4),("BBB","CWest",1),("CWest","HSt.",1),("HSt.","IG",5),  
                    ("IG","SadlerH",1),("SadlerH","Barnes",3),("Barnes","CP",1)]
    
    G.add_weighted_edges_from(weighted_edges)
    pos= nx.kamada_kawai_layout(G)
    nx.draw(G,pos,with_labels=True,edge_color="blue", node_size=400, node_color='lightgrey')
    edge_labels = nx.get_edge_attributes(G,"weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    return G


def comstock_loop():
    G = nx.DiGraph()
    weighted_edges = [('College Place','Comstock Lot', 5), ('Comstock Lot', 'Colvin Lot', 2)]
    G.add_weighted_edges_from(weighted_edges)
    pos= nx.kamada_kawai_layout(G)
    nx.draw(G,pos,with_labels=True,edge_color="purple", node_size=400, node_color='lightgrey')
    edge_labels = nx.get_edge_attributes(G,"weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    return G
