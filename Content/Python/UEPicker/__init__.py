# from .designer_thuy import picker_2 as designer_picker_thuy
# from .cmds import picker_v2 as cmds_picker
# from .designer import picker as designer_picker
import sys, os, pprint
import importlib

def reload_():
    """
    """
    reloadSubModules(__path__[0],os.path.basename(os.path.dirname(__file__)))

def reloadSubModules(path, moduleName):
    """
    """
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            if not filename.endswith(".py"):
                continue
            if filename == "__init__.py":
                subModuleName = moduleName
            else:
                subModuleName = moduleName + "." +filename[:-3]
            print("reload: " + subModuleName)
            try:
                module = __import__(subModuleName, globals(), locals(),["*"],0)
                importlib.reload(module)
            except ImportError as e:
                for arg in e.args:
                    print("ImportError err: " + arg)
            except Exception as e:
                for arg in e.args:
                    print("Exception err: " + arg)
        for dirName in dirs:
            reloadSubModules(path+"/"+dirName, moduleName+"."+dirName)

        break
