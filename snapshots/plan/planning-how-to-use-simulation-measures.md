---
title: "Use simulation measures in a planning sheet"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-use-simulation-measures](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-use-simulation-measures) · Last updated on **2026-08-03**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Use simulation measures in a planning sheet

Summarize this article for me

Simulation measures let you model projected values without modifying the original data. Use simulations to evaluate planning scenarios, compare projected and actual values, and analyze the impact of changes before committing them.

## Create a simulation measure

1. Open the planning sheet.
2. On the **Planning** ribbon, select **Simulate**.

   [![Screenshot of the Simulate command on the Planning ribbon.](media/planning-how-to-use-simulation-measures/simulate-command.png)](media/planning-how-to-use-simulation-measures/simulate-command.png#lightbox)
3. Configure the simulation in the **Simulation** pane.

   [![Screenshot of the Simulation pane used to create a simulation measure.](media/planning-how-to-use-simulation-measures/simulation-pane.png)](media/planning-how-to-use-simulation-measures/simulation-pane.png#lightbox)

   Configure the simulation by using the following options.

   | Option | Description |
   | --- | --- |
   | **Title** | Specifies the display name of the simulation measure. |
   | **Insert as** | Creates either a **Visual Measure** or **Visual Column**. |
   | **Simulation based on** | Selects the measure to simulate. |
   | **Variance formatting style** | Defines how favorable and unfavorable variances are displayed. |
   | **Show slider** | Displays an interactive slider for editing simulation values. |
   | **Value range** | Specifies the allowed simulation range. The default is **Â±100%**. |
   | **Simulation value** | Controls whether the percentage indicator is displayed to the left or right of the simulated value. |
   | **Allow input** | Specifies whether users can edit simulated values in read mode, edit mode, or both. |
   | **Description** | Adds an optional description for the simulation measure. |
4. Select **Create**.

   [![Screenshot of a planning sheet with a newly created simulation measure.](media/planning-how-to-use-simulation-measures/simulation-measure-created.png)](media/planning-how-to-use-simulation-measures/simulation-measure-created.png#lightbox)

## Adjust values by using the simulation slider

1. Select a simulated cell to display the slider.

   [![Screenshot of a simulation slider displayed for a simulated value.](media/planning-how-to-use-simulation-measures/simulation-slider.png)](media/planning-how-to-use-simulation-measures/simulation-slider.png#lightbox)
2. Drag the slider to increase or decrease the value. The percentage change appears while you drag, and the planning sheet recalculates totals when you release the slider.
3. If you simulate a parent value, the same percentage applies to all eligible child members.

   [![Screenshot showing a parent-level simulation applied to child values.](media/planning-how-to-use-simulation-measures/parent-value-simulation.png)](media/planning-how-to-use-simulation-measures/parent-value-simulation.png#lightbox)
4. To simulate multiple values, select multiple cells by using **Ctrl** or **Shift**, and then adjust the slider on any selected cell.

   [![Screenshot showing multiple selected cells being simulated together.](media/planning-how-to-use-simulation-measures/multiple-cell-simulation.png)](media/planning-how-to-use-simulation-measures/multiple-cell-simulation.png#lightbox)

## Edit a simulation

1. Select the **Edit** icon on the slider.

   [![Screenshot showing the Edit option on the simulation slider.](media/planning-how-to-use-simulation-measures/edit-simulation-button.png)](media/planning-how-to-use-simulation-measures/edit-simulation-button.png#lightbox)
2. Enter the required percentage and select **Apply**.

   [![Screenshot of the Simulation percentage dialog.](media/planning-how-to-use-simulation-measures/edit-simulation-dialog.png)](media/planning-how-to-use-simulation-measures/edit-simulation-dialog.png#lightbox)
3. The simulation updates immediately.

   [![Screenshot showing an updated simulated value.](media/planning-how-to-use-simulation-measures/updated-simulation-value.png)](media/planning-how-to-use-simulation-measures/updated-simulation-value.png#lightbox)

## Lock or unlock a simulation

1. Select the **Lock** icon to lock the simulated cell. Locked cells aren't updated when parent-level simulations are applied.

   [![Screenshot showing the Lock option on the simulation slider.](media/planning-how-to-use-simulation-measures/lock-simulation-cell.png)](media/planning-how-to-use-simulation-measures/lock-simulation-cell.png#lightbox)
2. Locked cells are dimmed and aren't updated by parent simulations.

   [![Screenshot showing a locked simulation cell.](media/planning-how-to-use-simulation-measures/locked-simulation-cell.png)](media/planning-how-to-use-simulation-measures/locked-simulation-cell.png#lightbox)
3. Select the lock icon again to unlock the cell.

   [![Screenshot showing the Unlock option on the simulation slider.](media/planning-how-to-use-simulation-measures/unlock-simulation-cell.png)](media/planning-how-to-use-simulation-measures/unlock-simulation-cell.png#lightbox)

## Delete a simulation

1. Select the **Delete** icon to remove the simulation from the selected cell or cells.

   [![Screenshot showing the Delete option on the simulation slider.](media/planning-how-to-use-simulation-measures/delete-simulation.png)](media/planning-how-to-use-simulation-measures/delete-simulation.png#lightbox)

   Note

   You can edit, lock, or delete multiple simulations by selecting multiple cells with **Ctrl** or **Shift**.
2. When the simulation slider isn't displayed, double-click a simulated cell, and enter the required value or formula directly.

   [![Screenshot showing direct editing of a simulated value.](media/planning-how-to-use-simulation-measures/direct-edit-simulation.png)](media/planning-how-to-use-simulation-measures/direct-edit-simulation.png#lightbox)

## Bulk edit simulation measures

Apply the same simulation percentage across multiple row and column members.

1. On the **Planning** ribbon, select **Bulk Edit**.

   [![Screenshot of the Bulk Edit command on the Planning ribbon.](media/planning-how-to-use-simulation-measures/bulk-edit-command.png)](media/planning-how-to-use-simulation-measures/bulk-edit-command.png#lightbox)
2. Select the simulation measure.
3. Configure filters, row level, column level, and the simulation percentage.
4. Select **Apply**.

   [![Screenshot of the Bulk Edit pane showing filters, row level, column level, and simulation options.](media/planning-how-to-use-simulation-measures/bulk-edit-pane.png)](media/planning-how-to-use-simulation-measures/bulk-edit-pane.png#lightbox)

   The selected members are updated using the specified simulation percentage.

   [![Screenshot showing the planning sheet after a bulk simulation is applied.](media/planning-how-to-use-simulation-measures/bulk-edit-results.png)](media/planning-how-to-use-simulation-measures/bulk-edit-results.png#lightbox)

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
