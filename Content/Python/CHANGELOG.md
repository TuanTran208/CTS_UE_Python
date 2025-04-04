# Changelog

## [Unreleased]
## [2.0.1] - 2024-5-24
### Bug:
- Bug fix and optimize
- Convert old metanode => show warning if anim layer not exist

# Update:
- Color selection behavior
  - Click: Only selected anim seqs that belong to that color
  - Shift + click: multi-select anim sequence 
- Support multi-select for:
  - Set start, end frame by maya timeline
  - Apply selected object to "Asset Name" column
- Support edit custom export path on text field

# Add
- Set start, end frame by maya timeline
- Add some preset color
- Auto generated color button
  - Click: select
  - Shift + click: deselect

## [2.0.5] - 2024-7-8
### Updated:
- Create ue export node and attach it into anim sequence
    - Support modify skeleton, and import path
    - Support modify some options such as:
        - force_front_x_axis, uniform_scale, convert_scene,convert_scene_unit,import_uniform_scale

## [2.0.4] - 2024-7-5
### Bug:
- Can't duplicate, paste anim sequence item

### Add:
- Popup a basic dialog when create a anim sequence
    - auto field:
        - asset name: current select
        - start, end: current timeline
        - anim layer: current active anim layer

## [2.0.3] - 2024-6-18
### Bug:

- Popup dialog after each exporting anim seq item
### Update:

- Import asset to Unreal:
    - Update asset template to get skeleton and import path
    - Support get skeleton, import path for specific asset (asset_mapping)

## [2.0.2] - 2024-6-1
### Add:

- Add Export Group "Upper, Lower, All", support for exporting fbx
    - Upper/Lower :
        - auto add the suffix "UP,LW" to file_name after exporting (not affect custom export path)
- Support copy exportingGroup from old meta to new one

## [2.0.1] - 2024-5-24
### Bug:

- Bug fix and optimize
- Convert old metanode => show warning if anim layer not exist

### Update:

- Color selection behavior
    - Click: Only selected anim seqs that belong to that color
    - Shift + click: multi-select anim sequence
- Support multi-select for:
    - Set start, end frame by maya timeline
    - Apply selected object to "Asset Name" column
- Support edit custom export path on text field

### Add

- Set start, end frame by maya timeline
- Add some preset color
- Auto generated color button
    - Click: select
    - Shift + click: deselect

## [2.0.0] - 2024-4-26
### Update:

- Re-defined UI
- Duplicate, Copy, Paste
    - Support multi-selected anim sequence
    - Among containers
    - Re-define paste function(create a new item instead of modifying on selected item)
- Support convert old anim seq item node to new
- Optimize and refactor code

### Add:

- Support Shortcut
- Auto generated color button
    - Click: select
    - Shift + click: deselect
- Support edit custom export path for anim sequence item

## [1.0.5] - 2024-4-04

### Bug:

- Convert old metanode
- Can't Export Fbx -> Force Load the plugin maya.mll

### Update:

- Hide Export Options
- Optimized UI:
    - Slow down scroll
    - Set focus whenever container is moved

### Add:

- Support add prefix/suffix
- Support duplicate anim sequence

## [1.0.4] - 2024-3-09

### Bug:

- Store column order and size settings
- Deleting an anim sequence does not remove it from the list visually
- Export Fbx

### Add

- P4, Unreal indicator
- The check box on the container to turn on or off anim sequence items
- Store change column orde, sort in maya scenes
- apply “anim layer” by middle-click
- Select metanode in maya in right-click menu
- “list root joins” and add to “Asset Name” combobox is triggered by double-click

### Updates:

- Support Resize name , asset_name column
- Be able to paste color with multiple anim sequence selected

## [1.0.3] - 2024-2-07

### HotFix:

- Sort Order setting issue

### Bug:

- Ares importer the start and end frame do not come in the same.

### Added:

- Able to reorder the columns
    - save column order settings
- Resize columns
- Support multi-select (Set color, delete)

## [1.0.2] - 2023-12-10

### Added:

- Add Perforce Plugin

### Next:

- Clean up and optimize code , consistency flow between Controller-View
- Export fbx in background
- Copy, Paste anim sequence, color among containers
- Re-implement Container using Model-View instead of ListWidgetItem

## [1.0.1] - 2023-12-10

### Added:

- Support reload tool when artist open new scene
- Support convert old metanode format to new metanode format
- Remove namespace using fbx_sdk
- Optimized and fix some logical bug

### Changed:

- Re-implement new Metanode format

### Next:

- Clean up and optimize code , consistency flow between Controller-View
- Export fbx in background
- Copy, Paste anim sequence, color among containers
- Re-implement Container using Model-View instead of ListWidgetItem

## [1.0.0] - 2023-11-08``

### Added:

- Container:
    - Create, Rename, Delete
    - Check all, uncheck all , up and down one row
- Anim Sequence Item:
    - Create, Copy, Paste, Delete
    - Color:``
        - Set, Reset, Copy, Paste
    - Add selected object (auto select object hierarchy when exporting)
    - Anim layer
        - Set Active Layer ( current non-muted anim layer)
        - Keep updating when deleting or rename anim layer
    - Auto apply start, end or active layer when select anim sequence
    - Link selected anim sequence item to Anim Sequence Info, Export Fields
- Anim Sequence Info:
    - Support collapsed
    - Edit current selected anim sequence item
- Export:
    - Progress bar for exporting status
- Import to Unreal remotely
- Storing Settings:
    - Sorting Order in containers
    - Position, Size
    - Auto apply start frame end frame, active layer , import to unreal
    - Anim Sequence Info status (collapsed or not)

### Todo:

- Clean up and optimize code
- Export fbx in background
- Copy, Paste anim sequence, color among containers