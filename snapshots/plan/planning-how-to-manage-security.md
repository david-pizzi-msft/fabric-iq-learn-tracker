---
title: "Manage security in planning"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-manage-security](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-manage-security) · Last updated on **2026-11-24**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Manage security in planning

Summarize this article for me

Security provides centralized role-based access control across your entire plan item, so you can govern who can view, edit, and manage sheets, data, and features.

- Role-based access: Create custom roles with granular permission levels and assign one or more roles to users or groups.
- End-to-end coverage: Manage visibility and edit access across Planning, PowerTable, and Intelligence sheets. Configure PowerTable database security, and control feature permissions for Measures, Scenario, Writeback, Bookmarks, and Comments.
- Workspace governance: Control whether workspace contributors can modify security settings and sheet configurations.

In this article, you learn how to configure contributor security controls, create and manage roles, set permissions for each role, and assign roles to users.

## Configure security settings

To open the Security window, select **Security** from the toolbar. The **Security** page has two tabs: **General** and **Roles**.

- **General**: This tab includes options to [control workspace contributors' access](#manage-workspace-security-controls) to the overall security and governance settings of the current plan item. Use these options to specify whether all workspace contributors, selected contributors, or no contributors can manage security settings and sheet-related access configurations.
- **Roles**: This tab includes two sections for configuring security roles and assigning them to users:
  - **Users**: Use this section to [assign one or more configured security roles](#assign-roles-to-users) to users.
  - **Roles**: Use this section to [create and configure security roles](#create-a-role) by defining the permissions and access levels associated with each role.

## Manage workspace security controls

For a plan item, **the item owner**, **workspace admins**, and **members** can always edit its security and governance settings available in the **Security** tab. These settings include configuring security roles, assigning roles to users, managing access to planning features such as writeback and scenarios, configuring PowerTable database security, and more. Go to **Security** > **Security access** under the **General** tab to control whether workspace contributors can change security and governance settings and sheets-related access settings in the plan item.

[![Screenshot of security options for contributors.](media/planning-how-to-manage-security/workspace-contributors-access.png)](media/planning-how-to-manage-security/workspace-contributors-access.png#lightbox)

You can choose one of the following options:

- **Yes**: Allow all workspace contributors to manage security and governance settings and sheets in the plan item.
- **No**: Prevent workspace contributors from managing these settings and sheets.
- **Specific Contributors only**: Allow only selected workspace contributors to manage these settings and sheets. If you select this option, enter the email addresses of the contributors you want to authorize.

Select **Save** to apply the changes.

This setting controls access to all security settings on the **Security** window, including PowerTable configurations such as *Approvals*, *Row Access*, and *Column Access*, and planning features' access configurations such as *Approvals*, *Scenarios*, *Writeback*, and more.

## Create a role

Security roles define the permissions available to a group of users. Create multiple roles to provide different levels of access based on user responsibilities. After creating a role, assign it to one or more users.

Note

The **Item Baseline** role is created by default and applies to all users. You can configure common permissions in this role or create additional roles to provide different access levels for different groups of users.

1. In the **Security** window, select **Roles**.
2. Select **Add Roles**.
3. Enter a role name, and then select **Add**.

   [![Screenshot of creating a new role titled budget contributor.](media/planning-how-to-manage-security/create-new-role.png)](media/planning-how-to-manage-security/create-new-role.png#lightbox)
4. Configure the required permissions for the role from the **General** tab. For example, for a contributor role, you can grant Read + Write access to active planning sheets, set Intelligence dashboards to Read access, and hide restricted planning, PowerTable, and intelligence sheets so they remain invisible to users assigned to that role.

   The following table describes each permission:

   | Permission | Description |
   | --- | --- |
   | Read | Allows users assigned to the selected role to view the sheet but prevents them from making edits. |
   | Read + Write | Allows users assigned to the selected role to view and edit the sheet. |
   | Hidden | Hides the sheet from users assigned to the selected role, preventing them from accessing it. |

   [![Screenshot of assigning permissions for planning, intelligence, and powertable sheets.](media/planning-how-to-manage-security/assign-permissions-planning-powertable-intelligence-sheet.png)](media/planning-how-to-manage-security/assign-permissions-planning-powertable-intelligence-sheet.png#lightbox)
5. Configure bookmark security in your planning sheet to restrict access by role. Assign the specific bookmarks a role can access. Users assigned to that role will only see their permitted bookmarks. To learn more about bookmarks, see [Save Analysis with Bookmarks](planning-how-to-add-bookmark).

   [![Screenshot of selecting the bookmarks which can be accessed by the role.](media/planning-how-to-manage-security/bookmark-security-selection.png)](media/planning-how-to-manage-security/bookmark-security-selection.png#lightbox)
6. Select **Save Changes**.
7. After the role is created, assign it to users from the **Users** tab.
8. To rename a role, select the edit (pencil) icon and enter the new name.
9. To delete a role, select the delete (trash can) icon.

   Note

   The **Item Baseline** role is the default system role and can't be renamed or deleted.
10. After configuring users and roles, select **Back to Sheet** to return to the planning sheet.

## Configure planning sheet permissions

In the **Planning** tab, configure permissions for planning-specific features. The default permissions apply to all the planning sheets in the current plan item.

- **Measure (Data input and forecast) and scenario permissions**

| Permission | Description |
| --- | --- |
| **Hidden** | Hide measures and scenarios from users assigned to the selected role. |
| **Read** | Allows users to view values but prevents them from making changes. |
| **Read + Write** | Allows users to view and modify values. |

- **Comment permissions**

| Permission | Description |
| --- | --- |
| **View** | Users assigned to the selected role can view all comments in the planning sheet. |
| **Add** | Allows users to enter a new comment. |
| **Lock/Unlock** | Allows users to lock or unlock comment threads for editing. |
| **Star** | Users can emphasize important comments. |

- **Writeback permissions**

Allow users to write back planning data to OneLake or a Fabric SQL database.

[![Screenshot of access permission list for writeback, scenarios, measures, and comments.](media/planning-how-to-manage-security/default-access-permission-list.png)](media/planning-how-to-manage-security/default-access-permission-list.png#lightbox)

You can also set permissions specific to a particular planning sheet.

1. Select the **Select Sheet** button and choose the planning sheets to configure permissions.

   [![Screenshot of selecting the consolidated profitability planning sheet to configure feature-wise access.](media/planning-how-to-manage-security/select-specific-planning-sheet-assign-access.png)](media/planning-how-to-manage-security/select-specific-planning-sheet-assign-access.png#lightbox)
2. Use **Comment Access** permissions to determine whether users can perform actions such as creating or locking comment threads.
3. Disable the **Writeback Access** toggle to prevent users from writing back planning data.
4. To configure measure-level access, select the measures from the **Select Measure** list.

   [![Screenshot of selecting Sales Plan and Revenue Simulation measures.](media/planning-how-to-manage-security/select-measure-configure-access.png)](media/planning-how-to-manage-security/select-measure-configure-access.png#lightbox)
5. Configure access for each selected measure.

   [![Screenshot of assigning read, write, and hidden access to selected measures.](media/planning-how-to-manage-security/measure-permission-list.png)](media/planning-how-to-manage-security/measure-permission-list.png#lightbox)
6. Similarly, if you created scenarios, select a scenario to configure permissions.

   [![Screenshot of assigning read and write permissions to the price increase and market expansion scenarios.](media/planning-how-to-manage-security/scenario-permissions.png)](media/planning-how-to-manage-security/scenario-permissions.png#lightbox)

## Assign roles to users

After you configure one or more roles, assign them to users or groups to control their access to planning sheets and features.

To assign roles to users:

1. In the **Security** window, select **Users**.
2. Select **Assign Role**.
3. In the **Users or Groups** dropdown, select one or more users or Microsoft Entra ID groups.
4. In the **Roles** dropdown, select one or more roles. You can assign multiple roles to a user or group.
5. Select **Add**.

   [![Screenshot of assigning user groups to the executive viewer and budget contributor roles.](media/planning-how-to-manage-security/assign-roles-users.png)](media/planning-how-to-manage-security/assign-roles-users.png#lightbox)

## Permission precedence

When you assign multiple roles to a user, the union of permissions from all assigned roles determines the user's effective access. If different roles define different permission levels for the same feature, the user gets the highest level of access.

Consider the configured permissions for the *Member* and *Lead* roles in the planning security settings.

| Feature | Member | Lead |
| --- | --- | --- |
| **Measures** | Read + Write | Read |
| **Scenario** | Read + Write | Hidden |
| **Writeback** | No | Yes |
| **Comments** | View, Add | View, Add, Lock/Unlock, Star Comments |

Suppose a user is assigned both the **Member** and **Lead** security roles. The effective permissions for the user are as follows:

| Feature | Effective permission |
| --- | --- |
| **Measures** | Read + Write |
| **Scenario** | Read + Write |
| **Writeback** | Yes |
| **Comments** | View, Add, Lock/Unlock, Star Comments |

The user receives **Read + Write** access to **Measures** from the **Member** role and **Writeback** and advanced **Comments** permissions from the **Lead** role. The user receives the highest level of access available for each feature because planning considers permissions from all assigned roles.

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
