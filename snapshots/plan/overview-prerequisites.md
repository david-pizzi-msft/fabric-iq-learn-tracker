---
title: "Prerequisites for planning in Fabric"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/overview-prerequisites](https://learn.microsoft.com/en-us/fabric/iq/plan/overview-prerequisites) · Last updated on **2026-10-01**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Prerequisites for planning in Fabric

Summarize this article for me

This article lists all the required prerequisites, tenant settings, and capacity settings that must be configured to use planning in Fabric.

## Tenant settings

[Fabric administrators](../../admin/roles) can grant access to these settings in **OneLake catalog** > **Govern** > **Configurations** > [**Tenant settings**](../../admin/tenant-settings-index).

1. Under [Integration settings](../../admin/tenant-settings-index#integration-settings), enable **Allow XMLA endpoints and Analyze in Excel with on-premises semantic models**.

   ![Screenshot of enabling allow xmla endpoints and analyze in excel with on-premises semantic models.](media/overview-prerequisites/allow-xmla-endpoints.png)
2. For service principal-based authentication, enable [Service principals can call Fabric public APIs](../../admin/service-admin-portal-developer#service-principals-can-call-fabric-public-apis) under **Developer settings**.

   [![Screenshot of enabling service principals can call Fabric public APIs option.](media/overview-prerequisites/service-principal-calls.png)](media/overview-prerequisites/service-principal-calls.png#lightbox)

## Capacity settings

- Semantic models used in planning must be hosted on supported capacities, such as

  - **Power BI Premium capacities (P1, P2, and higher)**
  - **Microsoft Fabric capacities (F SKUs)**
- Planning scenarios that rely on XMLA endpoints require supported **Microsoft Fabric capacities (F SKUs)** or **Power BI Premium capacities (P1âP5)**. Power BI Pro and Power BI Premium Per User (PPU) aren't supported for these scenarios. Some lower-capacity SKUs can also have XMLA and memory limitations that prevent supported usage.
- In **OneLake catalog** > **Govern** > **Capacities**, ensure that the **XMLA Endpoint** setting is configured as **Read Only** or **Read Write**.

  ![Screenshot of setting xmla endpoints as read only or read write.](media/overview-prerequisites/set-xmla-read-only.png)

## Optional: Database connections

The following list contains optional database connections that you can configure to enable specific scenarios such as collaboration and writeback.

- Create and share a Fabric SQL database connection with report viewers so they can collaborate on the plan report. For more information, see [Create a database connection for collaboration](planning-how-to-create-database-connection).
- Create and configure a writeback destination if you want to write back the plan data. For more information, see [Create a writeback destination](planning-writeback/planning-how-to-persist-data#create-a-writeback-destination).

Note

During plan item creation, a Fabric SQL database is automatically created in your workspace. This database stores your plan report's metadata.

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
