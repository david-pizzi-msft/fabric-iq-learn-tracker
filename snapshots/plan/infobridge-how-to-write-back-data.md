---
title: "Write back transformed data from Infobridge"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-how-to-write-back-data](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-how-to-write-back-data) · Last updated on **2026-07-28**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Write back transformed data from Infobridge

Summarize this article for me

Infobridge in planning not only transforms and integrates data from multiple sources but also enables direct writeback to a Microsoft Fabric SQL database. This process allows the transformed dataset produced in a bridge to become a governed dataset stored in the enterprise data platform.

This section explains how to write back the output of a bridge to a Fabric SQL database destination.

## Writeback overview

In the following example, a sample bridge is created using **Infobridge** that merges two data sources:

- **Query 1**: A planning sheet containing actual revenue from 2026
- **Query 2**: An external Excel file containing forecast and projected revenue

Through the **Merge Query** operation, measures from both queries are combined to produce a unified dataset that integrates actual and forecasted values.

Once the transformation is complete, the merged dataset can be written back to a **Fabric SQL database**. This writeback allows the combined data to be used by downstream applications such as analytics, planning models, and operational reporting systems.

Here's an example of transformed data:

[![Screenshot of the data that Infobridge transformed.](media/infobridge-how-to-write-back-data/transformed-data.png)](media/infobridge-how-to-write-back-data/transformed-data.png#lightbox)

## Add new destination

1. Select **Add new destination** to add a writeback destination.
2. Enter the Fabric SQL connection information, including the connection name, database name for writeback, schema, writeback table name, decimal precision, and text length.

   ![Screenshot of the Create destination configuration.](media/infobridge-how-to-write-back-data/create-destination.png)
3. The writeback destination is configured.

   [![Screenshot of the data in its newly configured destination.](media/infobridge-how-to-write-back-data/configured-destination.png)](media/infobridge-how-to-write-back-data/configured-destination.png#lightbox)

## Write back data

1. Select **Writeback** from the **Writeback** tab. This instruction writes back the merged query to the chosen destination.

   [![Screenshot of the Writeback tab and the merged query.](media/infobridge-how-to-write-back-data/write-back.png)](media/infobridge-how-to-write-back-data/write-back.png#lightbox)
2. The data that is written back to the Fabric SQL database is shown in the following image.

   [![Screenshot of the data after being written back to the Fabric SQL database.](media/infobridge-how-to-write-back-data/data-sql.png)](media/infobridge-how-to-write-back-data/data-sql.png#lightbox)

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
