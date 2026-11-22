---
title: "Ontology (preview) tutorial part 2: Enrich the ontology with additional data"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-2-enrich-ontology](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-2-enrich-ontology) · Last updated on **2026-11-17**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Ontology (preview) tutorial part 2: Enrich the ontology with additional data

Summarize this article for me

In this tutorial step, you enrich your ontology by adding metadata to the entity type and its properties. You also create some ontology business rules. This information adds more domain context and operational information.

Important

This feature is in [preview](../../fundamentals/preview).

## Add metadata

You can add metadata to entity types and to specific properties on the entity types. You can also add metadata to relationships.

### Add entity type metadata

Metadata for entity types supports descriptions, synonyms, and additional metadata key-value pairs. Follow these steps to add that metadata to your entity types.

1. Select an entity type in the **Explorer**, and then select **Entity type > Open details**. The following screenshot shows Inventory selected.

   [![Screenshot of Inventory selected on the canvas with the Entity type tab available.](media/tutorial-2-enrich-ontology/store-view-entity-type-details.png)](media/tutorial-2-enrich-ontology/store-view-entity-type-details.png#lightbox)
2. For the Store metadata example, repeat the previous step for **Store**. On its **Configure** page, scroll down to the **Metadata** section and select **Edit**.
3. Enter the following **Description**: *Filtered locations binding whereâ¯LocationType = STORE;â¯priorityDefinition=Tier 1 stores require same-day response.*

   [![Screenshot of adding a metadata description to Store.](media/tutorial-2-enrich-ontology/store-metadata.png)](media/tutorial-2-enrich-ontology/store-metadata.png#lightbox)

   Select **Update**.
4. Use the same steps that you used for the Store entity type to add the entity type metadata described in the following table.

   | Entity type name | Metadata | Notes |
   | --- | --- | --- |
   | Distribution Center | **Description:** *Filtered locations binding where LocationType = DC.* |  |
   | Frozen Product | **Description:** *Filtered items binding where StorageClass = FROZEN.* |  |
   | Perishable Product | **Description:** *Filtered items binding where StorageClass = PERISHABLE.* |  |
   | Inventory | **Additional metadata:**   On-Shelf Availability % : On-shelf availability percentage is calculated by dividing the total ShelfAvailableUnits by the total ShelfCapacityUnits. If total ShelfCapacityUnits is zero, the result is blank to avoid division by zero.    Low On-Shelf Availability : On-Shelf Availability % less than 95 | Additional metadata is entered as key-value pairs. |
   | Sale | **Description** and **Synonyms** are already added to the entity type from the semantic model import. | Review the metadata that's already there (no need to add metadata manually). |

### Add entity type property metadata

Metadata for properties supports descriptions and additional metadata key-value pairs, but not synonyms. Follow these steps to add metadata to properties on your entity types.

1. Start with Product > `ProductId`. Select the Product entity type, select **...**, and then select **Bind data**.

   [![Screenshot of opening the Product data bindings.](media/tutorial-2-enrich-ontology/product-bind-data.png)](media/tutorial-2-enrich-ontology/product-bind-data.png#lightbox)
2. Select **Properties** under **Entity type** in the left pane.
3. Next to the `ProductId` property, select **Metadata**.

   [![Screenshot of selecting metadata for the property.](media/tutorial-2-enrich-ontology/product-property-metadata.png)](media/tutorial-2-enrich-ontology/product-property-metadata.png#lightbox)
4. For **Description**, enter *Enterprise product identifier; not a supplier SKU or UPC.*

   [![Screenshot of entering metadata description for the property.](media/tutorial-2-enrich-ontology/product-property-metadata-edit.png)](media/tutorial-2-enrich-ontology/product-property-metadata-edit.png#lightbox)

   Select **Update**.
5. Select **Save**.
6. Use the same steps that you used for the Product > `ProductId` property to add the property metadata described in the following table.

   | Entity Type | Property | Metadata |
   | --- | --- | --- |
   | Refrigeration Telemetry | TemperatureC | **Description:** Temperature in Celsius. |
   | Inventory | InventoryStatus | **Description:** 0â¯isâ¯AT\_RISKâ¯andâ¯1â¯isâ¯HEALTHY. |

### Add relationship metadata

Metadata for relationship types supports descriptions and additional metadata key-value pairs, but not synonyms. Follow these steps to add metadata to your relationship types.

1. Start with *Store operates Refrigeration Unit*. Select the Store entity in the **Explorer** to show it on the configuration canvas, and select the *operates* relationship connected to it to open the relationship configuration options.
2. Scroll down to the **Metadata** section. Select **Edit**.

   For **Description**, enter *Identifies the refrigeration equipment operating in a store.*

   [![Screenshot of adding a metadata description to the relationship type.](media/tutorial-2-enrich-ontology/relationship-metadata.png)](media/tutorial-2-enrich-ontology/relationship-metadata.png#lightbox)

   Select **Update**.
3. Use the same steps that you used for the *Store operates Refrigeration Unit* relationship type to add the relationship type metadata described in the following table.

   | Relationship type name | Source > target entity type | Metadata |
   | --- | --- | --- |
   | *deliversTo* | Shipment > Store | **Description:** *Identifies the store receiving the shipment.* |
   | *occursAt* | Sale > Store | **Description:** *Identifies where the sale occurred.* |
   | *stockedAt* | Inventory > Store | **Description:** *Represents an active store assortment and its current inventory position, not merely a historical sale.* |
   | *originatesAt* | Shipment > Distribution Center | **Description:** *Identifies the distribution center sending the shipment.* |
   | *forProduct* | Sale > Product | **Description:** *Identifies the item sold.* |
   | *stockedAtProduct* | Product > Inventory | **Description:** *The item is part of the store's active assortment and has a current inventory position there.* |
   | *suppliedBy* | Product > Supplier | **Description:** *Identifies the supplier responsible for the items.* |
   | *contains* | Shipment > Product | **Description:** *Identifies the item being replenished.* |
   | *hasTelemetryReading* | Refrigeration Unit > Refrigeration Telemetry | **Description:** *Identified sensor telemetry readings for refrigeration units.* |

## Add rules

Next, add some business rules that give more detail about day-to-day operations. Write rules in natural language and link them to entity types, properties, and relationship types so consumers (like AI agents) can discover these rules and use them to ground their responses.

1. On the **Home** tab of the top ribbon, select **+ Add** > **Rule**.

   [![Screenshot of the Rule option in the Home ribbon's Add menu.](media/tutorial-2-enrich-ontology/rules.png)](media/tutorial-2-enrich-ontology/rules.png#lightbox)
2. Enter the following rule details:

   1. **Name:** Cold-chain exception
   2. **Definition:** *A frozen product has a cold-chain exception when the temperature of the refrigeration unit storing it remains above the productâs maximum storage temperature for more than 20 minutes.*
   3. **Linked ontology elements:** Frozen Product, Refrigeration Unit

   Under **Linked ontology elements**, select **+ Add**. In the **Add elements** dialog, select these two entity types and then select **Save**.

   [![Screenshot of configuring rule details.](media/tutorial-2-enrich-ontology/rules-configure.png)](media/tutorial-2-enrich-ontology/rules-configure.png#lightbox)
3. Select **Create**. In the **Explorer**, expand **Rules** and select **Cold-chain exception** to review the saved rule.

   [![Screenshot of the saved Cold-chain exception rule selected in the Explorer.](media/tutorial-2-enrich-ontology/rules-done.png)](media/tutorial-2-enrich-ontology/rules-done.png#lightbox)
4. Select **Home** > **+ Add** > **Rule** from the top ribbon to add more rules. Add two rules with the following details:

   | Name | Definition | Linked concepts |
   | --- | --- | --- |
   | Inventory at risk | *A store inventory position is at risk when projected on-hand inventory falls below safety stock before the next scheduled delivery* | - Store  - Inventory |
   | Late replenishment | *A replenishment shipment is late when its estimated arrival is more than four hours after its scheduled arrival.* | Shipment |

## Next steps

Your ontology is now enriched with additional metadata and business rules that give more context about day-to-day operations.

Next, continue to [Explore the ontology](tutorial-3-preview-ontology).

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
