---
title: "Group rows in PowerTable"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-group-rows](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-group-rows) · Last updated on **2026-07-19**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Group rows in PowerTable

Summarize this article for me

Use the **Group By** feature to organize records into logical groups based on shared values. Grouping makes large datasets easier to navigate and analyze. Expand or collapse individual groups to control the level of detail in the table.

## Group rows

To group rows:

1. From the **PowerTable** tab, select **Group By**.

   [![Screenshot of the Group By option on the toolbar.](media/powertable-how-to-group-rows/group-by.png)](media/powertable-how-to-group-rows/group-by.png#lightbox)
2. From the dropdown, select the column to group the records, and then select **Save**.

   [![Screenshot of selecting a column from the dropdown.](media/powertable-how-to-group-rows/select-column.png)](media/powertable-how-to-group-rows/select-column.png#lightbox)

PowerTable groups the records based on the selected column. In the following example, PowerTable groups the records by the *ProductSubcategoryKey* column. It aggregates the numerical fields to sum.

[![Screenshot of the table with grouped records.](media/powertable-how-to-group-rows/grouped-records.png)](media/powertable-how-to-group-rows/grouped-records.png#lightbox)

## Expand or collapse groups

Select the expand or collapse arrow beside a group name to show or hide the records within that group.

[![Screenshot of the expand and collapse arrows.](media/powertable-how-to-group-rows/expand-collapse-groups.png)](media/powertable-how-to-group-rows/expand-collapse-groups.png#lightbox)

## Create subgroups

Create subgroups within a group.

1. Select **Group By** again, and then select **Add Sub Group**.

   [![Screenshot of the Add Sub Group option.](media/powertable-how-to-group-rows/add-sub-group.png)](media/powertable-how-to-group-rows/add-sub-group.png#lightbox)
2. Select another column from the dropdown, and then select **Save**.

   [![Screenshot of selecting a column for sub group.](media/powertable-how-to-group-rows/select-column-sub-group.png)](media/powertable-how-to-group-rows/select-column-sub-group.png#lightbox)

PowerTable creates nested groups within the existing group. The following example shows the records further grouped by the *ModelName* column under *ProductSubcategoryKey*.

[![Screenshot of the table with nested groups.](media/powertable-how-to-group-rows/nested-groups.png)](media/powertable-how-to-group-rows/nested-groups.png#lightbox)

## Remove grouping

To remove a group, select the delete (bin) icon next to it, and then select **Save**. To return to the default table view, remove all groups.

[![Screenshot of the delete icon to remove group.](media/powertable-how-to-group-rows/remove-group.png)](media/powertable-how-to-group-rows/remove-group.png#lightbox)

## Work with grouped data

You can continue to perform table operations on grouped records, including:

- Edit data
- Insert rows
- Bulk edit records
- Apply formatting
- Sort records
- Use Find and Replace

[![Screenshot of editing the grouped data.](media/powertable-how-to-group-rows/edit-data.png)](media/powertable-how-to-group-rows/edit-data.png#lightbox)

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
