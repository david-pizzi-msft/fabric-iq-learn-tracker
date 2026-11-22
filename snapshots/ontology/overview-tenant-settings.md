---
title: "Required tenant settings for ontology (preview)"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/overview-tenant-settings](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview-tenant-settings) · Last updated on **2026-10-01**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Required tenant settings for ontology (preview)

Summarize this article for me

Before you can use all the features of ontology (preview), you must enable certain settings on your Fabric tenant. This article describes required and optional tenant settings for using ontology.

Important

This feature is in [preview](../../fundamentals/preview).

[Fabric administrators](../../admin/roles) can grant access to these settings in **OneLake catalog** > **Govern** > **Configurations** > [**Tenant settings**](../../admin/tenant-settings-index).

## Users can create Fabric items

This setting is **required** to create ontology (preview) items with the new experience: *Users can create Fabric items*.

[![Screenshot of enabling Fabric items in the admin portal.](media/overview-tenant-settings/prerequisite-fabric-items.png)](media/overview-tenant-settings/prerequisite-fabric-items.png#lightbox)

If you don't enable this setting, you get errors when creating a new ontology item, including while [migrating from the old experience to the new experience](overview#migrate-from-old-experience).

## Users can create ontology (preview) items

This setting is **required** to create ontology (preview) items: *Users can create ontology (preview) items*.

[![Screenshot of enabling ontology in the admin portal.](media/overview-tenant-settings/prerequisite-ontology.png)](media/overview-tenant-settings/prerequisite-ontology.png#lightbox)

If you don't enable this setting, you get errors when creating a new ontology item.

## Data agent tenant settings

If you want to use ontology (preview) with a Fabric data agent, make sure to configure the required [Fabric data agent tenant settings](../../data-science/data-agent-tenant-settings).

If you don't enable these settings, you might see errors when creating a new data agent item.

## Operations agent tenant settings

If you want to use ontology (preview) with a Fabric operations agent, make sure to configure the tenant settings listed in the [Fabric operations agent prerequisites](../../real-time-intelligence/operations-agent#prerequisites).

If you don't enable these settings, you might see errors when creating a new operations agent item.

## Next steps

Now that your tenant is ready to work with ontology (preview), get started with the [Ontology (preview) tutorial](tutorial-0-introduction).

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
