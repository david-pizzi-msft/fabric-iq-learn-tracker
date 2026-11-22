---
title: "Explore, organize, and summarize data in PowerTable"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-explore-organize-data](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-explore-organize-data) · Last updated on **2026-08-07**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Explore, organize, and summarize data in PowerTable

Summarize this article for me

PowerTable provides several options to help you search, organize, analyze, and clean up data in a table.

This article explains how to organize and analyze data in PowerTable. You learn how to search and sort records, reorder, show or hide, and pin columns, view column insights and column profiles, and clean up data.

## Search records

Use the **Search** box to quickly locate records by entering text, numbers, or phrases.

To search for records:

1. Select the **Search** box on the toolbar.

   [![Screenshot of the search box on the toolbar.](media/powertable-how-to-explore-organize-data/search-box.png)](media/powertable-how-to-explore-organize-data/search-box.png#lightbox)
2. Enter the text, number, or phrase that you want to find.

PowerTable sheet filters the table and shows matching records as you type. It returns search results across all pages of the table.

[![Screenshot of the table with search results.](media/powertable-how-to-explore-organize-data/search-results.png)](media/powertable-how-to-explore-organize-data/search-results.png#lightbox)

## Sort records

PowerTable provides standard sorting options to organize records in ascending or descending order based on the values in a selected column. You can sort numeric and non-numeric columns, including numbers, text, dates, and single-select fields.

To sort records:

1. Hover over the required column header and select the three-dot menu.

   ![Screenshot of the three dot menu in the column header.](media/powertable-how-to-explore-organize-data/three-dot-menu.png)
2. Select **Sort Ascending** or **Sort Descending**.

   [![Screenshot of the sort options.](media/powertable-how-to-explore-organize-data/sort-asc-des.png)](media/powertable-how-to-explore-organize-data/sort-asc-des.png#lightbox)

The following example shows the *ProductSKU* column sorted in ascending order.

[![Screenshot of the table with a column sorted in ascending order.](media/powertable-how-to-explore-organize-data/sorted-column.png)](media/powertable-how-to-explore-organize-data/sorted-column.png#lightbox)

To remove sorting, select **Remove Sort** from the same menu.

![Screenshot of the Remove Sort option.](media/powertable-how-to-explore-organize-data/remove-sort.png)

You can also use the **Sort By** option at the top, to sort records in ascending or descending order.

1. Select **Sort By**.
2. Select the column to sort by.
3. Select **ASC** or **DESC** to sort the records in ascending or descending order.
4. Optionally, select **Add Sort** to sort by additional columns.
5. Specify the sort order for each additional column.

   [![Screenshot of the Sort by Columns dialog with SubcategoryName set to ASC and ProductSKU set to DESC, with Add Sort and Save highlighted.](media/powertable-how-to-explore-organize-data/sort-by-column.png)](media/powertable-how-to-explore-organize-data/sort-by-column.png#lightbox)
6. Drag the reorder handle to change the priority of the sort columns.
7. Select **Save** to apply the sort.

## Reorder columns

Reorder columns to customize the table layout.

To move a column, drag the column header and drop it where you want.

In the following example, the *ProductSKU* column appears next to the *ProductName* column.

[![Screenshot of reordering the columns.](media/powertable-how-to-explore-organize-data/reorder-columns.png)](media/powertable-how-to-explore-organize-data/reorder-columns.png#lightbox)

## Show or hide columns

Hide columns that you don't need for your view and show them again when needed.

To hide a column:

1. Hover over the column header.
2. Select the three-dot menu and then select **Hide**.

   ![Screenshot of the Hide option.](media/powertable-how-to-explore-organize-data/hide.png)

The table view no longer shows the *ProductDescription* column.

[![Screenshot of the table after hiding a column.](media/powertable-how-to-explore-organize-data/hidden-column.png)](media/powertable-how-to-explore-organize-data/hidden-column.png#lightbox)

To show all hidden columns, select **Show All Columns** from the menu on any column header.

![Screenshot of the Show All Columns option.](media/powertable-how-to-explore-organize-data/show-all-columns.png)

## Pin columns

Pinning keeps important columns visible on the left while you scroll horizontally through the table.

To pin a column:

1. Hover over the column header.
2. Select the three-dot menu, and then select **Pin**.

   ![Screenshot of the Pin option.](media/powertable-how-to-explore-organize-data/pin.png)

The pinned *ProductName* column moves to the left side of the table and stays visible during horizontal scrolling.

[![Screenshot of the table with a pinned column.](media/powertable-how-to-explore-organize-data/pinned-column.png)](media/powertable-how-to-explore-organize-data/pinned-column.png#lightbox)

Pin multiple columns if needed.

To remove a pinned column, select **Unpin** from the same menu. To remove all pinned columns, select **Unpin All**.

[![Screenshot of the Un-pin and Un-pin All options.](media/powertable-how-to-explore-organize-data/un-pin.png)](media/powertable-how-to-explore-organize-data/un-pin.png#lightbox)

## View column insights

Use **Insights** to view summary statistics and key information about a column. Column insights help you understand data distribution, completeness, and trends without creating extra calculations.

To view column insights:

1. Hover over the column header.
2. Select the three-dot menu, and then select **Insights**.

   [![Screenshot of the available options in Insights.](media/powertable-how-to-explore-organize-data/insights.png)](media/powertable-how-to-explore-organize-data/insights.png#lightbox)

Depending on the column data type, you see the following insights:

- Sum
- Average
- Median
- Minimum value
- Maximum value
- Range
- Standard deviation
- Number and percentage of empty values
- Number and percentage of populated values
- Number and percentage of unique values
- Earliest date
- Latest date
- Date range

Use these insights to identify patterns, validate data quality, and make informed decisions. The following example shows column insights for a few columns.

[![Screenshot of the table with insights enabled for few columns.](media/powertable-how-to-explore-organize-data/enabled-insights.png)](media/powertable-how-to-explore-organize-data/enabled-insights.png#lightbox)

To view all available insights for the selected column, select **Show All** in the **Insights** dropdown.

[![Screenshot of the Insights window after selecting Show All.](media/powertable-how-to-explore-organize-data/all-insights.png)](media/powertable-how-to-explore-organize-data/all-insights.png#lightbox)

The toolbar also provides the **Sort**, **Hide**, **Pin**, and **Insights** options after you select a column.

[![Screenshot of the sort, hide, pin and insights options on the toolbar.](media/powertable-how-to-explore-organize-data/toolbar-options.png)](media/powertable-how-to-explore-organize-data/toolbar-options.png#lightbox)

## View column profile

The **Column Profile** option provides a quick summary of the data in each column. It shows the number of **Filled**, **Empty**, **Unique**, and **Distinct** values, so you can assess data completeness and identify potential data quality issues.

To view the column profile:

1. Select **Format** > **Column Profile** on the toolbar.

   ![Screenshot of PowerTable Format tab with Column Profile option highlighted on the toolbar.](media/powertable-how-to-explore-organize-data/column-profile.png)
2. PowerTable shows a profile row below the column headers. The profile includes:

   - **Filled** and **Empty** values, as both a count and a percentage.
   - **Unique** and **Distinct** values, as counts.

   [![Screenshot of PowerTable sheet showing the column profile row with Filled, Empty, Unique, and Distinct value counts below column headers.](media/powertable-how-to-explore-organize-data/display-column-profile-row.png)](media/powertable-how-to-explore-organize-data/display-column-profile-row.png#lightbox)
3. To hide the column profile and return to the default view, select **Column Profile** again.

## Clean up data

The **Data Cleanup** option improves data quality by removing duplicate and empty values from a selected column.

To clean up data:

1. Hover over the required column header, and then select the **three-dot** menu.
2. Select **Data Cleanup**.
3. Select one of the following options:

   - **Remove Duplicates**: Removes duplicate values from the selected column.
   - **Remove Empty**: Removes rows that contain empty values in the selected column.

   [![Screenshot of column header three-dot menu with Data Cleanup showing Remove Duplicates and Remove Empty options.](media/powertable-how-to-explore-organize-data/clean-up-data.jpg)](media/powertable-how-to-explore-organize-data/clean-up-data.jpg#lightbox)

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
