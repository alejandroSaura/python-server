import Image
import sys
import fbx

filepath = 'cubeman/cubeMan.fbx'

manager = fbx.FbxManager.Create()
importer = fbx.FbxImporter.Create(manager, 'myImporter')

status = importer.Initialize(filepath)
if status == False :
  print 'fbx initialization failed'
  print 'Error: %s' % importer.GetLastErrorString()
  sys.exit()

scene = fbx.FbxScene.Create( manager, 'myScene')
importer.Import(scene)
importer.Destroy()

root = scene.GetRootNode()

vertexCount = 0

def countVertex (node) :
    global vertexCount
    mesh = node.GetMesh()
    if(mesh != None) :
      vertexCount = vertexCount + mesh.GetControlPointsCount()
    childNumber = node.GetChildCount()
    count = list(range(childNumber))
    for i in count:
        countVertex(node.GetChild(i))


countVertex(root)
print'number of vertex: %s' % vertexCount




