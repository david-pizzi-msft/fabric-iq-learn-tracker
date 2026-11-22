---
title: "Manage columns in Infobridge"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-manage-columns](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-manage-columns) · Last updated on **2026-07-28**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Manage columns in Infobridge

Summarize this article for me

Use column management actions to update column names and remove columns you don't need.

Managing columns helps improve query readability, maintain consistent business terminology, and focus analysis on the most relevant data.

## Rename columns

Use the **Rename Column** transformation to replace existing column names with names that better align with your business terminology and reporting requirements.

Renaming columns makes measures and dimensions easier to understand and can improve consistency across reports and planning sheets.

The following example shows how to rename the **Value** column from an [unpivot transformation](infobridge-how-to-pivot-column) to **Sales**.

1. On the **Transform** tab, select **Rename Column**.
2. In **Column**, select **Value**.
3. In **New Column Name**, enter **Sales**.
4. Select **Apply**.

[![Screenshot of the Rename Column dialog. The Column dropdown shows Value, and the New Column Name box contains Sales.](../media/infobridge-transformations/infobridge-how-to-manage-columns/rename-column-configuration.png)](../media/infobridge-transformations/infobridge-how-to-manage-columns/rename-column-configuration.png#lightbox)

After you apply the transformation, the column displays the updated name.

[![Screenshot of query results showing the renamed Sales column after you apply the Rename Column transformation.](../media/infobridge-transformations/infobridge-how-to-manage-columns/renamed-sales-column.png)](../media/infobridge-transformations/infobridge-how-to-manage-columns/renamed-sales-column.png#lightbox)

## Remove columns

Use the **Remove Column** transformation to remove columns that you don't need for analysis or reporting.

Removing unnecessary columns simplifies query results and reduces visual clutter.

The following example removes the **Sum of Sales** column from a query.

1. On the **Transform** tab, select **Remove Column**.
2. In **Column**, select the column to remove.
3. Select **Remove**.

[![Screenshot of the Remove Column dialog. The Column list shows Sum of Sales selected.](../media/infobridge-transformations/infobridge-how-to-manage-columns/remove-column-configuration.png)](../media/infobridge-transformations/infobridge-how-to-manage-columns/remove-column-configuration.png#lightbox)

After you remove the column, it no longer appears in the query results.

This example removes the **Sum of Sales** column.

[![Screenshot of query results showing that the Sum of Sales column no longer appears.](../media/infobridge-transformations/infobridge-how-to-manage-columns/remove-column-results.png)](../media/infobridge-transformations/infobridge-how-to-manage-columns/remove-column-results.png#lightbox)

Subsequent transformations, calculations, and reporting scenarios don't include the removed column.

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
