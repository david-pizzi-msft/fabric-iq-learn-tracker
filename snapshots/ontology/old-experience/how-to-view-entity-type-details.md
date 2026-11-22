---
title: "Entity type details in ontology (preview) - Old experience"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/old-experience/how-to-view-entity-type-details](https://learn.microsoft.com/en-us/fabric/iq/ontology/old-experience/how-to-view-entity-type-details) · Last updated on **2026-09-29**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Entity type details in ontology (preview) - Old experience

Summarize this article for me

Important

This article is about the **old experience** of ontology (preview). You can't create ontology items with the old experience anymore through the ontology interface in Fabric. It's still possible to create instances of the old experience using the ontology APIs and CI/CD.

Use this documentation only if you're maintaining an existing old experience item. Otherwise, see the [ontology (preview) new experience documentation](../overview).

The old experience of ontology retires on Jan 31, 2027.

The *entity type details* view in ontology (preview) lets you explore your instantiated ontology data. The experience includes basic data previews, instance data, and a graph view.

Important

This feature is in [preview](../../../fundamentals/preview).

When you create your ontology (preview) item, you automatically create a [Graph in Microsoft Fabric](../../../graph/overview) child item that stores and displays data in the **Overview** tab of the entity type details.

[![Screenshot of data graphs in the entity type details overview page.](media/how-to-view-entity-type-details/entity-type-details-overview-1.png)](media/how-to-view-entity-type-details/entity-type-details-overview-1.png#lightbox)

## Prerequisites

Before viewing entity type details, make sure you have the following prerequisites:

- A [Fabric workspace](../../../fundamentals/create-workspaces) with a Microsoft Fabric-enabled [capacity](../../../enterprise/licenses#capacity).
- **Ontology item (preview)** enabled on your tenant.
- An ontology (preview) item with [data binding](how-to-bind-data) completed.

## Key concepts

The entity type details view uses the following ontology (preview) concepts. For definitions of these terms, see the [Ontology (preview) glossary](../resources-glossary).

- *Entity type*
- *Entity instance*
- *Entity type details*
- *[Graph in Microsoft Fabric](../../../graph/overview)*

## Access entity type details

Follow these steps to access the entity type details in your ontology (preview) item.

1. In the **Explorer** pane of the Home configuration canvas, select the entity type that you want to view. Select **View Entity Type details** from the top ribbon.

   ![Screenshot of opening the experience from the menu ribbon.](media/how-to-view-entity-type-details/view-entity-type-details.png)
2. The entity type details view opens to the **Configure** page. Tabs across the top of the page allow you to switch between the **Configure**, **Instances**, and **Overview** pages.

   [![Screenshot of the entity type details configure page. The three tabs are highlighted.](media/how-to-view-entity-type-details/entity-type-details-configure-1.png)](media/how-to-view-entity-type-details/entity-type-details-configure-1.png#lightbox)

## Configure tab

In the **Configure** page, you can manage properties, data bindings, relationship types, and report links for the entity type.

[![Screenshot of the entity type details configure page.](media/how-to-view-entity-type-details/entity-type-details-configure-2.png)](media/how-to-view-entity-type-details/entity-type-details-configure-2.png#lightbox)

For more information about these features, see the following articles:

- [Add properties](how-to-create-entity-types#add-properties)
- [Bind data](how-to-bind-data)
- [Add relationship types](how-to-create-relationship-types)
- [Use resource links](how-to-use-resource-links)

## Instances tab

On the **Instances** page, you can view the instances associated with the entity type and their static property values.

[![Screenshot of the entity type details instances page.](media/how-to-view-entity-type-details/entity-type-details-instances.png)](media/how-to-view-entity-type-details/entity-type-details-instances.png#lightbox)

### Explore an individual instance

You can browse to a specific entity instance to see more information about that specific instance.

To open the instance view, start in the **Instances** tab of the entity type details, and select a row from the table.

[![Screenshot of selecting a specific entity type instance.](media/how-to-view-entity-type-details/entity-type-details-instances-select.png)](media/how-to-view-entity-type-details/entity-type-details-instances-select.png#lightbox)

The instance view loads and displays tiles for its static properties, relationships, and time series data.

[![Screenshot of data graphs for a single entity type instance.](media/how-to-view-entity-type-details/entity-type-details-instances-details.png)](media/how-to-view-entity-type-details/entity-type-details-instances-details.png#lightbox)

You can **Expand** the relationship graph to open its full Graph view and run queries that are scoped specifically to this entity instance. For more information about the graph view and querying, see the [Open graph view](#open-graph-view) section later in this article.

[![Screenshot of the graph and query view for a specific entity instance.](media/how-to-view-entity-type-details/entity-type-details-instances-query.png)](media/how-to-view-entity-type-details/entity-type-details-instances-query.png#lightbox)

## Overview tab

In the **Overview** page, you can view entity instances as tiles in a dashboard. Tiles are provided through [Graph in Microsoft Fabric](../../../graph/overview), and reflect relationships and time series data for the entity type.

[![Screenshot of the entity type details overview page.](media/how-to-view-entity-type-details/entity-type-details-overview-2.png)](media/how-to-view-entity-type-details/entity-type-details-overview-2.png#lightbox)

### Manage tiles

The entity type details in ontology (preview) automatically shows tiles that display data about your entity types, including entity instance details and relationship graphs. All tiles you create at the entity level also appear at the [entity instance](#explore-an-individual-instance) level.

To create more tiles, follow these steps.

1. From the top right corner of the page, select **Add Tile**.

   [![Screenshot of adding a tile.](media/how-to-view-entity-type-details/add-tile.png)](media/how-to-view-entity-type-details/add-tile.png#lightbox)
2. Select the type of tile you want to create: a **Timeseries** (time series) line chart for streaming data, a **Static property** bar chart for static data, a **Resource links** tile to display linked external resources, or a **Fabric graph** tile to visualize relationships (only one Fabric graph tile is allowed per overview).
3. Complete the configuration for your chosen tile type. The following image shows an example of configuring a static property tile.

   ![Screenshot of configuring a static property tile.](media/how-to-view-entity-type-details/add-tile-static.png)
4. Back on the overview page, verify that your new tile is visible at the bottom of the dashboard.

If necessary, use the time range selector to configure the time range for the data displayed in time series tiles.

[![Screenshot of configuring the time range.](media/how-to-view-entity-type-details/change-date-range.png)](media/how-to-view-entity-type-details/change-date-range.png#lightbox)

To edit or delete existing tiles, select **...** in the upper right corner of a tile.

[![Screenshot of edit and delete options for a tile.](media/how-to-view-entity-type-details/edit-delete.png)](media/how-to-view-entity-type-details/edit-delete.png#lightbox)

### Open graph view

Follow these steps to view your ontology (preview) entities in a graph view provided by [Graph in Microsoft Fabric](../../../graph/overview).

1. Select **Expand** from a graph tile in the **Overview** tab.

   ![Screenshot of expanding a graph tile.](media/how-to-view-entity-type-details/graph-expand.png)
2. The full graph view opens:

   [![Screenshot of the full graph view showing entity types and their relationships.](media/how-to-view-entity-type-details/graph-full.png)](media/how-to-view-entity-type-details/graph-full.png#lightbox)

In the graph view, you can explore using Graph in Microsoft Fabric's interface, and craft custom queries as described in the next section.

#### Query across entity instances

In the full graph view, use the **Query builder** ribbon to craft custom queries.

[![Screenshot of the query builder.](media/how-to-view-entity-type-details/query-builder.png)](media/how-to-view-entity-type-details/query-builder.png#lightbox)

The default query shows the current entities and all relationships that are one hop away. Select **Run query** to run the default query. You see the results in a pane underneath the relationship type graph.

[![Screenshot of the default query results showing specific instances that meet the criteria.](media/how-to-view-entity-type-details/query-default.png)](media/how-to-view-entity-type-details/query-default.png#lightbox)

To change the query, you can **Add filters** for property values or change the **Components** that are visible in the graph.

[![Screenshot of the filter options for a query.](media/how-to-view-entity-type-details/query-filter.png)](media/how-to-view-entity-type-details/query-filter.png#lightbox)

You can also change the view type of the query results from **Diagram** to **Card** or **Table**.

[![Screenshot of query results in table view.](media/how-to-view-entity-type-details/query-view.png)](media/how-to-view-entity-type-details/query-view.png#lightbox)

To run more complex queries or explore the data in more detail, navigate to the Graph in Microsoft Fabric interface by selecting **Open in Fabric Graph**. For more information, see [Graph in Microsoft Fabric overview (preview)](../../../graph/overview).

![Screenshot of the button to open Graph in Microsoft Fabric.](media/how-to-view-entity-type-details/open-in-graph.png)

## Refresh the graph model

This section describes how and when your bound data stays up to date in your ontology (preview) item.

Downstream experiences automatically refresh whenever you make changes to your ontology schema. This feature ensures that whenever you add, edit, or remove any element like properties, types, or relationships, the system re-ingests all currently bound data to keep your downstream experiences in sync with the latest schema adjustments.

However, this automatic refresh only applies to changes made within the schema itself. If there are changes to the external data source that feeds your graph (for example, if new records are added, updated, or deleted in the upstream system), the graph doesn't know about these changes unless you explicitly inform it. In this case, your graph might display stale data until a new ingestion is triggered. You can enforce an update by manually refreshing the graph.

Important

We recommend batching updates for refresh instead of refreshing the graph after every individual change, as the graph does a full refresh each time. **This approach has cost implications for the [Graph in Microsoft Fabric](../../../graph/overview) item.**

To refresh the graph, follow these steps:

1. Go to your Fabric workspace, and locate the graph model associated with your ontology (preview) item.

   ![Screenshot of the graph model in the workspace view.](media/how-to-view-entity-type-details/refresh-graph-1.png)
2. Select **...** to expand the option menu for the graph model, and select **Schedule**.

   ![Screenshot of the Schedule option for the graph model.](media/how-to-view-entity-type-details/refresh-graph-2.png)
3. In the **Schedule** view, select **Refresh now**.

   ![Screenshot of the Refresh now button in the graph model scheduling options.](media/how-to-view-entity-type-details/refresh-graph-3.png)

   Tip

   You can also use this panel to manage a recurring refresh schedule for the graph model, to keep your ontology (preview) data up to date automatically on a specified cadence.
4. Verify that when you return to the ontology item, the data shown reflects your changes.

## Troubleshooting

For troubleshooting tips related to the entity type details in ontology (preview), see [Troubleshoot ontology (preview)](../resources-troubleshooting).

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
