---
title: "Define business metrics in ontology (preview)"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-metrics](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-metrics) · Last updated on **2026-11-09**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Define business metrics in ontology (preview)

Summarize this article for me

When you generate an ontology (preview) from a Power BI semantic model, the ontology surfaces the model's DAX measures under the corresponding ontology entities as *metrics*. A *metric* in ontology reflects the measures from the semantic model by keeping a link to the semantic model and pulling the original DAX expression on demand. This article shows how to view and work with metrics in ontology.

Important

This feature is in [preview](../../fundamentals/preview).

## Prerequisites

Before you view metrics, make sure you have the following prerequisites:

- A [Fabric workspace](../../fundamentals/create-workspaces) with a Microsoft Fabric-enabled [capacity](../../enterprise/licenses#capacity).
- **Ontology item (preview)** enabled on your tenant.
- A Power BI semantic model that contains one or more DAX measures.
- To view a measure's original DAX expression, **write** permission on the source semantic model. Without it, you can still see each measure's name, description, table, and source, but you can't pull the expression.

## How metrics work

One way to create an ontology is to [generate it from one or multiple semantic models](how-to-generate-from-semantic-models). Generating an ontology from a semantic model brings in the model's tables as entities, and its measures as *metrics*. Metrics are visible on ontology entities and have the following behavior:

- Each measure appears as a metric under the entity for the table you defined it on. Today the mapping is one entity to one table, even when a measure's DAX references multiple tables.
- Ontology metrics proxy measures instead of copying them. A metric stores a link to the source semantic model and retrieves the original DAX expression from the model when you request it.
- Anything you edit in the ontology, such as a metric description, stays in the ontology only, where agents can use it. It never changes the semantic model.

## Generate the ontology from a semantic model

1. From the semantic model, select **Generate ontology**, name the new ontology, and create it. Fabric connects to the semantic model and pulls its tables, columns, and relationships. For more information, see [Generate an ontology from a semantic model](how-to-generate-from-semantic-models).

   [![Screenshot of the generate-ontology progress connecting to a semantic model.](media/how-to-use-metrics/generate-ontology-progress.png)](media/how-to-use-metrics/generate-ontology-progress.png#lightbox)
2. When generation finishes, open the new ontology item and confirm that the tables appear as entities and the relationships connect them.

   [![Screenshot of a generated ontology model view showing tables as entities with relationships.](media/how-to-use-metrics/generated-model-view.png)](media/how-to-use-metrics/generated-model-view.png#lightbox)

## View metrics on an entity

1. Select an entity, and then select **Entity type > Open details**.

   [![Screenshot of Sales selected on the canvas with the Entity type tab available.](media/how-to-use-metrics/entity-type-details.png)](media/how-to-use-metrics/entity-type-details.png#lightbox)
2. Locate the **Metrics** section on the entity details page. It lists metrics based on measures in the semantic model behind this entity. Each metric shows a name, description, source semantic model, and table.

   [![Screenshot of the Metrics section listing metrics with their source semantic model and table.](media/how-to-use-metrics/metrics-grid.png)](media/how-to-use-metrics/metrics-grid.png#lightbox)

   Note

   The Metrics section is only visible if the entity has metrics coming from its semantic model source. If you don't see a Metrics section, the entity might not have any metrics.
3. Use the search, sort, and filter controls to find metrics by source semantic model or by table.

## View metric details

Select a metric to open its details. The details include the description, the source semantic model, and the table the metric applies to.

[![Screenshot of a single metric's details, including its DAX expression.](media/how-to-use-metrics/metric-details.png)](media/how-to-use-metrics/metric-details.png#lightbox)

You can perform these actions from the detail page:

- Edit the metric description when description editing is available. The metric formula is read-only in ontology. To change the DAX expression, edit the measure in the source semantic model.

  Note

  The ontology stores description changes locally, where agents use them; these changes don't modify the semantic model.
- Select **Resolve underlying DAX** to pull the original DAX expression from the semantic model. Viewing the original expression requires **write** permission on the source semantic model. The first pull is slower because Fabric fetches all measures; later ones load quickly.
- Select the **Source model** link to open the semantic model in a new tab.

## Refresh to see semantic model changes

Metrics don't update automatically. When a measure's DAX expression or description changes in the semantic model, refresh the ontology to see the updated metric value.

## Related content

- [Generate an ontology from a semantic model](how-to-generate-from-semantic-models)

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
