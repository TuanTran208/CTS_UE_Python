import unreal


def get_focused_level_seq():
    return unreal.LevelSequenceEditorBlueprintLibrary.get_focused_level_sequence()


def get_control_rigs_in_lev_seq(seq):
    return unreal.ControlRigSequencerLibrary.get_control_rigs(seq)


def parent_external_window(window):
    unreal.parent_external_window_to_slate(window.winId())
