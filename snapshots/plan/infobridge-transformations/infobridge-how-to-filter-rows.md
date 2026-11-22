---
title: "Filter rows in Infobridge"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-filter-rows](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-filter-rows) · Last updated on **2026-07-28**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Filter rows in Infobridge

Summarize this article for me

Use the **Filter Rows** transformation to keep only rows that meet specified conditions.

Filtering rows reduces the amount of data in a query and ensures that only relevant records are available for analysis and reporting.

## Filter rows

The following example filters a query to keep only rows where **Country** is **United States of America** and **Sum of COGS** is greater than **500250**.

1. On the **Transform** tab, select **Filter Rows**.

   [![Query results before applying filters. The query contains rows from multiple countries and COGS values.](../media/infobridge-transformations/infobridge-how-to-filter-rows/filter-rows-source-data.png)](../media/infobridge-transformations/infobridge-how-to-filter-rows/filter-rows-source-data.png#lightbox)

   The **Filter Rows** dialog opens.
2. Enter the following example filters. For a full list of filter options, see [Filter dialog options](#options-for-filter-dialog) later in the article.

   1. In **Column Name**, select **Country**.
   2. In **Operator**, select **Is**.
   3. In **Value**, select **United States of America**.
   4. Select **Add Filter**.
   5. Select **And**.
   6. In **Column Name**, select **Sum of COGS**.
   7. In **Operator**, select **Is greater than**.
   8. In **Value**, enter **500250**.

   [![Filter Rows dialog configured to retain rows where Country is United States of America and Sum of COGS is greater than 500250.](../media/infobridge-transformations/infobridge-how-to-filter-rows/filter-rows-configuration.png)](../media/infobridge-transformations/infobridge-how-to-filter-rows/filter-rows-configuration.png#lightbox)
3. Select **Apply**.

After you apply the filter, only rows that satisfy the specified conditions remain in the query results.

[![Query results after applying filters. Only rows that meet the Country and Sum of COGS filter conditions remain.](../media/infobridge-transformations/infobridge-how-to-filter-rows/filter-rows-results.png)](../media/infobridge-transformations/infobridge-how-to-filter-rows/filter-rows-results.png#lightbox)

The applied filter appears in **Performed Steps** and applies to subsequent transformations, calculations, and reporting scenarios.

## Options for filter dialog

The filter dialog supports the following options:

- **Condition**: Defines how to combine multiple filter conditions.
  - Use **And** when all conditions must be true.
  - Use **Or** when any condition is true.
- **Column Name**: Select the measure or dimension to filter on.
- **Operator**: Select the condition to apply.
  - For text columns, operators include **Is**, **Is not**, **In**, and **Not in**.
  - For numeric columns, operators include **Is**, **Is not**, **Less than**, **Greater than**, **Less than or equal to**, and **Greater than or equal to**.
- **Value**: Enter a value or select one from the list.
- **Add Filter**: Add more filter conditions.

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
