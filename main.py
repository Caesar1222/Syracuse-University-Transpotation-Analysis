### This program is for SOURCE Explore!!! ####
from individual_routes import south_campus_Loop, warehouse_loop, orange_loop, blue_loop, comstock_loop
import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate
import math

plt.rcParams['font.family'] = 'serif' # Sets the general font family
plt.rcParams['font.serif'] = 'Times New Roman'

plt.figure(figsize=(14.65, 8.0))
all_routes = nx.MultiDiGraph()

### Route Edges ###
south_campus_edges =[('College Place', 'Comstock Lot', 6), ('Comstock Lot', 'Colvin Lot', 2), 
                    ('Colvin Lot', 'Small & Lambreth', 6), ('Small & Lambreth', 'Slocum & Lambreth', 2),
                    ('Slocum & Lambreth', 'Winding Ridge', 2), ('Winding Ridge', 'Skytop Offices', 2), 
                    ('Skytop Offices', 'Goldstein', 2)]   

warehouse_edges = [('College Place', 'BBB', 2), ('BBB', 'Syracuse Stage',3), ('Syracuse Stage', 'Peck Hall', 5), 
                       ('Peck Hall','Warehouse',5),('Warehouse', 'Peck Hall', 9), ('Peck Hall', 'Syracuse Stage', 3), 
                       ('Syracuse Stage', 'Schine Student Center', 3)]

orange_loop_edges = [("College Place","Flint Hall",4),("Flint Hall","Shaw Hall",2),("Shaw Hall","Barnes Center",2),
                     ("Barnes Center","Forestry Gate",3),("Forestry Gate","BBB",2),("BBB","Campus West",1),
                     ("Campus West","Henry St.",1),("Henry St.","Lawrinson Garage",1),("Lawrinson Garage","Irving Garage",5),
                     ("Irving Garage","Quad Lot",5),("Quad Lot","N.V.C",3),("N.V.C","University Ave",2),
                     ("University Ave","Schine Student Center",2),  ("Schine Student Center","Comstock Ave",2),("Comstock Ave","Dellplain",2)]

blue_loop_edges=[("College Place","Flint Hall",5),("Flint Hall","Shaw Hall",5),("Shaw Hall","Life Sciences",2),
                    ("Life Sciences","Comstock Ave",3),("Comstock Ave","Waverly Ave. Lot",2),("Waverly Ave. Lot","Walnut Ave",2),
                    ("Walnut Ave","University Ave",1),("University Ave","N.V.C",2),("N.V.C","Quad Lot",2),
                    ("Quad Lot","BBB",4),("BBB","Campus West",1),("Campus West","Henry St.",1),("Henry St.","Irving Garage",5),  
                    ("Irving Garage","Sadler Hall",1),("Sadler Hall","Barnes Center",3)]

comstock_edges = [('College Place','Comstock Lot', 5), ('Comstock Lot', 'Colvin Lot', 2)]

### Routes and Colors Dics ###
routes ={
    'South Loop': (south_campus_edges, 'red'),
    'Warehouse Loop': (warehouse_edges, 'green'),
    'Orange Loop': (orange_loop_edges, 'orange'),
    'Blue Loop': (blue_loop_edges, 'blue'),
    'Comstock': (comstock_edges, 'purple')
}

### All Routes Graph ###
for route, edges in routes.items():
    for u, v, w in edges[0]:
        all_routes.add_edge(u, v, weight=w, route=route, color=edges[1])
# Drawing graph 
pos = nx.spring_layout(all_routes, seed=42, k=5, scale=5)
nx.draw_networkx_nodes(all_routes, pos, node_color='lightgray', node_size=900)

for (u, v, key, data) in all_routes.edges(keys=True, data=True):
    nx.draw_networkx_edges(all_routes, pos, edgelist=[(u, v)], edge_color=[data['color']],
                           connectionstyle=f"arc3,rad={0.25 * (key + 1)}",
                           arrowstyle='-|>',
                           min_source_margin=15, min_target_margin=15,  # Ensures arrows don't enter nodes
                           arrowsize=20, width=2)
edge_labels = {(u, v): data["weight"] for u, v, k, data in all_routes.edges(keys=True, data=True)}
nx.draw_networkx_edge_labels(all_routes, pos, edge_labels=edge_labels, font_size=0.5, font_color='black')

