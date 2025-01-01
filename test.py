import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
st.set_page_config(layout="wide", page_title="Dashboard")
# Define nodes
nodes = [
    Node(
        id="1",
        label="\n\n        Node 1         \n\n\n[Details]\n\n",
        shape="box",
        color={"border": "white", "background": "#131727"},
        font={"color": "white"},
        size=50
    ),
    Node(
        id="2",
        label="\n\n        Node 2         \n\n\n[Details]\n\n",
        shape="box",
        color={"border": "white", "background": "#131727"},
        font={"color": "white"},
        size=50
    ),
    Node(
        id="3",
        label="\n\n        Node 3         \n\n\n[Details]\n\n",
        shape="box",
        color={"border": "white", "background": "#131727"},
        font={"color": "white"},
        size=50
    )
]

# Define edges with labels and custom font styling
edges = [
    Edge(
        source="1",
        target="2",
        color="#00FFE0",
        width=2,
        label="                  normal",
        font={"strokeWidth": 0, "color": "white"}
    ),
    Edge(
        source="1",
        target="3",
        color="#00FFE0",
        width=2,
        label="                  chat",
        font={"strokeWidth": 0, "color": "white"}
    )
]

# Configuration for the graph
config = Config(
    width=1500,
    height=1300,
    directed=True,
    physics=False,
    hierarchical=True,  # Enable hierarchical layout
    layout={
        'hierarchical': {
            'sortMethod': 'directed',  # Position nodes based on their edges
            'direction': 'UD',        # Top-to-bottom (Up-Down) layout
            'nodeSpacing': 300,       # Spacing between sibling nodes
            'levelSeparation': 300    # Vertical distance between levels
        }
    },
    center={'x': 0, 'y': -500}  # Adjust center of the graph
)

# Render the graph and capture the selection
selection = agraph(nodes=nodes, edges=edges, config=config)

# Define the URL to open upon node selection

# Check if a node is selected
if selection:
    print (selection)