import re
from graph import SparseGraph 
def buildGraphFromFile(aGraph,filePath):
    graphList=[]
    with open(filePath,'r',encoding='utf-8') as f:
        for line in f:
            graphList.append([int(x) for x in re.split(r'\s+',line.strip())])
    for i in range(len(graphList)):
        aGraph.add_edge(graphList[i][0],graphList[i][1])
g2=SparseGraph()

buildGraphFromFile(g2,'testG1.txt')
print ("所有的点为:",g2.get_node())
print ("邻接表:",g2.show())
g2.cal_cc()
print ("连通分量的个数为:",g2.get_cc())
node1 = 6
node2 = 4
print (node1,"和",node2,"两个点是否连接(非相邻):",g2.is_connected(node1,node2))
print (node1,"和",node2,"两个点之间的路径为(dfs):",g2.get_path(node1,node2))
print (node1,"和",node2,"两个点之间的最短路径为(bfs):",g2.get_shortest_path(node1,node2))
