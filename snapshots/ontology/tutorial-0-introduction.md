---
title: "Ontology (preview) tutorial part 0: Introduction and environment setup"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-0-introduction](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-0-introduction) · Last updated on **2026-09-29**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Ontology (preview) tutorial part 0: Introduction and environment setup

Summarize this article for me

This tutorial shows how to create your first ontology (preview) in Microsoft Fabric. You create ontology elements manually and with the help of the ontology agent, and bind them to data from multiple OneLake data sources. You enrich the ontology with additional metadata and information, and explore the completed ontology in the visual experience as well as through ontology agent queries.

Important

This feature is in [preview](../../fundamentals/preview).

The example scenario for this tutorial is a fictional company called Lakeshore Retail. Lakeshore is a retail ice cream seller that keeps data on sales and refrigerator streaming data. In the tutorial, you create entity types like *Store*, *Products*, and *Sale*. You bind streaming data like refrigerator temperature from an eventhouse, and answer questions like: "What is the top product by revenue across all stores?"

## Prerequisites

- A [workspace](../../fundamentals/create-workspaces) with a Microsoft Fabric-enabled [capacity](../../enterprise/licenses#capacity). Use this workspace for all resources you create in the tutorial.
- The *Users can create ontology (preview) items* and *Users can create Fabric items* settings enabled on your Fabric tenant.

  A [Fabric administrator](../../admin/roles) can enable the settings in **OneLake catalog** > **Govern** > **Configurations** > [**Tenant settings**](../../admin/tenant-settings-index):

  [![Screenshot of enabling ontology in the admin portal.](media/overview-tenant-settings/prerequisite-ontology.png)](media/overview-tenant-settings/prerequisite-ontology.png#lightbox)

  [![Screenshot of enabling Fabric items in the admin portal.](media/overview-tenant-settings/prerequisite-fabric-items.png)](media/overview-tenant-settings/prerequisite-fabric-items.png#lightbox)

## Scenario

Lakeshore Retail is a multi-region retailer that sells general merchandise, perishable goods, and frozen products through stores supplied by regional distribution centers. Store operations teams need to maintain product availability without increasing waste, while frozen products must remain within safe storage temperatures throughout the retail cold chain.

This tutorial works toward one concrete operational outcome: *Which high-priority stores in the West have frozen products below safety stock, a recent refrigeration-temperature exception, and on-shelf availability below target? For each store, show the next inbound shipment and its expected arrival.*

With a robust ontology, the ontology agent can answer this question. Design an ontology that helps the agent understand that a frozen product is a type of product, whatâ¯below safety stockâ¯andâ¯temperature exceptionâ¯mean, how products are stocked at stores, which refrigeration units operate at each store, how inbound shipments connect distribution centers to stores, and how the governed Power BI measure for on-shelf availability should be calculated.

The ontology in this tutorial connects operational signals, business definitions, governed metrics, and business relationships so that an agent can explain where intervention is needed and why.

### Ontology

The Lakeshore Retail elements in this tutorial comprise the following ontology. Review the diagram to understand the entity types and relationships that are involved in the scenario.

[![Diagram showing entity types like Store, Shipment, and Product connected by relationships like deliversTo and stockedAt .](media/tutorial-0-introduction/scenario.png)](media/tutorial-0-introduction/scenario.png#lightbox)

## Download sample data

Download the contents of the **New experience** folder from ontology samples in GitHub: [Ontology samples](https://github.com/microsoft/fabric-samples/tree/main/docs-samples/iq/ontology/new-experience).

The sample data includes a set of CSV files containing static entity details about the Lakeshore Retail scenario and streaming data from its refrigerators, as well as a Power BI semantic model containing sales data.

## Prepare the lakehouse

Follow these steps to prepare the sample tutorial data in a lakehouse.

1. Start in your Fabric workspace. Use the **+ New item** button to create a new **Lakehouse** item.

   [![Screenshot of creating a new lakehouse item.](media/tutorial-0-introduction/lakehouse-new.png)](media/tutorial-0-introduction/lakehouse-new.png#lightbox)
2. For the lakehouse **Name**, enter *LakeshoreStaticDataLH*. For **Location**, select your workspace. Keep the **Lakehouse schemas** checkbox selected (default) and select **Create**.
3. The new lakehouse opens when it's ready. From the lakehouse ribbon, select **Get data > Upload files**.

   [![Screenshot of uploading files to the lakehouse.](media/tutorial-0-introduction/lakehouse-upload.png)](media/tutorial-0-introduction/lakehouse-upload.png#lightbox)
4. Upload **all except one of the sample CSV files** to your lakehouse. Don't upload *refrigeration\_telemetry.csv* (you upload this file to eventhouse instead in a later step), or *SalesReport.pbix* (you import this data through the ontology agent in a later step).
5. Expand the **Files** folder in the Explorer to view your uploaded files. Next, load each file to a delta table.

   For each file, select **...** next to the file name, then **Load to Tables > New table**.

   [![Screenshot of the load to tables dialog in lakehouse.](media/tutorial-0-introduction/lakehouse-new-table.png)](media/tutorial-0-introduction/lakehouse-new-table.png#lightbox)

   Continue through the table creation dialog, keeping the default settings.

The lakehouse looks like the following image when you're done. The default table names reflect the file names in all lowercase.

[![Screenshot of the tables in the lakehouse.](media/tutorial-0-introduction/lakehouse-tables.png)](media/tutorial-0-introduction/lakehouse-tables.png#lightbox)

## Prepare the eventhouse

Follow these steps to upload the device streaming data file to a KQL database in an eventhouse.

1. In your Fabric workspace, select **+ New item** to create a new eventhouse called *LakeshoreTelemetryDataEH*. Fabric creates a default KQL database with the same name.
2. The eventhouse opens when it's ready. Open the KQL database by selecting its name in the explorer.

   [![Screenshot of the KQL database in the eventhouse.](media/tutorial-0-introduction/eventhouse-database.png)](media/tutorial-0-introduction/eventhouse-database.png#lightbox)
3. Next, create a new table called *RefrigerationTelemetry* that uses the *refrigeration\_telemetry.csv* sample file as a source.

   In the menu ribbon, select **Get data > Local file**.

   [![Screenshot of the data source options for the database.](media/tutorial-0-introduction/eventhouse-get-data.png)](media/tutorial-0-introduction/eventhouse-get-data.png#lightbox)

   Create a **New table** called *RefrigerationTelemetry* and browse for the *refrigeration\_telemetry.csv* file that you downloaded earlier.

   [![Screenshot of uploading the csv file and creating the table.](media/tutorial-0-introduction/eventhouse-get-data-table.png)](media/tutorial-0-introduction/eventhouse-get-data-table.png#lightbox)

   Continue through the table creation dialog, keeping the default settings.

When you're done, the KQL database shows the *RefrigerationTelemetry* table with data:

[![Screenshot of the table in the database.](media/tutorial-0-introduction/eventhouse-table.png)](media/tutorial-0-introduction/eventhouse-table.png#lightbox)

## Upload the semantic model

Finally, upload the sample semantic model to your workspace.

1. In your Fabric workspace, select **Import** > **Report, Paginated Report or Workbook** > **From this computer**.

   [![Screenshot of importing a report into a workspace.](media/tutorial-0-introduction/import.png)](media/tutorial-0-introduction/import.png#lightbox)

   Find the *SalesReport.pbix* file that you downloaded and select **Open**.
2. The report is visible in your workspace, and a semantic model is created with the same name.

   [![Screenshot of the report now visible in the workspace.](media/tutorial-0-introduction/workspace-semantic-model.png)](media/tutorial-0-introduction/workspace-semantic-model.png#lightbox)

## Next steps

Now your sample scenario is set up in Fabric. Next, create an ontology (preview) item and add elements to it that connect to these data sources: [Create an ontology](tutorial-1-create-ontology).

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
