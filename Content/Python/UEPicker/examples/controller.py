#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict, List


class AppController:
    """
    Controller class for the Control Rig Selector application.
    Handles communication between the model and view components.
    """

    def __init__(self, model, view):
        """
        Initialize the controller with model and view instances.

        Args:
            model: The ControlRigModel instance
            view: The MainWindow instance
        """
        self.model = model
        self.view = view

        # Connect view signals to controller methods
        self._connect_signals()

        # Initialize the UI with data from the model
        self._initialize_ui()

    def _connect_signals(self):
        """Connect view signals to controller methods"""
        # View -> Controller connections
        self.view.rig_selected.connect(self._handle_rig_selection)
        self.view.control_selected.connect(self._handle_control_selection)
        self.view.control_deselected.connect(self._handle_control_deselection)
        self.view.search_requested.connect(self._handle_search)
        self.view.refresh_requested.connect(self._handle_refresh)

        # Model -> Controller connections
        self.model.rigs_changed.connect(self._on_rigs_changed)
        self.model.controls_changed.connect(self._on_controls_changed)
        self.model.selection_changed.connect(self._on_selection_changed)

    def _initialize_ui(self):
        """Initialize the UI with data from the model"""
        # Populate rig dropdown
        rigs = self.model.get_available_rigs()
        self.view.update_rig_list(rigs)

        # Set default status message
        self.view.set_status_message("Ready")

    def _handle_rig_selection(self, rig_name):
        """
        Handle rig selection from the view.

        Args:
            rig_name (str): Name of the selected rig
        """
        if rig_name:
            success = self.model.set_current_rig(rig_name)
            if success:
                self.view.set_status_message(f"Rig '{rig_name}' selected")
            else:
                self.view.set_status_message(f"Failed to select rig '{rig_name}'")

    def _handle_control_selection(self, control_name, exclusive):
        """
        Handle control selection from the view.

        Args:
            control_name (str): Name of the control to select
            exclusive (bool): Whether to make this an exclusive selection (deselect others)
        """
        success = self.model.select_control(control_name, exclusive)
        if success:
            message = f"Selected control '{control_name}'"
            self.view.set_status_message(message)
        else:
            self.view.set_status_message(f"Failed to select control '{control_name}'")

    def _handle_control_deselection(self, control_name):
        """
        Handle control deselection from the view.

        Args:
            control_name (str): Name of the control to deselect, or "*" to clear all
        """
        if control_name == "*":
            # Clear all selections
            self.model.clear_selection()
            self.view.set_status_message("Cleared all selections")
        else:
            # Deselect specific control
            success = self.model.deselect_control(control_name)
            if success:
                self.view.set_status_message(f"Deselected control '{control_name}'")
            else:
                self.view.set_status_message(f"Failed to deselect control '{control_name}'")

    def _handle_search(self, search_text):
        """
        Handle search requests from the view.

        Args:
            search_text (str): Search text entered by the user
        """
        if not search_text:
            # If search is empty, show all controls
            self._on_controls_changed(self.model.get_current_rig())
            return

        # Get current rig controls
        all_controls = self.model.get_controls_in_rig()

        # Filter controls by search text
        filtered_controls = [
            control for control in all_controls
            if search_text.lower() in control["name"].lower()
        ]

        # Update the view with filtered controls
        self.view.update_controls_tree(filtered_controls)
        self.view.set_status_message(f"Found {len(filtered_controls)} controls matching '{search_text}'")

    def _handle_refresh(self):
        """Handle refresh requests from the view"""
        # In a real implementation, this would refresh data from UE
        self.view.set_status_message("Refreshing data...")

        # For now, just update the UI with current model data
        self._on_rigs_changed()
        current_rig = self.model.get_current_rig()
        if current_rig:
            self._on_controls_changed(current_rig)

        self.view.set_status_message("Data refreshed")

    def _on_rigs_changed(self):
        """Handle changes to the available rigs in the model"""
        rigs = self.model.get_available_rigs()
        self.view.update_rig_list(rigs)

    def _on_controls_changed(self, rig_name):
        """
        Handle changes to the controls in the model.

        Args:
            rig_name (str): Name of the rig whose controls changed
        """
        controls = self.model.get_controls_in_rig(rig_name)
        self.view.update_controls_tree(controls)

        # Also update the selection view to match current rig
        self._update_selection_tree()

    def _on_selection_changed(self, selected_controls):
        """
        Handle changes to the selection in the model.

        Args:
            selected_controls (List[str]): List of selected control names
        """
        self._update_selection_tree()

    def _update_selection_tree(self):
        """Update the selection tree view with current selection data"""
        # Get selected controls
        selected_controls = self.model.get_selected_controls()

        # Create a dictionary mapping control names to their info
        controls_info = {}
        current_rig = self.model.get_current_rig()

        if current_rig:
            all_controls = self.model.get_controls_in_rig(current_rig)
            for control in all_controls:
                controls_info[control["name"]] = control

        # Update the view
        self.view.update_selection_tree(selected_controls, controls_info)