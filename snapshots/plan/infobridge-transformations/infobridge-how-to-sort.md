---
title: "Sort data in Infobridge"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-sort](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-sort) · Last updated on **2026-07-28**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Sort data in Infobridge

Summarize this article for me

Use the **Sort** transformation to arrange dimensions and measures in ascending or descending order.

Sorting data helps improve readability and ensures that query results appear in the order required for analysis and reporting.

## Sort data

The following example sorts the **Market & Geography** column in ascending order.

1. On the **Transform** tab, select **Sort Ascending** in the **Sort** group.

   [![Screenshot of query results before sorting. The Market & Geography column contains unsorted values.](../media/infobridge-transformations/infobridge-how-to-sort/sort-data-source.png)](../media/infobridge-transformations/infobridge-how-to-sort/sort-data-source.png#lightbox)

   The **Sort By Ascending** dialog opens.
2. In **Column Name**, select **Market & Geography**.
3. In **Order**, select **Ascending**.
4. Select **Apply**.

   [![Screenshot of the Sort By Ascending dialog configured to sort the Market & Geography column in ascending order.](../media/infobridge-transformations/infobridge-how-to-sort/sort-data-configuration.png)](../media/infobridge-transformations/infobridge-how-to-sort/sort-data-configuration.png#lightbox)

After you apply the sort, the column appears in the order you specified.

In this example, the **Market & Geography** column appears in ascending order.

[![Screenshot of query results showing the Market & Geography column in ascending order.](../media/infobridge-transformations/infobridge-how-to-sort/sort-data-results.png)](../media/infobridge-transformations/infobridge-how-to-sort/sort-data-results.png#lightbox)

The applied sort appears in **Performed Steps** and applies to subsequent transformations, calculations, and reporting scenarios.

## Sort data from the column menu

You can also sort data directly from a column menu without opening the **Sort** dialog.

1. Open the menu for the column to sort.
2. Select **Sort ascending** or **Sort descending**.

   [![Screenshot of the column menu showing the Sort ascending and Sort descending options.](../media/infobridge-transformations/infobridge-how-to-sort/sort-data-column-menu.png)](../media/infobridge-transformations/infobridge-how-to-sort/sort-data-column-menu.png#lightbox)

The column sorts immediately based on your selection.

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
