import bpy


bl_info = {
    "name": "Scale Object",
    "author": "uosotm",
    "version": (2, 0),
    "blender": (2, 79, 0),
    "location": "3D View > Object",
    "description": "Enlarge and reduce selected object.",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}


class EnlargeObject(bpy.types.Operator):

    bl_idname = "object.enlarge_object"
    bl_label = "Enlarge"
    bl_description = "Enlarge selected object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        active_obj = context.active_object
        active_obj.scale = active_obj.scale * 2.0
        self.report({'INFO'}, "%s is enlarged" % (active_obj.name))
        print("Operation: %s has been executed" % (self.bl_idname))

        return {'FINISHED'}


class ReduceObject(bpy.types.Operator):

    bl_idname = "object.reduce_object"
    bl_label = "Reduce"
    bl_description = "Reduce selected object"

    def execute(self, context):
        active_obj = context.active_object
        active_obj.scale = active_obj.scale * 0.5
        self.report({'INFO'}, "%s is reduced" % (active_obj.name))
        print("Operation: %s has been executed" % (self.bl_idname))

        return {'FINISHED'}


def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(EnlargeObject.bl_idname)
    self.layout.operator(ReduceObject.bl_idname)

def register():
    bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_MT_object.append(menu_fn)
    print("Scale object add-on has been enabled")

def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_fn)
    bpy.utils.unregister_module(__name__)
    print("Scale object add-on has been disabled")


if __name__ == "__main__":
    register()
