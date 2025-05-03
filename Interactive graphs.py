from main import all_routes, dijkstras_graph
import networkx as nx
import pygame
import sys

### Initializing Pygame ###
pygame.init()
run, graph_show = True, True
clock = pygame.time.Clock()
screen_width, screen_height = 1465, 800
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("Graph Theory/Visuals/All Syracuse Shuttle Routes Graph1.png")

### Sprite Group for nodes ###
button_group = pygame.sprite.Group()
# gather node locations by using node names in one list then append clicks from pygame to loc list then zip print and paste to script
node_locations = {'College Place': (728, 144), 'N.V.C': (632, 173), 'Forestry Gate': (542, 159), 'Winding Ridge': (420, 188), 
                  'BBB': (425, 245), 'Quad Lot': (318, 255), 'Small & Lambreth': (281, 316), 'Flint Hall': (291, 376), 
                  'Irving Garage': (279, 423), 'Sadler Hall': (283, 478), 'Walnut Ave': (326, 533), 'Warehouse': (425, 557), 
                  'Colvin Lot': (453, 600), 'Goldstein': (560, 622), 'Henry St.': (658, 642), 'Comstock Ave': (768, 635), 
                  'Shaw Hall': (881, 640), 'Syracuse Stage': (944, 598), 'Peck Hall': (1036, 593), 'Barnes Center': (1107, 547), 
                  'Skytop Offices': (1188, 511), 'Lawrinson Garage': (1184, 457), 'Comstock Lot': (1203, 400), 'Dellplain': (1242, 347), 
                  'University Ave': (1094, 311), 'Campus West': (1202, 274), 'Life Sciences': (1110, 208), 'Slocum & Lambreth': (1018, 208), 
                  'Waverly Ave. Lot': (937, 165), 'Schine Student Center': (829, 162)}

### Run loop for game ###
while run:
    ### getting player events, if user clicks node display background changes to dijkstra path, if ESC return to all_route grph
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN and graph_show == True: # checking if user clicks on node & all_routes graph is displayed.
            pos = pygame.mouse.get_pos()
            for node, loc in node_locations.items():
                if abs(loc[0] -pos[0]) < 30 and abs(loc[1] - pos[1]) < 30: ### Margin of error for click allowing for larger click radius
                    path = nx.dijkstra_path(all_routes,'College Place', str(node))
                    time = nx.dijkstra_path_length(all_routes,'College Place',str(node))
                    dijkstras_graph(path, time) 
                    background = pygame.image.load("Graph Theory/Visuals/Dijkstra.png") 
                    graph_show = False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    background = pygame.image.load("Graph Theory/Visuals/All Syracuse Shuttle Routes Graph1.png")
                    graph_show = True

        if event.type == pygame.QUIT:
            # dict1 = dict(zip(location_names, loc_position))
            # print(dict1)
            pygame.quit()
            sys.exit()


    ### Object Loading ###
    button_group.update()
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    button_group.draw(screen)
    pygame.display.flip()
    clock.tick()

