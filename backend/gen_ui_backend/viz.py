import pygraphviz as pgv
from langgraph import LangGraph
from .chain import create_graph

def generate_graph_visualization():
    graph = create_graph()
    app = graph.compile()

    # Draw the graph to a PNG file
    app.get_graph().draw('output.png', prog='dot', format='png')

    # Alternatively, draw the graph to an ASCII representation
    print(app.get_graph().string())

if __name__ == "__main__":
    generate_graph_visualization()
