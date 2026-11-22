---
title: "Merge queries in Infobridge"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transform-queries/how-to-merge-query](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transform-queries/how-to-merge-query) · Last updated on **2026-07-27**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Merge queries in Infobridge

Summarize this article for me

Use **Merge Query** to combine measures from multiple queries into a single query.

**Merge Query** simplifies reporting by combining related measures while preserving the existing row and column dimensions.

Important

**Merge Query** works only when all selected queries use the same row and column dimensions. The queries can contain different measures.

**Merge Query** creates a new query. It doesn't modify the original queries.

## Example scenario

The following example uses two product-based queries.

Both queries use the same ProductName and Category dimensions but contain different measures.

The **Product Sales query** contains sales measures.

| ProductName | Category | Units | Sales Amount |
| --- | --- | --- | --- |
| Camera M300 | Cameras and camcorders | 415 | 78.28K |
| Camera M200 | Cameras and camcorders | 362 | 68.06K |
| Camera X300 | Cameras and camcorders | 381 | 71.25K |

The **Product Pricing query** contains pricing measures.

| ProductName | Category | Unit Price | Unit Cost |
| --- | --- | --- | --- |
| Camera M300 | Cameras and camcorders | 27.52K | 12.66K |
| Camera M200 | Cameras and camcorders | 22.56K | 10.37K |
| Camera X300 | Cameras and camcorders | 23.18K | 10.66K |

After you merge the queries, the new query contains the shared dimensions with measures from both queries.

| ProductName | Category | Units | Sales Amount | Unit Price | Unit Cost |
| --- | --- | --- | --- | --- | --- |
| Camera M300 | Cameras and camcorders | 415 | 78.28K | 27.52K | 12.66K |
| Camera M200 | Cameras and camcorders | 362 | 68.06K | 22.56K | 10.37K |
| Camera X300 | Cameras and camcorders | 381 | 71.25K | 23.18K | 10.66K |

## Merge queries

This example merges the **Product Sales query** and **Product Pricing query**.

The **Product Sales query** contains the shared dimensions **ProductName** and **Category**, together with the **Units** and **Sales Amount** measures.

[![Screenshot of the Product Sales query showing ProductName, Category, Units, and Sales Amount.](../media/infobridge-transform-queries/how-to-merge-query/product-sales-query.png)](../media/infobridge-transform-queries/how-to-merge-query/product-sales-query.png#lightbox)

The **Product Pricing query** uses the same dimensions and contains the **Unit Price** and **Unit Cost** measures.

[![Screenshot of the Product Pricing query showing ProductName, Category, Unit Price, and Unit Cost.](../media/infobridge-transform-queries/how-to-merge-query/product-pricing-query.png)](../media/infobridge-transform-queries/how-to-merge-query/product-pricing-query.png#lightbox)

To merge queries:

1. On the **Home** ribbon, select **Merge Query**.
2. In the **Merge Query** dialog, add the queries that you want to merge.
3. For the **Product Sales query**, select the measures to include in the merged query.

   In this example, select:

   - **Sum of Units**
   - **Sum of Sales Amount**

   [![Screenshot of the Merge Query dialog showing the Product Sales query with the Sum of Units and Sum of Sales Amount measures selected.](../media/infobridge-transform-queries/how-to-merge-query/merge-query-select-first-query.png)](../media/infobridge-transform-queries/how-to-merge-query/merge-query-select-first-query.png#lightbox)
4. For the **Product Pricing query**, select the measures to include in the merged query.

   In this example, select:

   - **Sum of Unit Price**
   - **Sum of Unit Cost**

   [![Screenshot of the Merge Query dialog showing the Product Pricing query with the Sum of Unit Price and Sum of Unit Cost measures selected.](../media/infobridge-transform-queries/how-to-merge-query/merge-query-select-second-query.png)](../media/infobridge-transform-queries/how-to-merge-query/merge-query-select-second-query.png#lightbox)
5. Select **Apply**.

   [![Screenshot of the Merge Query dialog with both queries configured and ready to merge.](../media/infobridge-transform-queries/how-to-merge-query/merge-query-ready-to-apply.png)](../media/infobridge-transform-queries/how-to-merge-query/merge-query-ready-to-apply.png#lightbox)

   Infobridge creates a new merged query.

   The merged query preserves the shared row and column dimensions and combines the measures from all selected queries.

   [![Screenshot of the merged query showing ProductName, Category, Units, Sales Amount, Unit Price, and Unit Cost.](../media/infobridge-transform-queries/how-to-merge-query/merged-query-results.png)](../media/infobridge-transform-queries/how-to-merge-query/merged-query-results.png#lightbox)

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
