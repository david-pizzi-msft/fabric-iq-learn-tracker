---
title: "Manage columns in PowerTable sheet"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-manage-columns](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-manage-columns) · Last updated on **2026-07-07**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Manage columns in PowerTable sheet

Summarize this article for me

Use **Manage Columns** to control column visibility, width, order, input type configuration, and access permissions.

To open the **Manage Columns** panel, select **PowerTable** > **Manage Columns**.

![Screenshot of the Manage Columns option on the toolbar.](media/powertable-how-to-manage-columns/manage-columns.png)

The following options are available:

## Show or hide columns

To show or hide columns:

1. In the **Show** column, select the check box for each column to display.
2. Clear the check box for each column to hide.

   [![Screenshot of displaying or hiding the columns.](media/powertable-how-to-manage-columns/display-hide-columns.png)](media/powertable-how-to-manage-columns/display-hide-columns.png#lightbox)

To display all available columns, select the **All** check box.

![Screenshot of the All checkbox used to display all the columns.](media/powertable-how-to-manage-columns/display-all-columns.png)

Note

Hiding a column removes it from the table view but doesn't delete the column or its data.

## Edit column configuration

Use **Edit Config** to set column properties such as input types, constraints, default values, display settings, and lookups.

To edit column configuration:

1. Select **Edit Config** in the **Manage Columns** panel.

   [![Screenshot of the Edit Config option in the Manage Columns window.](media/powertable-how-to-manage-columns/edit-config.png)](media/powertable-how-to-manage-columns/edit-config.png#lightbox)
2. The **Column Configuration** window opens. Configure the column properties.

   [![Screenshot of the column configuration window.](media/powertable-how-to-manage-columns/column-configuration-window.png)](media/powertable-how-to-manage-columns/column-configuration-window.png#lightbox)

To learn about configuring columns, see **Configure columns**.

## Set column access control

Use **Column Access** to control which users can edit specific columns.

1. Select **Column Access** in the **Manage Columns** panel.

   [![Screenshot of the Column Access option in the Manage Columns window.](media/powertable-how-to-manage-columns/column-access.png)](media/powertable-how-to-manage-columns/column-access.png#lightbox)
2. The **Manage Access** window opens. Use the **Column Access** section to set write permissions for each column.

   [![Screenshot of the Column Access window.](media/powertable-how-to-manage-columns/column-access-window.png)](media/powertable-how-to-manage-columns/column-access-window.png#lightbox)

For more information about setting up column access control, see [Column access control](powertable-how-to-set-up-access-control#column-access).

## Reorder columns

Reorder columns to customize the table layout.

To reorder columns:

1. Drag a column header to the position you want in the table.
2. Alternatively, in the **Manage Columns** panel, drag the **reorder handle** (six-dot icon) next to a column and drop it in the required position.

   [![Screenshot of the reorder handle in the Manage Columns window.](media/powertable-how-to-manage-columns/reorder-columns.png)](media/powertable-how-to-manage-columns/reorder-columns.png#lightbox)

The table layout immediately reflects your changes.

Note

Reordering a column changes only its display position in the table and doesn't affect the underlying data.

## Search and filter columns

Use the search and filter options to locate specific columns, especially in large tables.

- **Search**: Find columns by their name.

  [![Screenshot of searching a column in the Manage Columns window.](media/powertable-how-to-manage-columns/search.png)](media/powertable-how-to-manage-columns/search.png#lightbox)
- **Filter**: Filter columns by **Input Type** or **Column Type**.

  [![Screenshot of filtering columns in the Manage Columns window.](media/powertable-how-to-manage-columns/filter.png)](media/powertable-how-to-manage-columns/filter.png#lightbox)

Select **Reset** to clear all filters.

## Set column widths

To set the column widths:

In the **Width** field, enter the width in pixels for each column.

[![Screenshot of adjusting the column widths.](media/powertable-how-to-manage-columns/adjust-column-width.png)](media/powertable-how-to-manage-columns/adjust-column-width.png#lightbox)

To restore the original column widths, select the **Reset** icon.

![Screenshot of resetting the column widths to its default value.](media/powertable-how-to-manage-columns/reset-column-width.png)

## Other ways to adjust column widths

Other options for adjusting column widths help you optimize the display of data, especially in tables with many columns.

You can resize columns by dragging column borders or automatically fitting them to the header or content.

### Resize columns manually

The quickest way to resize a column is to select and drag its header boundary.

To resize a column:

1. Hover over the edge of the column header.
2. Select and drag the resize handle to the required width.

   [![Screenshot of resizing the column width manually.](media/powertable-how-to-manage-columns/resize-columns-manually.png)](media/powertable-how-to-manage-columns/resize-columns-manually.png#lightbox)

### Autofit column widths

Use the **Auto Fit** options to automatically adjust column widths based on the header or content.

To access the autofit options:

1. Go to the **Format** tab.
2. Select the **Auto Fit** dropdown.

   ![Screenshot of the Auto Fit dropdown on the toolbar.](media/powertable-how-to-manage-columns/auto-fit.png)

#### Fit to header

Select **Fit to Header** to resize each column based on the width of its column header.

[![Screenshot of the table after applying the Fit to Header option.](media/powertable-how-to-manage-columns/fit-to-header.png)](media/powertable-how-to-manage-columns/fit-to-header.png#lightbox)

#### Fit to content

Select **Fit to Content** to resize each column based on the width of the data it contains.

[![Screenshot of the table after applying the Fit to Content option.](media/powertable-how-to-manage-columns/fit-to-content.png)](media/powertable-how-to-manage-columns/fit-to-content.png#lightbox)

## Lock column widths

After you configure column widths, lock them to prevent users from changing them.

To lock column widths:

1. Go to **PowerTable** > **Manage Columns**. In the **Manage Columns** window, adjust the column widths as needed.
2. Select the **Lock** icon next to the columns you want to lock. To lock all columns, select the **Lock** icon next to **All**.

When you lock column widths, all column and row resizing options become unavailable, including drag-to-resize functionality.

[![Screenshot of the lock icons in the Manage Columns window after locking.](media/powertable-how-to-manage-columns/lock.png)](media/powertable-how-to-manage-columns/lock.png#lightbox)

The options in the **Auto Fit** dropdown also become unavailable until you unlock the column widths.

![Screenshot of showing the unavailable Auto Fit options.](media/powertable-how-to-manage-columns/auto-fit-unavailable.png)

To enable resizing again, select **PowerTable** > **Manage Columns**, and then select the **Lock** icon to unlock the widths.

[![Screenshot of showing the unlock option in the Manage Columns window.](media/powertable-how-to-manage-columns/unlock.png)](media/powertable-how-to-manage-columns/unlock.png#lightbox)

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
