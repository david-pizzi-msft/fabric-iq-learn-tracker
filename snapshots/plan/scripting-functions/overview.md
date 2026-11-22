---
title: "Scripting functions"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/overview](https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/overview) · Last updated on **2026-11-18**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Scripting functions

Summarize this article for me

Scripting functions let you configure and automate custom actions in planning. You can run these actions during initial load, when data changes, or when a user selects a button or toggle.

Use scripting functions while configuring action parameters to define the actions you want to execute in response to the events.

Some scripting functions operate at the ROOT level, while others operate at the planning sheet level. The function reference pages describe the scope and configuration steps for each function.

## Available scripting functions

The following table lists the scripting functions available in planning in Fabric.

| Function | Description |
| --- | --- |
| [HIDE\_VISUAL](hide-visual) | Hides a visual or visual group in an intelligence sheet. |
| [OPEN\_LINK](open-link) | Opens a specified URL from a planning sheet. |
| [OPEN\_SHEET](open-sheet) | Opens a specified sheet in a planning sheet. |
| [REFRESH\_REPORT](refresh-report) | Refreshes a report in a planning sheet. |
| [REFRESH\_VISUAL](refresh-visual) | Refreshes a specific visual in an intelligence sheet. |
| [SETBOTTOMN](setbottomn) | Displays the bottom N records based on a selected category and ranking criterion. |
| [SETFILTER](setfilter) | Applies a saved filter to a planning sheet. |
| [SETLAYOUT](setlayout) | Applies a layout to a planning sheet, including Hierarchy, Table, Tree, default, measures-on-rows, and measures-on-columns layouts. |
| [SETNUMBERFORMATTING](setnumberformatting) | Switches the number formatting applied to values in a planning sheet between Native, Uniform, Measure Level, and Auto modes. |
| [SETSCALING](setscaling) | Scales measure values in a planning sheet to a specified unit, such as thousands or millions. |
| [SETTOPBOTTOMN](settopbottomn) | Displays the top and bottom items in a category based on a specified count or percentage. |
| [SETTOPN](settopn) | Displays the top N records based on a selected category and ranking criterion. |
| [SETVISIBILITY](setvisibility) | Shows or hides rows, columns, and measures in a planning sheet. |
| [SHOW\_MESSAGE](show-message) | Displays a custom message to users as a toast notification. |
| [SHOW\_VISUAL](show-visual) | Shows a visual or visual group in an intelligence sheet. |
| [SHOWCLOSEDFORECAST](showclosedforecast) | Shows or hides forecast values for closed periods in a planning sheet. |
| [SHOWMEASURES](showmeasures) | Shows or hides all measures in a planning sheet. |
| [TRIGGERWRITEBACK](triggerwriteback) | Executes a configured Writeback operation from a button in a planning sheet. |

## Use scripting functions

You can use scripting functions in parameter actions to control the behavior of planning sheets and intelligence sheets. For example, configure a toggle parameter to show or hide measures, display a visual, or change the layout when a user changes the parameter state.

For details about the syntax, parameters, and configuration steps, see the individual function reference pages.

---

## Feedback

Was this page helpful?

Yes

No

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

Ask Learn

Ask Learn

 Suggest a fix?

---

## Additional resources
