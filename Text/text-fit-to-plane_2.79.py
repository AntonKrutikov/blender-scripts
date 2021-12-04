#Text fit to plane

import bpy

mesh = next(filter(lambda o: o.type=='MESH', bpy.context.selected_objects), None)
text = next(filter(lambda o: o.type=='FONT', bpy.context.selected_objects), None)

if mesh is not None and text is not None:
    #make text children of plane
    text.parent = mesh
    
    #set bounding box width = mesh width
    text.data.text_boxes[0].width = mesh.dimensions.x
    #text.data.overflow = 'SCALE'
    
    #set text as current active property
    bpy.context.scene.objects.active = text
    #reset geometry (hack for make pivot point in center of text)
    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='MEDIAN')
    
    #put text on plane
    text.location.x = 0
    text.location.y = 0
    text.location.z = 0
    
    #reset text scaling if exists
    text.scale.x =1
    text.scale.y =1
    text.scale.z =1
    
    #reset rotation
    text.rotation_euler[0] =0
    text.rotation_euler[1] =0
    text.rotation_euler[2] =0