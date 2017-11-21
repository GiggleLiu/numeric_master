#!/usr/bin/env python
test_str = '''
<LATTICES>
 <GRAPH name = "heisenberg" dimension="1" vertices="6" edges="5">
  <VERTEX id="1" type="0"><COORDINATE>0</COORDINATE></VERTEX>
  <VERTEX id="2" type="1"><COORDINATE>2</COORDINATE></VERTEX>
  <VERTEX id="3" type="1"><COORDINATE>3</COORDINATE></VERTEX>
  <VERTEX id="4" type="1"><COORDINATE>4</COORDINATE></VERTEX>
  <VERTEX id="5" type="1"><COORDINATE>5</COORDINATE></VERTEX>
  <VERTEX id="6" type="0"><COORDINATE>6</COORDINATE></VERTEX>
  <EDGE source="1" target="2" id="1" type="0" vector="1"/>
  <EDGE source="2" target="3" id="2" type="0" vector="1"/>
  <EDGE source="3" target="4" id="3" type="0" vector="1"/>
  <EDGE source="4" target="5" id="4" type="0" vector="1"/>
  <EDGE source="5" target="6" id="5" type="0" vector="1"/>
 </GRAPH>
</LATTICES>
'''
import lxml.etree as ET

def build_j1j2(size, filename):
    lattice = ET.Element('LATTICES')
    graph = ET.SubElement(lattice, 'GRAPH', attrib={'name':'J1J2',
        'dimension':'1', 'vertices':'%d'%size, 'edges':'%d'%(size-1)})
    for i in range(size):
        vi = ET.SubElement(graph, 'VERTEX', attrib={'id':'%d'%(i+1), 
            'type':'0'})
        co = ET.SubElement(vi, 'COORDINATE')
        co.text = '%d'%i

    for i in range(1,size+1):
        ET.SubElement(graph, 'EDGE', attrib={'source':'%d'%(i),'target':'%d'%((i)%size+1),
            'id':'%d'%i, 'type':'0', 'vector':'1'})
        ET.SubElement(graph, 'EDGE', attrib={'source':'%d'%(i),'target':'%d'%((i+1)%size+1),
            'id':'%d'%i, 'type':'1', 'vector':'1'})

    with open(filename, 'w') as f:
        f.write(ET.tostring(lattice, pretty_print=True))

if __name__ == '__main__':
    import sys
    nsite = int(sys.argv[1])
    build_j1j2(nsite, 'lattices/j1j2_%d.xml'%nsite)
