---
title: "Blend measures by using Infobridge"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-how-to-blend-measures](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-how-to-blend-measures) · Last updated on **2026-08-24**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Blend measures by using Infobridge

Summarize this article for me

Blend measures to combine measures maintained in different planning sheets or available from Infobridge queries. You can use a measure from another planning sheet directly or use an Infobridge query to make a measure available to another planning sheet.

A blend measure can combine values from multiple sources while keeping each source measure connected to its planning data.

## Prerequisites

Before you begin, ensure you have:

- A Unit Price planning sheet with a `Forecast UnitPrice` measure.
- A Sales Plan planning sheet with a `Forecast Quantity` measure.
- A COGS Plan planning sheet with a `Forecast UnitCost` measure.
- Common dimensions that allow the measures to be evaluated at the required planning level, such as Account, ProductCategory, ProductID, ProductName, and Date.

Note

You can blend measures from one planning sheet with measures from another planning sheet when both sheets have the same dimensions. The common dimensions allow the measures to be evaluated at the same planning level.

## Create the source measures

Create or verify the measures that you want to use in the blend calculation.

1. Go to the **Unit Price** planning sheet and verify that the `Forecast UnitPrice` measure is available.

   [![Screenshot of the Unit Price planning sheet with the Forecast UnitPrice measure.](media/infobridge-how-to-blend-measures/unit-price-forecast-unitprice.png)](media/infobridge-how-to-blend-measures/unit-price-forecast-unitprice.png#lightbox)
2. Go to the **Sales Plan** planning sheet and verify that the `Forecast Quantity` measure contains the values that you want to use.

   [![Screenshot of the Sales Plan planning sheet with forecast quantity values.](media/infobridge-how-to-blend-measures/sales-plan-forecast-quantity.png)](media/infobridge-how-to-blend-measures/sales-plan-forecast-quantity.png#lightbox)

## Add a measure from another planning sheet

Use **From Sheets** to add a measure that's maintained in another planning sheet.

1. In the **Sales Plan** sheet, in the **Data** pane, expand **From Sheets**.
2. Expand **Unit Price**, and add `Forecast UnitPrice` to **Values**.

The measure is available in the **Sales Plan** sheet and you can use it with the existing measures.

[![Screenshot of the Sales Plan planning sheet with Forecast UnitPrice added from the Unit Price sheet to Values.](media/infobridge-how-to-blend-measures/sales-plan-forecast-unitprice-from-sheet.png)](media/infobridge-how-to-blend-measures/sales-plan-forecast-unitprice-from-sheet.png#lightbox)

## Create a query for a measure

Use **Queries** to add a measure from an Infobridge query to another planning sheet. You can use the query to prepare and transform the data before using the measure in a planning sheet.

To create a query that contains `Forecast Quantity`:

1. In the **Infobridge** ribbon, select **Create Query**.
2. In **Create Query**, select `Forecast Quantity`.
3. Select **Create**.

   [![Screenshot of the Create Query pane with Forecast Quantity selected.](media/infobridge-how-to-blend-measures/create-query-forecast-quantity.png)](media/infobridge-how-to-blend-measures/create-query-forecast-quantity.png#lightbox)

   When you create the query, Infobridge opens so you can join, append, merge, pivot, and transform the data.

   [![Screenshot of the Infobridge bridge created from the Sales Plan sheet.](media/infobridge-how-to-blend-measures/sales-plan-infobridge-bridge.png)](media/infobridge-how-to-blend-measures/sales-plan-infobridge-bridge.png#lightbox)
4. Review the query results to verify that the required dimensions and `Forecast Quantity` are available.
5. Select **Close** to return to the planning sheet.

## Add the query measure to a planning sheet

Use the query measure in the COGS Plan sheet.

1. Go to the **COGS Plan** planning sheet and verify that `UnitCost` and `Forecast UnitCost` are available.

   [![Screenshot of the COGS Plan planning sheet with UnitCost and Forecast UnitCost measures.](media/infobridge-how-to-blend-measures/cogs-plan-unitcost-forecast-unitcost.png)](media/infobridge-how-to-blend-measures/cogs-plan-unitcost-forecast-unitcost.png#lightbox)
2. In the **Data** pane, expand **Queries**.
3. Expand **Query 1 - Sales Plan**.
4. Add `Forecast Quantity` to **Values**.

   The COGS Plan sheet now has Forecast Quantity from the Infobridge query and Forecast UnitCost from the COGS Plan sheet.

   [![Screenshot of the COGS Plan planning sheet with Forecast Quantity added from the Sales Plan query.](media/infobridge-how-to-blend-measures/cogs-plan-forecast-quantity-from-query.png)](media/infobridge-how-to-blend-measures/cogs-plan-forecast-quantity-from-query.png#lightbox)

## Create a blend measure

Create a visual measure that combines forecast quantity with forecast unit cost.

1. In the **Planning** ribbon, select **Formula**.
2. In **Title**, enter `Forecast COGS`.
3. For **Insert as**, select **Visual Measure**.
4. For **Data type**, select **Number**.
5. In **Formula**, enter:

   ```
   [Sum of Forecast Quantity]*[Forecast UnitCost]
   ```
6. For **Column aggregation type**, select **Sum**.
7. For **Row aggregation type**, select **Formula**.
8. Select **Create**.

   [![Screenshot of the Formula Measure pane configured to create the Forecast COGS measure.](media/infobridge-how-to-blend-measures/create-forecast-cogs-measure.png)](media/infobridge-how-to-blend-measures/create-forecast-cogs-measure.png#lightbox)

   The `Forecast COGS` measure combines `Forecast Quantity` from the Infobridge query with `Forecast UnitCost` maintained in the COGS Plan sheet.

   [![Screenshot of the COGS Plan planning sheet displaying the Forecast COGS measure.](media/infobridge-how-to-blend-measures/cogs-plan-forecast-cogs-measure.png)](media/infobridge-how-to-blend-measures/cogs-plan-forecast-cogs-measure.png#lightbox)

Use this approach when a calculation depends on measures maintained in different planning processes. The source measures remain connected to their respective planning data, and the blend measure uses those values in the calculation.

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
