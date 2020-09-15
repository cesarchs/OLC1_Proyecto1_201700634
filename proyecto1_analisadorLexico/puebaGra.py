from graphviz import Digraph
from graphviz import *

dot = Digraph(comment='REPORTE CSS')
dot = Source('digraph "the holy hand grenade" { rankdir=LR;      size=\"8,5\" node [shape = doublecircle]; S_0 IDENT NUM; node [shape = circle]; S_0 -> IDENT [ label = \"letra\" ]; S_0 -> S_0 [ label = \"simb\" ]; S_0 -> NUM [ label = \"numero\" ]; IDENT -> NUM [ label = \"numero\" ]; IDENT -> S_0 [ label = \"simb\" ]; IDENT -> IDENT [ label = \"letra\" ]; NUM -> IDENT [ label = \"letra\" ]; NUM -> S_0 [ label = \"simb\" ]; NUM -> NUM [ label = \"numero\" ]; NUM -> NUM [ label = \"punto\" ]; coment -> S_0 [label = \"\\n,*/\"]; coment -> NUM [label = \"\\n,*/\"]; coment -> IDENT [label = \"\\n,*/\"]; coment -> coment [label = \"caracter\"]; IDENT -> coment [ label = \"//,/*\" ]; NUM -> coment [ label = \"//,/*\" ];  S_0 -> coment [ label = \"//,/*\" ]; error -> S_0 [label = \"Simb.\"]; error -> NUM [label = \"Numero\"]; error -> IDENT [label = \"letra\"]; error -> error [label = \"Desc.\"]; error -> coment [label = \"//,/*\"]; IDENT -> error [ label = \"Desc.\" ]; NUM -> error [ label = \"Desc.\" ]; S_0 -> error [ label = \"Desc.\" ]; }')


# dot.node('A', 'King Arthur')
# dot.node('B', 'Sir Bedevere the Wise')
# dot.node('L', 'Sir Lancelot the Brave')

# dot.edges(['AB', 'AL'])
# dot.edge('B', 'L', constraint='false')

# print(dot.source)

dot.render('test-output/round-table.gv', view=True)  