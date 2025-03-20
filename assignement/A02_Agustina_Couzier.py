#r: networkx
#r: matplotlib

import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore

#create a Graph
G = nx.Graph()

#add nodes
G.add_node('CABA')
G.add_node('Rosario')
G.add_node('Cordoba')
G.add_node('Mendoza')
G.add_node('Jujuy')
G.add_node('Salta')
G.add_node('Bariloche')
G.add_node('Parana')
G.add_node('Calafate')
G.add_node('Santa Fe')
G.add_node('Arminda')
G.add_node('San Juan')
G.add_node('La Pampa')
G.add_node('La Cumbre')
G.add_node('Melincue')
G.add_node('Pilar')
G.add_node('Posadas')
G.add_node('Tucuman')
G.add_node('Pinamar')


#add edges
G.add_edge('CABA', 'Rosario')
G.add_edge('CABA', 'Cordoba')
G.add_edge('CABA', 'Bariloche')
G.add_edge('CABA', 'La Pampa')
G.add_edge('CABA', 'Pilar')
G.add_edge('CABA', 'Pinamar')
G.add_edge('Rosario', 'Cordoba')
G.add_edge('Rosario', 'Mendoza')
G.add_edge('Rosario', 'Parana')
G.add_edge('Rosario', 'Santa Fe')
G.add_edge('Rosario', 'Arminda')
G.add_edge('Rosario', 'Melincue')
G.add_edge('Rosario', 'Pilar')
G.add_edge('Cordoba', 'Mendoza')
G.add_edge('Cordoba', 'Santa Fe')
G.add_edge('Cordoba', 'La Cumbre')
G.add_edge('Mendoza', 'Jujuy')
G.add_edge('Mendoza', 'San Juan')
G.add_edge('Jujuy', 'Salta')
G.add_edge('Jujuy', 'Posadas')
G.add_edge('Salta', 'Posadas')
G.add_edge('Salta', 'Tucuman')
G.add_edge('Bariloche', 'Calafate')
G.add_edge('Santa Fe', 'Parana')
G.add_edge('La Pampa', 'Bariloche')
G.add_edge('La Pampa', 'Pinamar')

#add position to display
pos = nx.spring_layout(G)

#draw serttings
fig = plt.figure(figsize=(15,15))
ax = plt.subplot()
ax.set_title('Graph', fontsize=12)
nx.draw(G, pos, node_size=1100, with_labels=True, node_color='black', font_size=7, font_color='white')

#draw the graph
plt.tight_layout()


#plot
path= r"C:\Users\agusc\Desktop\MPDA\AT-APY\session 2\Session02Homework\images\ArgentinianRoutes.png"
plt.savefig(path, format="PNG")