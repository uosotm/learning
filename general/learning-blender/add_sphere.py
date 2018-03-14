import bpy


bl_info = {
    "name": "Add Sphere",
    "author": "uosotm",
    "version": (2, 0),
    "blender": (2, 79, 0),
    "location": "3D View > Add > Mesh",
    "description": "To create ICO sphere",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}


class CreateObject(bpy.types.Operator):

    bl_idname = "object.create_object"
    bl_label = "Sphere"
    bl_description = "Add ICO sphere"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.primitive_ico_sphere_add()
        print("Created ICO sphere in 3D View")

        return {'FINISHED'}


def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(CreateObject.bl_idname)

def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_mesh_add.append(menu_fn)
    
def unregister():
    bpy.types.INFO_MT_mesh_add.remove(menu_fn)
    bpy.utils.unregister_module(__name__)

if __name__ == '__main__':
    register()