### Visual for Pygame ###
nx.draw_networkx_labels(all_routes, pos, font_size=8, font_color='black', font_weight='bold')
plt.title("Click on your destination and shortest path starting from College Place will appear!", fontsize = 20)
plt.savefig('Graph Theory/Visuals/All Syracuse Shuttle Routes Graph1.png')

### Visual for Poster ###
plt.title("'Cuse Shuttle Route Network with Directed Multi-Edges & Weights", fontsize=20)
plt.legend(['Bus Stop','South Loop', 'Comstock Loop', 'Warehouse Loop', 'Orange Loop', 'Blue Loop'], loc= 'upper left', frameon = True, fontsize = 8)
plt.savefig('Graph Theory/Visuals/All Syracuse Shuttle Routes Graph.png')
plt.close()

### Creating Visual for All Routes as individual Graphs ###
fig,ax = plt.subplots(2,2,figsize=(19.2,10.8))
fig.suptitle('Individual Routes Graph', fontsize=30)

### South Campus Loop Plot 
ax[0,0].set_title('South Campus Loop Graph')
plt.subplot(221)
s =south_campus_Loop()

### Warehouse Loop Plot 
ax[0,1].set_title('Warehouse Loop Graph')
plt.subplot(222)
w = warehouse_loop()

### Blue Loop Plot
ax[1,0].set_title('Blue Loop Graph')
plt.subplot(223)
b = blue_loop()

### Orange Loop Plot
ax[1,1].set_title('Orange Loop Graph')
plt.subplot(224)
o = orange_loop()

### Saving plot as png image ###
fig.savefig('Graph Theory/Visuals/Individual Shuttle Route Graphs.png')
plt.close()

### Table of shortest paths starting from College Place ###
header = ['start', 'Destination', 'Time to Arrive', 'Optimal Path', 'loop name']
data = []

locations = list(all_routes.nodes())
locations.remove('College Place')

# ### making table to display Dijkstra algorithm applied to all stops using College Place as the Source ###
# for loc in locations:
#     data.append(['CP', str(loc), nx.dijkstra_path_length(all_routes, 'CP', str(loc), weight = 'weight'),
#                     nx.dijkstra_path(all_routes, 'CP', str(loc), weight = 'weight') ])
# print(tabulate(data, headers=header, tablefmt='grid'))
# #########################################################################################################

### Utilizing output path of Dijkstra's graph to form a sub graph to display when user clicks destination (sort of like GPS) ###
def dijkstras_graph(path, t):
    edges =[]
    nodes = list(path)
    nodes.reverse() # Reversing path in order to display graph starting from College Place

    ### making and ploting graph
    plt.figure(figsize=(14.65, 8.0))
    plt.title("Press Escape in order to try another destination!", fontsize = 20)
    G = nx.Graph()
    G.add_nodes_from(nodes)
    for i in range(1,len(nodes)): # loop through nodes in order to form edges connecting a node n+1 to n
        edge = (nodes[i-1], nodes[i])
        edges.append(edge)
    G.add_edges_from(edges)
    pos= nx.kamada_kawai_layout(G)
    nx.draw(G,pos, node_size = 1200,  with_labels = True, node_color='lightgray')
    plt.legend([f'Total Time: {t} min '], loc = 'upper left', frameon = True, fontsize = 30)
    plt.savefig('Graph Theory/Visuals/Dijkstra.png')
    plt.close()

''' which stop is the best/ has the shortest average time to arrive to every location if all averages are equal, 
 then we can conclude the bus system is optimal'''

# loop through every stop as the source for dijkstra's algorithm; then find shortest path to every other source, take average of all lengths.
# lastly determine which source had shortest average, O(n^2) time :( 
# I understand this is upcoming code is not the ruiner of the programs time complexity however it may just be the most time consuming process 
# for this file.

dijkstra_paths_all_nodes = {}
path_sums = 0

for source in locations:
    for target in locations:
        if target != source:   
            try: 
                path_sums += nx.dijkstra_path_length(all_routes.to_undirected(), source, target) # graph becomes undirected since buses loop
                # print(nx.dijkstra_path(all_routes.to_undirected(), source, target))
            except:
                print(f"unfortunately {target} is not reahcable from {source}")
    dijkstra_paths_all_nodes[source] = math.ceil(path_sums/(len(locations)-1))
    path_sums = 0

min_time = min(dijkstra_paths_all_nodes.values())
for val in dijkstra_paths_all_nodes.keys():
    if dijkstra_paths_all_nodes[val] == min_time:
        print(val, min_time)
print(dijkstra_paths_all_nodes)


### Determining which of the four loops are oversaturated with stops ###





