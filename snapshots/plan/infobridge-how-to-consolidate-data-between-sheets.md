---
title: "Consolidate data between sheets"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-how-to-consolidate-data-between-sheets](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-how-to-consolidate-data-between-sheets) · Last updated on **2026-08-14**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Consolidate data between sheets

Summarize this article for me

Use Infobridge to consolidate plans, budgets, and forecasts from multiple planning sheets into a single, unified plan. For example, you can combine regional sales plans into a consolidated sales plan.

In this article, you learn how to combine rows from multiple planning sheets by using **Append Query**.

## Combine rows in a bridge

Consider a scenario where you want to consolidate regional sales plans.

1. Create a bridge and add the individual regional plans.

   [![Screenshot of a bridge with Central Sales, East Sales, South Sales, and West Sales queries.](media/infobridge-how-to-consolidate-data-between-sheets/create-bridge.png)](media/infobridge-how-to-consolidate-data-between-sheets/create-bridge.png#lightbox)
2. On the **Home** ribbon, select **Append Query**. Then select the queries you want to combine.

   [![Screenshot of the Append Query menu with Central Sales, East Sales, and South Sales selected.](media/infobridge-how-to-consolidate-data-between-sheets/append-query.png)](media/infobridge-how-to-consolidate-data-between-sheets/append-query.png#lightbox)

   A new query is created after the rows from the selected queries are combined.

   [![Screenshot showing the new appended query in the Queries list.](media/infobridge-how-to-consolidate-data-between-sheets/appended-query.png)](media/infobridge-how-to-consolidate-data-between-sheets/appended-query.png#lightbox)

## Map the appended query to a planning sheet

1. Create a new planning sheet. In the **Data** pane, under **Queries**, expand the appended query and select the row dimensions you want to use.

   For example, select **Region**, **Category**, and **Sub-Category** to add them to **Rows**.

   [![Screenshot of a planning sheet with Region, Category, and Sub-Category mapped to Rows from the appended query.](media/infobridge-how-to-consolidate-data-between-sheets/map-row-dimensions.png)](media/infobridge-how-to-consolidate-data-between-sheets/map-row-dimensions.png#lightbox)

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
