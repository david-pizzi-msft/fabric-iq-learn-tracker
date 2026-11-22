---
title: "Use dimension level in Infobridge"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-how-to-use-dimension-level](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-how-to-use-dimension-level) · Last updated on **2026-08-19**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Use dimension level in Infobridge

Summarize this article for me

The dimension level is a list of dimensions that are part of the report. When you select a particular dimension from the dimension level list, Infobridge displays it as a measure in a query. In simple terms, any row category you select under the Dimension level list converts to a measure in Infobridge.

Use **Dimension level** in a row model to control which dimension items appear as measures in an Infobridge query. For example, when you select `ProductName` as the dimension level, the ProductName items are available as measures when you create an Infobridge query. The existing measures, such as Units, Unit Price, and Revenue, then appear as rows in the query.

When you change **Dimension level** back to `None`, the existing query no longer has a dimension level to determine which items to use as measures. Edit the query source and select the required measures to restore the query.

## Set a dimension level

1. In the report, go to **Model** and select **Row Model**.

   [![Screenshot of the Model tab with Row Model selected.](media/planning-infobridge-dimension-level/select-row-model.png)](media/planning-infobridge-dimension-level/select-row-model.png#lightbox)
2. In the **Model Builder** pop-up, select **Enable**.

   [![Screenshot of the Model Builder prompt with Enable selected.](media/planning-infobridge-dimension-level/enable-model-builder.png)](media/planning-infobridge-dimension-level/enable-model-builder.png#lightbox)
3. In the **Row Model** screen, select the dimension you want under the **Dimension Level** list.

   This setting uses the ProductName dimension in an Infobridge query.

   [![Screenshot of the Dimension Level menu with ProductName selected.](media/planning-infobridge-dimension-level/select-productname-dimension-level.png)](media/planning-infobridge-dimension-level/select-productname-dimension-level.png#lightbox)
4. Save the report.
5. Go to **Infobridge** and select **Create Query**.

   [![Screenshot of the Infobridge Create Query window showing the available measures.](media/planning-infobridge-dimension-level/create-infobridge-query.png)](media/planning-infobridge-dimension-level/create-infobridge-query.png#lightbox)
6. Create the query.

   Since `ProductName` is selected as the dimension level in the row model, the ProductName items are used as measures in the query. The original measures, such as Units, Unit Price, and Revenue, are displayed as rows.

   [![Screenshot of an Infobridge query showing ProductName items as measures and Units, Unit Price, and Revenue as rows.](media/planning-infobridge-dimension-level/dimension-level-query-results.png)](media/planning-infobridge-dimension-level/dimension-level-query-results.png#lightbox)

## Reset the dimension level

To reset the report to the original state, follow these steps:

1. In the report, go to **Model** and open **Row Model**.
2. Select **Dimension Level**, and then select `None`.

   [![Screenshot of the Dimension Level menu with None selected.](media/planning-infobridge-dimension-level/reset-dimension-level.png)](media/planning-infobridge-dimension-level/reset-dimension-level.png#lightbox)
3. Save the report and return to **Infobridge**.

   When you set the dimension level to `None`, the query no longer has a dimension level to determine which measures to display.
4. In **Manage Queries**, select the pencil icon for the query to edit its source.

   [![Screenshot of Manage Queries with the edit icon for an Infobridge query.](media/planning-infobridge-dimension-level/edit-infobridge-query-source.png)](media/planning-infobridge-dimension-level/edit-infobridge-query-source.png#lightbox)
5. In **Manage Source**, select the measures that you want the query to display, such as `Units`, `Unit Price`, and `Revenue`, and then select **Update**.

   [![Screenshot of Manage Source with Units, Unit Price, and Revenue selected.](media/planning-infobridge-dimension-level/select-query-measures.png)](media/planning-infobridge-dimension-level/select-query-measures.png#lightbox)
6. Verify the query.

   The query is restored to its previous measure-based layout, with Units, Unit Price, and Revenue available as measures.

   [![Screenshot of the Infobridge query restored to its original measure-based layout.](media/planning-infobridge-dimension-level/query-restored.png)](media/planning-infobridge-dimension-level/query-restored.png#lightbox)

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
