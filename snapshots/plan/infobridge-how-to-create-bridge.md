---
title: "Create a bridge to integrate and transform plans"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-how-to-create-bridge](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-how-to-create-bridge) · Last updated on **2026-07-28**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Create a bridge to integrate and transform plans

Summarize this article for me

A bridge provides a unified workspace for integrating data sources such as planning sheets, PowerTable sheets, or file-based sources. Use the bridge editor to transform and prepare data for planning. Bridges support data consolidation, real-time planning, and collaboration.

## Create a bridge

Consolidate planning sheets across dimensions with varying granularities using bridges.

1. To create a bridge, in the **Infobridge** ribbon, select **Create Query**.
2. Select the measures to consolidate in the bridge, then select **Create**.

   [![Screenshot of selecting measures to create a query from a planning sheet in Infobridge.](media/infobridge-how-to-create-bridge/create-query.png)](media/infobridge-how-to-create-bridge/create-query.png#lightbox)
3. Creating a query automatically opens Infobridge, where you can join, append, merge, pivot, and transform data. Select **Close** to return to the planning sheet.

   [![Screenshot of planning sheet data preview in a bridge.](media/infobridge-how-to-create-bridge/bridge-created.png)](media/infobridge-how-to-create-bridge/bridge-created.png#lightbox)
4. To access the bridge from a planning sheet, from the **Data** pane, expand **Queries**. Select **More options (â¦)** > **Edit** to open Infobridge. You can also delete or rename the query.

   [![Screenshot of accessing the bridge from a planning sheet.](media/infobridge-how-to-create-bridge/access-bridge.png)](media/infobridge-how-to-create-bridge/access-bridge.png#lightbox)
5. Repeat the same process to add measures from other planning sheets to the bridge.

   [![Screenshot of adding a second planning sheet to the bridge.](media/infobridge-how-to-create-bridge/create-second-query.png)](media/infobridge-how-to-create-bridge/create-second-query.png#lightbox)

   This example consolidates the bonus component across roles and departments in the bridge.

   [![Consolidating multi-dimensional planning data in a bridge.](media/infobridge-how-to-create-bridge/second-query-added-bridge.png)](media/infobridge-how-to-create-bridge/second-query-added-bridge.png#lightbox)
6. Within Infobridge, hover over the query name and select **More options (â¦)** to edit, delete, duplicate, rerun the job, or copy the query ID.

   [![Screenshot of options to edit, delete, refresh, and duplicate queries.](media/infobridge-how-to-create-bridge/bridge-query-options.png)](media/infobridge-how-to-create-bridge/bridge-query-options.png#lightbox)

## Import data into a bridge

Infobridge supports data integration to centralize data for analysis and reporting. Import and consolidate data from planning sheets, PowerTable sheets, and CSV, Excel, JSON, and Parquet files into a unified planning model.

1. Select **Add Source** and choose the source type.

   [![Screenshot of options to import sources like Excel, Parquet, CSV files, planning or powertable sheets.](media/infobridge-how-to-create-bridge/import-source.png)](media/infobridge-how-to-create-bridge/import-source.png#lightbox)
2. For file-based sources, select and upload the file.

   [![Screenshot of uploading a file source to infobridge.](media/infobridge-how-to-create-bridge/upload-files.png)](media/infobridge-how-to-create-bridge/upload-files.png#lightbox)
3. Infobridge adds a new query that holds the source data to the bridge.

   [![Screenshot of data imported into a bridge and stored in a query.](media/infobridge-how-to-create-bridge/query-created.png)](media/infobridge-how-to-create-bridge/query-created.png#lightbox)

To use data from the query in a planning sheet, import dimensions and measures from the **Queries** section of the **Data** pane.

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
