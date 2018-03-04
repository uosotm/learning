bl_info = {
    "name": "My first blender addon",
    "author": "uosotm",
    "version": (2, 0),
    "blender": (2, 79, 0),
    "location": "",
    "description": "A sample addon which does nothing.",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

def register():
    print('The sample addon has been enabled')
    
def unregister():
    print('The sample addon has been disabled')

if __name__ == '__main__':
    register()