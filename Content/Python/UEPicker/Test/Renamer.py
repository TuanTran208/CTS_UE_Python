from pprint import pprint
import re
# import unreal

# # 開いているControlRigを取得する
# rigs = unreal.ControlRigBlueprint.get_currently_open_rig_blueprints()
# rig = rigs[0]

# # ControlRigHierarchyModifierを取得する
# # h_mod = rig.get_hierarchy_modifier()

# # 選択エレメントを取得する
# # elements = h_mod.get_selection()

# print(rig)

# # """------------------------------------------------
# #     スペース＆コントロール作成＆階層作成
# # ------------------------------------------------"""
# # parent=None
# # for element in elements:
# #     # スペースを作成する
# #     space = h_mod.add_space("{}_space".format(element.name), space_type=unreal.RigSpaceType.SPACE)

# #     # コントロールを作成する
# #     control = h_mod.add_control("{}_control".format(element.name), space_name=space.name)

# #     # スペースにボーンの初期トランスフォームを適用する
# #     bone_initial_transform = h_mod.get_initial_transform(element)
# #     h_mod.set_initial_transform(space, bone_initial_transform)

# #     # parent変数が空でない場合、ペアレントする(階層を作る部分)
# #     if parent is not None:
# #         h_mod.reparent_element(space, parent)
# #     parent = control

# filename = "D:/Projects/Cobra/UE5/Cobra/Content/Developers/thuynguyen/Python/copy.txt"
# with open(filename, "r+") as f:
#     data = f.read()
#     pattern = r'(Name=")(l|r)_([a-zA-Z0-9]*?)_'
#     x = re.findall(pattern, data)
#     # res = re.sub(pattern, r'\g<1>\g<3>_\g<2>_fk_', data)
#     res = re.sub(pattern, lambda pat: ( pat.group(1)+
#                                         pat.group(3).lower()+
#                                         "_"+pat.group(2)+"_fk_"), data)
#     # print(res)
#     f.seek(0)
#     f.write(res)
#     f.truncate()