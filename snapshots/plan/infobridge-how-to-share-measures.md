---
title: "Import measures between planning sheets with Infobridge"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-how-to-share-measures](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-how-to-share-measures) · Last updated on **2026-08-31**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Import measures between planning sheets with Infobridge

Summarize this article for me

By using Infobridge in planning, you can consolidate measures from different data sources, such as files and planning sheets, into a target planning sheet. For example, you can integrate multiple regional forecasts into a single global forecast.

In this article, you learn how to import a measure from one planning sheet into another.

## Prerequisites

Create two planning sheets with identical row and column dimensions. The row and column dimensions must match in both sheets to import measures successfully.

Sample reports used in this article:

- A COGS planning sheet that is used for forecasting and contains a *COGS Projections* data input measure.

  [![Screenshot of a sample COGS report with the described input measure.](media/infobridge-how-to-share-measures/sample-cogs.png)](media/infobridge-how-to-share-measures/sample-cogs.png#lightbox)
- A sales planning sheet

  [![Screenshot of a sample quarterly sales planning sheet.](media/infobridge-how-to-share-measures/sample-sales.png)](media/infobridge-how-to-share-measures/sample-sales.png#lightbox)

In this article, you use Infobridge to bring COGS projections into the Sales report.

## Create a bridge

1. Go to **Data** > **Queries** > **Add** and select **Planning sheet**.
2. Select **COGS Report** from the **Sheet** dialog.
3. Select the **COGS Projections** measure to be uploaded to the bridge. Select **Add**.

   [![Screenshot of adding a COGS projection measure to the report.](media/infobridge-how-to-share-measures/add-bridge.png)](media/infobridge-how-to-share-measures/add-bridge.png#lightbox)
4. A new bridge is created with the COGS Projections measure. The scope of this article is limited to importing a measure without any transformations. Validate the data and select **Close**.

   [![Screenshot of the newly created bridge with the imported measure.](media/infobridge-how-to-share-measures/new-bridge.png)](media/infobridge-how-to-share-measures/new-bridge.png#lightbox)

Note

Infobridge can be used to transform, cleanse, and change the structure of the data.

## Import a measure

1. Open the target planning sheet, *Quarterly Sales Report*.
2. The bridge created in the previous step appears under the **Queries** section. To import COGS projections, add it to the **Values** field.

   [![Screenshot of the imported bridge in the target planning sheet.](media/infobridge-how-to-share-measures/imported-measure.png)](media/infobridge-how-to-share-measures/imported-measure.png#lightbox)

Measures from Infobridge act like regular data source measures and can be used for calculations or included in other reports and visualizations.

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
