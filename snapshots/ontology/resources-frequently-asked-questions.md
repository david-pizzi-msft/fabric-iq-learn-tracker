---
title: "Ontology (Preview) Frequently Asked Questions"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/resources-frequently-asked-questions](https://learn.microsoft.com/en-us/fabric/iq/ontology/resources-frequently-asked-questions) · Last updated on **2026-10-05**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Ontology (Preview) Frequently Asked Questions

This article contains answers to frequently asked questions about ontology (preview).

## Does ontology (preview) support Eventstream?

Yes, you can bind data from Fabric Eventstream to ontology (preview) by landing that eventstream data in an eventhouse that is used as the ontology binding data source. For a walkthrough of this process, see the [ontology (preview) tutorial](tutorial-0-introduction).

## Does ontology (preview) support ontology management like versioning?

Yes, versioning is available in the ontology new experience. For more information, see [Manage version history in ontology (preview)](how-to-use-version-history).

## Does ontology (preview) support importing from industry-specific database templates from Azure Synapse?

No, import from industry-specific templates isn't currently available.

## What's the difference between ontology (preview) and graph in Microsoft Fabric?

While ontology (preview) integrates with [graph in Microsoft Fabric](../../graph/overview), they are distinct items that serve different purposes.

Ontology provides a semantic layer for your enterprise vocabulary that unifies meaning across domains and OneLake sources. It defines entity types, relationships, properties, rules, and constraints, and binds them to real data so that downstream tools share the same language. [Graph in Microsoft Fabric](../../graph/overview) is a graph solution that offers native graph storage and compute for nodes, edges, and traversals over connected data. It's good for path finding, dependency analysis, and graph algorithms.

Ontology (preview) works together with graph today. Ontology declares which things connect and why, and you can use graph to view your entity instances to learn more about the instantiated ontology and see patterns in the [entity type details](how-to-view-ontology-details).

For more about these items in Fabric IQ, see [What is Fabric IQ (preview)?](../overview#iq-as-a-workload-in-fabric)

## Submit Fabric ideas

If you have suggestions for new features that aren't currently part of ontology (preview), consider submitting them to [Fabric Ideas](https://community.fabric.microsoft.com/t5/Fabric-Ideas/idb-p/fbc_ideas). Use the idea label **IQ | Ontology**.

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
