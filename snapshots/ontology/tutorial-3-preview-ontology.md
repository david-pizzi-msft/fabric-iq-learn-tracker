---
title: "Ontology (preview) tutorial part 3: Explore the ontology"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-3-preview-ontology](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-3-preview-ontology) · Last updated on **2026-11-17**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Ontology (preview) tutorial part 3: Explore the ontology

Summarize this article for me

In this tutorial step, explore your ontology in different ways. View the ontology in multiple canvas views, explore its entity instances, and explore the ontology's integrated graph.

Important

This feature is in [preview](../../fundamentals/preview).

## Explore canvas views

The home configuration canvas of ontology contains three views: [full ontology](#full-ontology), [neighborhood](#neighborhood), and [inheritance](#inheritance).

To switch views, select **Full ontology**, **Neighborhood**, or **Inheritance** in the upper-right corner of the canvas.

### Full ontology

The **Full ontology** view of the canvas shows all entity types and relationships present in the ontology. Select an entity type from the **Explorer** to center it in the canvas window.

[![Screenshot of the full ontology canvas view.](media/tutorial-3-preview-ontology/canvas-full-ontology.png)](media/tutorial-3-preview-ontology/canvas-full-ontology.png#lightbox)

### Neighborhood

The **Neighborhood** view of the canvas shows the modeled relationships of an entity type. Select an entity type from the **Explorer** to show it in the canvas along with related entity types.

[![Screenshot of the Neighborhood canvas view.](media/tutorial-3-preview-ontology/canvas-relationship.png)](media/tutorial-3-preview-ontology/canvas-relationship.png#lightbox)

### Inheritance

The **Inheritance** view of the canvas shows the inheritance structure of entity types. Select an entity type from the **Explorer** to show it in the canvas along with its inheritance relationships.

[![Screenshot of the Inheritance canvas view.](media/tutorial-3-preview-ontology/canvas-lineage.png)](media/tutorial-3-preview-ontology/canvas-lineage.png#lightbox)

## Explore entity instances

When you bound data to your entity types in [part 1 of the tutorial](tutorial-1-create-ontology), ontology automatically created instances of those entity types that map to the source data rows. View the entity instances with these steps:

1. Start in the Home configuration canvas of ontology. Select an entity type, and then select **Entity type > Open details** from the ribbon.

   [![Screenshot of opening entity type details from the Entity type ribbon.](media/tutorial-3-preview-ontology/view-entity-type-details.png)](media/tutorial-3-preview-ontology/view-entity-type-details.png#lightbox)
2. Open the **Instances** tab. You see a list of entity instances with data populated from the original lakehouse table data source. For example, the Inventory entity type instances have columns like `ProductId`, `OnHandQuantity`, and `ShelfAvailableUnits`.

   [![Screenshot of the Inventory instances.](media/tutorial-3-preview-ontology/instances.png)](media/tutorial-3-preview-ontology/instances.png#lightbox)

   Tip

   If data bindings don't load, confirm that the source data tables exist with matching column names, and that your Fabric identity has data access.

## Explore ontology graph

Ontology comes with an optional built-in instance of [graph in Microsoft Fabric](../../graph/overview). This feature isn't required for your ontology to work, but you can set it up to add another option for viewing and exploring your ontology details.

This section shows how to create an optional materialized graph from your existing ontology by selecting eligible entities and relationships and materializing the projection. Then, utilize the materialized graph to explore and discover connected data insights.

### Prepare the graph

1. Prepare data for graph visualization by defining an *entity type key* for each entity type. An entity type key shows which field uniquely identifies a row of sample data.

   Note

   Entity types must have entity type keys defined to be eligible for graph projection.

   1. Select an entity type in the canvas and select **Entity type > Open details**.
   2. Select **Define entity type key**.

      [![Screenshot of selecting an entity type key.](media/tutorial-3-preview-ontology/entity-type-key.png)](media/tutorial-3-preview-ontology/entity-type-key.png#lightbox)
   3. Select the right key from the following table. Select **Save**.

      | Entity type | Entity type key |
      | --- | --- |
      | Location | `LocationId` |
      | Store | `LocationId` |
      | Distribution Center | `LocationId` |
      | Product | `ProductId` |
      | Frozen Product | `ProductId` |
      | Perishable Product | `ProductId` |
      | Sale | *skip* |
      | Inventory | `StoreId`, `ProductId` (multi-select) |
      | Refrigeration Unit | `UnitId` |
      | Shipment | `ShipmentId` |
      | Supplier | `SupplierId` |
      | Refrigeration Telemetry | *skip* |
   4. Repeat for each entity type that you plan to project, except the types marked *skip*.
2. Set up the graph instance. From the home canvas ribbon, select **Home > Manage > Graph**.

   [![Screenshot of opening the manage graph option from the ribbon.](media/tutorial-3-preview-ontology/manage-graph.png)](media/tutorial-3-preview-ontology/manage-graph.png#lightbox)
3. On **Review validation**, wait for validation to finish. Review the **Status** column, and select **Ineligible** for an entry to learn why it can't be projected. Select **Select entities**.
4. On **Choose what to project**, select the eligible entity types and expand them to select their relationships. The **Preview** pane shows the selected subgraph. Each entity type becomes a node type, and each relationship type becomes an edge type.

   [![Screenshot of a focused projection containing Product, Supplier, and suppliedBy.](media/tutorial-3-preview-ontology/configure-graph.png)](media/tutorial-3-preview-ontology/configure-graph.png#lightbox)

   The screenshot shows a focused Product and Supplier example. For the queries later in this tutorial, include Store, Product, Shipment, Supplier, and their connecting relationships.

   Note

   Only delta tables from lakehouses or mirrored databases are supported. Sale and Refrigeration Telemetry use unsupported source types. Relationships also need a supported data binding with a single backing table. For example, you can use *dimproducts* as a mapping table for *suppliedBy*, mapping Product's `ProductId` to `ProductId` and Supplier's `SupplierId` to `SupplierId`. For more information, see [Create relationship types](how-to-create-relationship-types) and [Graph limitations](how-to-use-ontology-graph#limitations).

   Select **Continue**.
5. On **Projection summary**, review your selected entities and relationships. Select **Materialize**. Creating and loading the graph model might take several minutes.

   [![Screenshot of selecting to materialize the graph.](media/tutorial-3-preview-ontology/materialize-graph.png)](media/tutorial-3-preview-ontology/materialize-graph.png#lightbox)
6. Wait for **Materialization status** to show **Graph materialized** and a **Complete** refresh status.

### Explore the graph

1. In your Fabric workspace, open the graph model associated with your ontology. In the graph model, select **Query > Query now**.

   [![Screenshot of Query now in the graph model Query menu.](media/tutorial-3-preview-ontology/explore-graph.png)](media/tutorial-3-preview-ontology/explore-graph.png#lightbox)
2. The graph queryset view opens. On the right side of the queryset, select the puzzle piece icon to expand the **Components** pane. The Components pane shows the list of nodes and edges that are available in your graph.

   [![Screenshot of the Components pane.](media/tutorial-3-preview-ontology/graph-components.png)](media/tutorial-3-preview-ontology/graph-components.png#lightbox)
3. Under **Nodes**, select **Store**, **Product**, and **Shipment**. Under **Edges**, select **Shipment\_Store** and **Shipment\_Product**. The nodes and relationships are added to the canvas.

   [![Screenshot of entities and relationships selected in the Components pane.](media/tutorial-3-preview-ontology/graph-components-selected.png)](media/tutorial-3-preview-ontology/graph-components-selected.png#lightbox)
4. Select **Path query** from the top ribbon and confirm the **Switch** when prompted. In this view, you can create complex path-finding queries.
5. Enter the following query details to search for nodes within two hops of the Seattle store's relationship with the supplier Cascade Fresh Products.

   - **Start node:** Store
   - **End node:** Supplier
   - **Filter start node:** *City = Seattle*
   - **Filter end node:** *SupplierName = Cascade Fresh Products*
   - **Max hops:** 2

   [![Screenshot of building a path query with a start node, direction, and end node.](media/tutorial-3-preview-ontology/path-query.png)](media/tutorial-3-preview-ontology/path-query.png#lightbox)
6. Select **Run query** to run the query and render the result in both the query result canvas and the path results pane.

   [![Screenshot of the path query results.](media/tutorial-3-preview-ontology/path-query-results.png)](media/tutorial-3-preview-ontology/path-query-results.png#lightbox)

If you want, try more queries and [graph features](../../graph/overview) to explore the ontology further before continuing with the tutorial.

## Next steps

In this step, you explored the ontology, including the canvas, entity type instances, and graph view. Next, use the ontology agent to explore the data further with natural language queries.

Continue to [Consume ontology from agents](tutorial-4-use-agent).

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
