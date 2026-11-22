---
title: "Fabric planning tutorial part 1: Allocation and collaboration"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-tutorial/planning/tutorial-1-allocation-collaboration](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-tutorial/planning/tutorial-1-allocation-collaboration) · Last updated on **2026-09-04**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Fabric planning tutorial part 1: Allocation and collaboration

Summarize this article for me

In this tutorial, you build a revenue plan, set a top-down $30M target distributed by prior-year weights, then build a bottom-up sales plan with a subcategory adjustment, a trend distribution, and a segment-wide uplift.

## Prerequisites

Complete [1: Introduction to Fabric Planning](tutorial-0-introduction) before starting this tutorial.

## Set the top-down target

In this section, you set a top-down 2026 revenue target and Planning distributes it across regions, categories, and subcategories using the prior-year mix. You then lock specific quarters to control how additional target increases are distributed.

1. In the **Planning** ribbon, select **Totals** and enable **Column Grand Total** on the left. A grand total column appears showing full-year 2025 actuals. By enabling Column Sub/Grand Total, you make it straightforward to input a single value and distribute it across the row and column hierarchies.
2. In the **Planning** ribbon, select **Number** > **Copy from another series** > **2025 Gross Revenue**. Enter **2026 Target** as the title and select **Create**. The column is prepopulated with 2025 values.

   Note

   Native columns don't allow data input or value changes, so you create a copy to hold the target values. This approach also keeps the 2025 actuals separate from the 2026 plan and target.

   [![Screenshot of creating a copy of the 2025 revenue native measure into a new 2026 target measure.](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/copy-series-2025-revenue-2026-target-column.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/copy-series-2025-revenue-2026-target-column.png#lightbox)
3. Double-click the grand total cell of the *2026 Target* column, enter $28.5*m*, and select the check mark. Planning allocates the values you enter proportionally to all regions, categories, and subcategories based on the 2025 revenue mix.

   [![Screenshot of entering a value and allocating it across row and column hierarchies.](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/enter-2026-target-value-proportional-allocation.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/enter-2026-target-value-proportional-allocation.png#lightbox)
4. Expand the column hierarchy to quarters. Select the Q1 row total cell of the *2026 Target* column, select the distribution icon, and select **Lock all children**. Repeat for the Q2 row total cell. Locked cells turn grey. Locking the children prevents the next data input from distributing into Q1 and Q2.

   [![Screenshot of locking the Q1 and Q2 child cells in the 2026 Target revenue column.](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/expand-column-hierarchy-lock-children.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/expand-column-hierarchy-lock-children.png#lightbox)
5. Double-click the grand total cell of the *2026 Target* column, enter $30m, and press Enter. The extra $1.5m distributes only across Q3 and Q4, as Q1 and Q2 are locked.

   [![Screenshot of allocating values to unlocked Q3 and Q4 without affecting the Q1 and Q2 values.](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/distribute-value-unlocked-columns.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/distribute-value-unlocked-columns.png#lightbox)
6. Select the Q1 total cell, select the distribution icon, and select **Unlock all children**. Repeat for the Q2 total cell. Unlocking the children once allocation is complete ensures the next allocation or change also applies to Q1 and Q2.

   [![Screenshot of option to unlock all children for the Q1 revenue target column.](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/unlock-all-children-q1-total-cell.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/unlock-all-children-q1-total-cell.png#lightbox)

## Build a bottom-up sales plan

In this section, you build a bottom-up sales plan by adjusting individual subcategories and applying bulk edits across regions and categories. This approach complements the top-down target with granular, ground-level input.

1. In the **Planning** ribbon, select **Number** > **Copy from another series** > **2025 Gross Revenue**. Enter *2026 Sales Plan* as the title and select **Create**. The column is prepopulated with 2025 values.

   [![Screenshot of creating a 2026 sales plan by copying values from 2025 gross revenue.](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/create-2026-sales-plan-from-2025-gross-revenue.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/create-2026-sales-plan-from-2025-gross-revenue.png#lightbox)
2. In the footer, select the **Settings** icon and set rows per page to **All**. This action displays all the dimension categories on a single page with a scroll bar.
3. Hover near the *Americas* row, select the row gripper, and select **Collapse** > **Region** to collapse to region level. This action collapses the row hierarchy and displays only the regions.

   [![Screenshot of the row hierarchy collapsed to show only the region level in the planning grid.](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/collapse-hierarchy-region-level.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/collapse-hierarchy-region-level.png#lightbox)
4. Expand *Americas* > *Beverages* and locate the *Energy & Sports* row.
5. Double-click the grand total cell of the *2026 Sales Plan* column for *Energy & Sports* and append 8% to the existing value by entering "+ 8%" in the formula bar. Press Enter. The totals roll up to *Beverages* â *Americas*.

   [![Screenshot of increasing the value of the energy and sports row by 8%.](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/increase-energy-value-eight-percent.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/increase-energy-value-eight-percent.png#lightbox)
6. Select the *Energy & Sports* grand total cell, select **Distribute to column with trend**, and drag the slider to *4%*. The annual total distributes across quarters following a 4% growth trendâQ1 receives the smallest share and Q4 the largest.

   [![Screenshot of distributing the entered value across child rows and columns based on a trend value of 4%.](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/distribute-column-trend-four-percent.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/distribute-column-trend-four-percent.png#lightbox)
7. In the **Planning** ribbon, select **Bulk Edit** and configure the options as follows:

   | Setting | Value |
   | --- | --- |
   | **Measure** | 2026 Sales Plan |
   | **Region Name** | Asia Pacific, Europe |
   | **Category** | Beverages, Personal Care |
   | **Quarter Name** | Q3 |
   | **Apply to Row Level** | Subcategory |
   | **Apply to Column Level** | Month Short |
   | **Type** | Append By |
   | **Value** | 8% |

   [![Screenshot of the bulk edit configuration increasing Q3 sales plan values by 8 percent for selected regions and categories.](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/bulk-edit-configuration-increase-eight-percent.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/bulk-edit-configuration-increase-eight-percent.png#lightbox)
   |
8. Q3 values for the selected regions and categories increase by 8%.

   [![Screenshot of bulk updating the values for multiple regions, categories, and subcategories.](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/selected-region-category-bulk-update.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/selected-region-category-bulk-update.png#lightbox)

## Add collaboration columns

In this section, you add comments and a status column to the sales plan. These collaboration features let planners document assumptions and track review progress directly in the sheet.

1. Select and right-click the grand total cell of the *2026 Sales Plan* column for *Energy & Sports* under *Americas* â *Beverages*. Select **Add Comment**, enter â*8% uplift agreed with the Americas sales lead. Annual total distributed across quarters with a 4% growth trendâ. S*elect **Post**.

   [![Screenshot of adding a cell-level comment in a planning sheet.](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/add-cell-level-comment.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/add-cell-level-comment.png#lightbox)
2. In the **Planning** ribbon, select **Comments** > **Settings**. Enable **Comments Column** and select **Save**. A comments column appears in the grid.

   [![Screenshot of adding a comments column to a planning sheet.](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/add-comments-column.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/add-comments-column.png#lightbox)
3. Double-click the comments cell for the *Americas row*. Enter â*Sales Plan reviewed and ready for submissionâ*, type *@* to tag a team member, and select **Post**.

   [![Screenshot of entering a comment in the comments column and tagging a user.](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/tag-user-post-comment-comments-column.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/tag-user-post-comment-comments-column.png#lightbox)
4. Collapse the column hierarchy. In the **Planning** ribbon, select **List** > **Single Select** to add a dropdown field.
5. Enter *Status* as the title, select **Options** > **Preset**, and select **Process Status**. Select **Apply**, then **Create**. The *Status* column appears in the grid.
6. Set the *Status* cell for the *Americas* row to *In Progress*.

   [![Screenshot of setting the process status to In Progress for the Americas row. ](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/set-process-status-progress.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/set-process-status-progress.png#lightbox)

## Set up an approval workflow

In this section, you configure a two-level approval workflow and verify it by submitting a change for review.

1. In the **Model** ribbon, select **Approval**.
2. In the approval workflow configuration, select the edit icon next to Level 1. Rename to *Regional Manager.* Select the first-level approver.
3. Select the edit icon next to Level 2. Rename to *Finance Director* and select the second-level approver. Select **Next**.

   [![Screenshot of assigning the first-level and second-level approver.](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/approval-workflow-configuration-select-approvers.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/approval-workflow-configuration-select-approvers.png#lightbox)
4. In approval workflow settings, enable **Reset on Rejection** and **Teams Notifications**. Select **Submit**.

   [![Screenshot of reset and teams notification options. ](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/approval-workflow-reject-teams-settings.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/approval-workflow-reject-teams-settings.png#lightbox)
5. The *Regional Manager* and *Finance Director* columns appear in the sheet.

   [![Screenshot of the manager and director approval status columns added to the planning sheet.](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/approval-columns-added-manager-director.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/approval-columns-added-manager-director.png#lightbox)
6. Expand *Asia Pacific* and double-click the Beverages cell in the *2026 Sales Plan* grand total column, then append 10% by entering "+10%" in the formula bar. Press **Enter**.
7. In the *Regional Manager* column for the *Asia Pacific* â *Beverages* row, select **Submitted** from the dropdown. The *Finance Director* column automatically updates to **Pending**, confirming the submission has been routed for approval.

   [![Screenshot of setting the status to submitted for the manager column. The status for the director column automatically changes to pending.](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/select-submitted-status.png)](../../media/planning-tutorial/planning/tutorial-1-allocation-collaboration/select-submitted-status.png#lightbox)

## Next steps

Create data input fields, create a calculated measure, and use the Optimizer to achieve a target value in the next tutorial, [Optimize data input measures](tutorial-2-optimizer)

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
