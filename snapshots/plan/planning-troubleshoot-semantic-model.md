---
title: "Troubleshoot common issues in planning"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-troubleshoot-semantic-model](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-troubleshoot-semantic-model) · Last updated on **2026-10-01**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Troubleshoot common issues in planning

Summarize this article for me

This article provides troubleshooting guidance for some of the common issues you might face while working in Fabric Planning. For information about known limitations, see [Known limitations in planning](overview-limitations).

## Semantic model not found

### Cause

The semantic model linked to the plan item can't be found. It might have been moved, renamed, or deleted.

### Resolution

1. Verify that the semantic model exists in the required workspace in Microsoft Fabric.
2. If it got moved, locate the new workspace and connect to it.

## Insufficient semantic model permissions

If you see error code `SM_CONN_1003`, the error indicates that you don't have sufficient permissions on the semantic model.

To attach a semantic model to a plan, ensure that you have both *Read* and *Build* permissions on the semantic model. If you only need to read data from a semantic model that is already connected to a plan, *Read* permission is sufficient.

### Resolution

Ask the semantic model administrator to grant you *Read* and *Build* permissions on the semantic model, and then try attaching the semantic model to the plan again.

## Related content

To learn more about other error codes and resolutions, see [Error codes and resolutions](resources/error-codes-and-resolutions).

## Shared cloud connection expired

### Cause

The shared cloud connection credentials you created for SQL database in Fabric expired.

### Resolution

The connection owner must reauthenticate the connection by following these steps:

1. In Microsoft Fabric **Home**, go to **Settings > Manage connections and gateways**.
2. Locate the connection, select **More actions** (`Â·Â·Â·`), then **Settings**.
3. Select **Edit credentials**, reauthenticate, and then select **Save**.
4. Return to the artifact and retry the connection.

## When a shared plan item isn't accessible to a user outside the workspace

### Cause

Users who aren't members of the workspace can't access a shared plan item.

### Resolution

Ensure that you followed all the steps explained in this article: [Share a plan item with users outside the workspace](sharing-plan-artifact).

This article explains how to share a plan item with a user who isn't a member of the workspace by using item sharing, specifically focusing on granting access to the semantic model associated with the plan.

## User can't access Fabric SQL data in PowerTable due to insufficient permissions

A user might be unable to access the database or retrieve table and schema information even when the database is shared with the user with **Read all data** permission.

### Cause

PowerTable supports database-level row-level security (RLS). When you share the database with a user, the user can access the database data but might not have explicit permission to read system information, such as the available schemas and tables. PowerTable requires access to this system information to perform lookups. As a result, when you share the table app with the user, they might be unable to view the database data.

### Resolution

Grant the user the required database-level access by using one of the following methods.

#### Option 1: Grant SELECT permission

Run the following query in the corresponding Fabric SQL database:

```
GRANT SELECT TO [mailId];
```

Replace `[mailId]` with the email address of the user to share the PowerTable app with.

#### Option 2: Add the user to the `db_datareader` role

1. In the Fabric SQL database, go to **Security** > **Manage SQL security**.
2. Select **`db_datareader`** role.
3. Select **Manage access**.
4. Add the user to the role.

[![Screenshot of Fabric SQL database Manage SQL security pane with db_datareader role selected and Manage access button highlighted.](media/planning-troubleshoot-semantic-model/manage-sql-security.png)](media/planning-troubleshoot-semantic-model/manage-sql-security.png#lightbox)

After you grant the required access, the user can access the database schema and table information that PowerTable needs.

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
