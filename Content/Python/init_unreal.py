import unreal
import os
import sys

# Core
cts_ue_python = os.path.dirname(__file__)
if cts_ue_python not in sys.path:
    sys.path.append(cts_ue_python)

# Add dependencies
dependencies = os.path.join(os.path.dirname(__file__), "dependencies")
if dependencies not in sys.path:
    sys.path.append(dependencies)

unreal.log("""@

####################

 Unreal Init Script

####################

""")


def create_python_tool_menu_entry(name, label, command_string="", entry_type=unreal.MultiBlockType.MENU_ENTRY):
    menu_entry = unreal.ToolMenuEntry(name, type=entry_type)
    menu_entry.set_label(label)
    if command_string:
        menu_entry.set_string_command(
            unreal.ToolMenuStringCommandType.PYTHON, "python", command_string
        )
    return menu_entry


def create_menu_button(name, label, command_string=""):
    return create_python_tool_menu_entry(name, label, command_string)


def get_toolbar():
    return unreal.ToolMenus.get().find_menu("LevelEditor.LevelEditorToolBar")


def create_toolbar_combo_button(name, section_name, tool_tip="", register_button=True):
    # menu_name = ".".join([str(get_toolbar().menu_name),menu])
    # section_name = ".".join([str(get_toolbar().menu_name), menu, section])
    # get_toolbar().add_section(section_name)
    # menu_entry_script = EditorToolbarMenuEntry(get_toolbar().menu_name, section_name, name, "", tool_tip, ["EditorStyle", "DetailsView.PulldownArrow.Down", "DetailsView.PulldownArrow.Down"], get_toolbar().menu_name, ["None", unreal.ToolMenuInsertType.DEFAULT], ["None", unreal.MultiBlockType.TOOL_BAR_COMBO_BUTTON, unreal.UserInterfaceActionType.BUTTON, True, True, True, False])
    # menu_entry_script.register_menu_entry()
    menu_entry = unreal.ToolMenuEntry(
        name, type=unreal.MultiBlockType.TOOL_BAR_COMBO_BUTTON
    )
    if register_button:
        get_toolbar().add_menu_entry(section_name, menu_entry)
    return menu_entry


def get_mainmenu_item(name):
    return unreal.ToolMenus.get().find_menu("MainFrame.MainMenu.{}".format(name))


def extend_mainmenu_item(mainmenu_name, section_name, name, label, tooltips=""):
    parent_menu = get_mainmenu_item(mainmenu_name)
    return parent_menu.add_sub_menu(
        parent_menu.menu_name, section_name, name, label, tooltips
    )


def extend_mainmenu(name, label, tooltip=""):
    main_menu = get_mainmenu()
    return main_menu.add_sub_menu(
        main_menu.menu_name, unreal.Name(), name, label, tooltip
    )


def get_mainmenu():
    return unreal.ToolMenus.get().find_menu("MainFrame.MainMenu")


def extend_editor():
    # Create standard menu entry
    me_reloadbutton = create_menu_button(
        name="ReloadUEPickerBtn",
        label="ReloadUEPicker",
        command_string="import UEPicker; UEPicker.reload_()",
    )

    pythonsubmenu = extend_mainmenu_item(
        "File", "PythonTools", "PythonTools", "Python Tools"
    )
    pythonsubmenu.add_section("python.file.menu", "Python Tools")
    pythonsubmenu.add_menu_entry("python.file.menu", me_reloadbutton)


extend_editor()
