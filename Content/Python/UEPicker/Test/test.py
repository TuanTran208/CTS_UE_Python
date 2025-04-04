import unreal

unreal.load_module('ControlRigDeveloper')

# import sys
# from PySide2 import QtWidgets 

# path_ = "C:/rndCharTech/UE/CharTech/Plugins/CTS_UE_Python/Content/Python" 
# if path_ not in sys.path:
#     sys.path.append(path_)
# from UEPicker import Bob

# class test(QtWidgets.QMainWindow):

#     DATA = ""

#     def __init__(self):
#         super(test, self).__init__()
#         self.ui = Bob.Ui_MainWindow()
#         self.ui.setupUi(self)

#         # l = sorted([i.track.get_display_name() for i in ctrlRigs])
#         self.ui.ctrlRigNames_cbx.addItems(["gsadjsgj","sadsas"])

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     ui = test()
#     ui.show()
#     sys.exit(app.exec_())

def run():
    # print(dir(rig))
    # rigs = unreal.ControlRigBlueprint.get_currently_open_rig_blueprints()

    # factory = unreal.ControlRigBlueprintFactory()
    # rig = factory.create_new_control_rig_asset(desired_package_path = '/Game/TestRig')

    # library = rig.get_local_function_library()
    # library_controller = rig.get_controller(library)
    # print(dir(hierarchy))
    # print(dir(unreal.ControlRigBlueprint))
    # for element in elements:
    #     if hierarchy.is_selected(element):
    #         print(element.name)
    # hierarchy_controller = hierarchy.get_controller()
    
    rig = unreal.load_object(name='/Game/Developers/Trainning_CtrlRig/CR_wolf_leg', outer = None)
    hierarchy = rig.hierarchy
    elements = hierarchy.get_all_keys()
    bones = hierarchy.get_bones()
    print([str(i.name) for i in hierarchy.get_selected_keys()])