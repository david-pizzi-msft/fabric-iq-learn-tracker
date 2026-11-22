---
title: "Planning solutions with org apps"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/resources/how-to-create-org-apps](https://learn.microsoft.com/en-us/fabric/iq/plan/resources/how-to-create-org-apps) · Last updated on **2026-09-30**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Planning solutions with org apps

Summarize this article for me

Organizational apps provide a centralized experience for planning, analysis, and decision-making by bringing related content together in a single destination. With organizational apps, teams can access the plans they need, collaborate on planning activities, track progress, and review performance insights from one place.

Users can access plans, review analytics, submit updates, and track approvals without switching between different workspaces or applications. This approach simplifies navigation, promotes collaboration, and delivers a connected planning experience.

This article guides you through creating an organizational app that consolidates enterprise planning across forecasts, budgets, sales, and workforce data.

## Prerequisites

- Users must be an admin, member, or contributor to create org app items.
- Create the Fabric Plan items to bundle in the org app.
- In the **Home** ribbon, go to **Manage Connections** and create an **App Database** connection to enable collaboration on a Plan item in reading view.

[![Screenshot of the Manage Connections dialog with App Database Connection selected and a connection chosen.](../media/resources/how-to-create-org-apps/create-app-database-connection.png)](../media/resources/how-to-create-org-apps/create-app-database-connection.png#lightbox)

## Create an org app

Bundle multiple plan items, such as budget planning, forecasting, workforce planning, and sales planning, into an organizational app that's tailored to a specific business process or department.

1. Open your shared workspace and select **New Item** from the Workspace home page.
2. Select **Org app** from the **Distribute data** section.

   [![Screenshot of selecting a new Org App item.](../media/resources/how-to-create-org-apps/new-item-org-app.png)](../media/resources/how-to-create-org-apps/new-item-org-app.png#lightbox)
3. Enter the app name.
4. Select **Add Content** from the org apps homepage toolbar. Select the Fabric items to package into an org app and select **Add to app**.

   [![Screenshot of the select items dialog for adding plans, reports, and related items to an org app.](../media/resources/how-to-create-org-apps/add-content-select-items.png)](../media/resources/how-to-create-org-apps/add-content-select-items.png#lightbox)
5. The side pane shows the items you added. Select any plan item to view data and collaborate by updating forecasts and budgets.

   [![Screenshot of the side pane showing plan items added to the org app.](../media/resources/how-to-create-org-apps/plan-items-side-pane.png)](../media/resources/how-to-create-org-apps/plan-items-side-pane.png#lightbox)

## Add an overview page

An overview page in an org app serves as a centralized landing page that lists and organizes all the content included within the app such as reports, plans, and links. Create an overview page to give consumers an immediate, high-level map of all available content as soon as they open the app. You can have one overview page in an org app.

1. Select **Add** > **Overview**, and then enter the page name.

   [![Screenshot of the new overview page dialog with a page name field and create button.](../media/resources/how-to-create-org-apps/new-overview-page-name-dialog.png)](../media/resources/how-to-create-org-apps/new-overview-page-name-dialog.png#lightbox)
2. Add a title and description.

   [![Screenshot of adding a page title and description.](../media/resources/how-to-create-org-apps/add-overview-title-header.png)](../media/resources/how-to-create-org-apps/add-overview-title-header.png#lightbox)

   The following image shows the overview page:

   [![Screenshot of the Enterprise Planning overview page listing app elements like Finance Plan and Sales Plan.](../media/resources/how-to-create-org-apps/enterprise-planning-overview-page-elements.png)](../media/resources/how-to-create-org-apps/enterprise-planning-overview-page-elements.png#lightbox)

## Add navigation and folders

Organize and streamline your workspace navigation by grouping related items into dedicated sections, such as by department, project, or region. Add navigation to help end users quickly locate specific resources by expanding relevant sections rather than scanning through a long, unstructured menu.

1. Group related items into folders by adding a section. Select **Add** > **Section**, enter the name, and select **Create**.

   [![Screenshot of creating a navigation section.](../media/resources/how-to-create-org-apps/new-section-dialog-create-folder.png)](../media/resources/how-to-create-org-apps/new-section-dialog-create-folder.png#lightbox)
2. To move an item into a folder, hover over an item and select the **More options (...)** menu. Select **Move to section** and choose the section name.

   [![Screenshot of options to move items under a navigation section.](../media/resources/how-to-create-org-apps/move-item-section.png)](../media/resources/how-to-create-org-apps/move-item-section.png#lightbox)

   The following screenshot shows the navigation structure:

   [![Screenshot of the completed navigation bar with items grouped under sections.](../media/resources/how-to-create-org-apps/navigation-side-bar.png)](../media/resources/how-to-create-org-apps/navigation-side-bar.png#lightbox)

## Add links

By adding links to an organizational app, you can integrate relevant external resources, such as SharePoint sites, internal documentation, web portals, or supporting forms directly into the app's main navigation pane. Users can access complementary tools, reference guides, or external resources without leaving the app.

1. To add an external link, select **Add** > **Link**.
2. Enter the URL and link name. Then select whether to open the URL within the app or in a new browser tab.

   [![Screenshot of New link dialog with fields for link name, URL address, and link behavior options.](../media/resources/how-to-create-org-apps/add-link-configuration.png)](../media/resources/how-to-create-org-apps/add-link-configuration.png#lightbox)

   The following screenshot shows the link content accessed from within the app:

   [![Screenshot of an Excel workbook showing regional sales data accessed as a linked app resource.](../media/resources/how-to-create-org-apps/open-links-within-app.png)](../media/resources/how-to-create-org-apps/open-links-within-app.png#lightbox)

## View and share apps

1. Select **Preview app** to test the user interface, navigation, and layout before publishing.
2. After verifying your changes, select **Save**.
3. Access the org app from your workspace:

   [![Screenshot of Enterprise Planning Hub org app listed among workspace items.](../media/resources/how-to-create-org-apps/access-org-app-workspace.png)](../media/resources/how-to-create-org-apps/access-org-app-workspace.png#lightbox)
4. Select **Share** from the top-right corner to copy the app link and manage access.

   - Select **Copy link to this app** to share the org app item. Users who use the link you send must already have access.
   - Select **Link to this app page,** and users go directly to the item you have in view when copying the link.

   [![Screenshot of share menu options for an org app, including copy link, manage access, add person.](../media/resources/how-to-create-org-apps/share-options.png)](../media/resources/how-to-create-org-apps/share-options.png#lightbox)

   To learn more about sharing org apps, see [Sharing your Org App](/en-us/power-bi/explore-reports/org-app-items#granting-others-access-to-and-sharing-your-org-app).

## Related content

- Get started with [Org Apps](/en-us/power-bi/explore-reports/org-app-items).
- Manage [user access and permissions to org apps](/en-us/power-bi/explore-reports/org-app-items#managing-org-app-permissions-like-removing-users).
- Configure [audiences for Org Apps](/en-us/power-bi/explore-reports/org-app-items#add-users-and-groups-to-audiences).

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
