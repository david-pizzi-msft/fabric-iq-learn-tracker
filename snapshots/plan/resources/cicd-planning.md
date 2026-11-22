---
title: "CI/CD for planning in Fabric"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/resources/cicd-planning](https://learn.microsoft.com/en-us/fabric/iq/plan/resources/cicd-planning) · Last updated on **2026-10-27**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# CI/CD for planning in Fabric

Summarize this article for me

Use CI/CD (Continuous Integration and Continuous Deployment) to streamline the development and deployment of planning content across environments. Integrate planning artifacts into source control, validate changes, and deploy updates consistently from development to production while reducing manual effort and deployment errors.

Planning supports two key CI/CD capabilities: Git integration and deployment pipelines. These tools help manage planning items across development, test, and production environments by allowing individual items to be deployed, or multiple items to be deployed at once.

In addition, Planning supports using variables to dynamically manage semantic models, writeback destinations, and writeback connections across environments.

## Configure Git integration

Planning integrates with source control at the workspace level. You can commit all planning items in a workspace to a Git branch and version multiple planning items through a single process. The workspace structure, including folders, is preserved in the Git repository. Fabric supports source control through GitHub and Azure DevOps. For more information, see [Fabric Git Integration](/en-us/fabric/cicd/git-integration/git-get-started?tabs=azure-devops%2CAzure%2Ccommit-to-git).

1. Open the Fabric workspace to integrate with a Git repository.
2. Go to **Workspace Settings** and select **Git integration**.
3. Select your source control provider: **Azure DevOps** or **GitHub**.

   [![Screenshot of Fabric workspace Git integration settings showing Azure DevOps and GitHub as source control provider options.](../media/resources/cicd-planning/select-git-provider.png)](../media/resources/cicd-planning/select-git-provider.png#lightbox)
4. Enter the Azure DevOps or GitHub account and repository details. In this example, you choose GitHub.
5. Select **Connect**.
6. In the **Connect Git repository and branch** section, select an existing branch or create a new branch.

   [![Screenshot of selecting the branch and connecting to the repository.](../media/resources/cicd-planning/select-git-branch-connect.png)](../media/resources/cicd-planning/select-git-branch-connect.png#lightbox)
7. Select **Connect and Sync**.
8. Fabric displays the branch, sync status for each item, and the time of the last sync.

   [![Screenshot of a Fabric workspace showing the connected Git branch, sync status for each item, and last sync time.](../media/resources/cicd-planning/git-status-branch-commit.png)](../media/resources/cicd-planning/git-status-branch-commit.png#lightbox)

## Commit changes to the Git repository

When you make changes to an existing plan, delete a plan, or create a new plan, you must commit those changes to the Git repository linked to the workspace. The status of modified items changes to *Uncommitted*.

1. Select the **Source control** option.

   [![Screenshot of source control highlighted.](../media/resources/cicd-planning/source-control.png)](../media/resources/cicd-planning/source-control.png#lightbox)
2. Select the **Changes** tab from the **Source control** side pane. This tab displays all the items you changed, with an icon indicating the status: **New**, **Modified**, **Conflict**, or **Deleted**.
3. Select the items to commit to the Git repository and add an optional commit message. Select **Commit**.

   [![Screenshot of selecting changed plans in the Changes tab and selecting Commit to push them to the GitHub repository.](../media/resources/cicd-planning/commit-selected-plans-github.png)](../media/resources/cicd-planning/commit-selected-plans-github.png#lightbox)
4. After the selected items are committed to the Git repository, Fabric removes them from the list. The item status changes to *Synced,* and the status bar displays the latest commit.

   [![Screenshot of status changing to synced for committed items in the workspace.](../media/resources/cicd-planning/committed-items-status-change-workspace.png)](../media/resources/cicd-planning/committed-items-status-change-workspace.png#lightbox)

## Deploy planning items to other workspaces

Create a deployment pipeline to promote plan items from development to test and production workspaces. To learn more about deployment pipelines in Fabric, see [Introduction to deployment pipelines](/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines?tabs=new-ui).

Fabric's lineage view helps you track item dependencies. When the plan and semantic model reside in the same workspace and deployment pipeline, deploy the semantic model to the target workspace at least once, either before or together with the plan. This step establishes the connection to the semantic model in the target workspace. For semantic models in other workspaces, follow the stand-alone or separate-pipeline scenarios in the next section.

[![Screenshot of lineage view showing the plan connected to the semantic model in the source workspace.](../media/resources/cicd-planning/source-workspace-plan-item-lineage.png)](../media/resources/cicd-planning/source-workspace-plan-item-lineage.png#lightbox)

The following steps describe how to deploy a plan when the plan and semantic model reside in the same workspace and are part of the same deployment pipeline.

1. Commit your plan and semantic model to the Azure DevOps or GitHub repository connected to the workspace.
2. Create a new deployment pipeline, define the pipeline stages, and assign the designated workspaces to each stage.
3. Select the target stage, such as Test or Production, to deploy your planning item. **Deploy from** is automatically set to the previous stage in the pipeline (For example, Development when deploying to Test). Select the plan, the Fabric SQL app DB, and the related semantic model to deploy to the next stage.

   Note

   - The \_\_fabric\_plan\_sys SQL database stores metadata for data inputs, comments, writeback destinations, user access, and more. Deploy it once during your first deployment. It doesn't need to be redeployed in subsequent updates.
   - To deploy your plan, the semantic model used in the plan must already exist in the target stage or be selected for deployment along with the planning item.

   [![Screenshot of selecting the plan, semantic model, and database for deployment.](../media/resources/cicd-planning/select-plan-database-model-deploy.png)](../media/resources/cicd-planning/select-plan-database-model-deploy.png#lightbox)
4. Select **Deploy** and verify the source and target stages and the items selected for deployment. Verify that the deployment is successful from the **Deployment history** pane.

   [![Screenshot of verifying the source and target stages and selected items before deploying the plan.](../media/resources/cicd-planning/deployment-pipeline-verify-source-target-stages-items.png)](../media/resources/cicd-planning/deployment-pipeline-verify-source-target-stages-items.png#lightbox)
5. Open the target workspace and refresh the semantic model.

   [![Screenshot of refreshing the semantic model in the target workspace.](../media/resources/cicd-planning/refresh-semantic-model-target-workspace.png)](../media/resources/cicd-planning/refresh-semantic-model-target-workspace.png#lightbox)
6. Open the plan in the target workspace. Fabric automatically retains the semantic model connection and loads the data.

   [![Screenshot of plan connecting to semantic model from the target workspace.](../media/resources/cicd-planning/plan-semantic-model-connection-data-loaded.png)](../media/resources/cicd-planning/plan-semantic-model-connection-data-loaded.png#lightbox)

## Deploy planning items with stand-alone semantic models

If your semantic model resides in a separate workspace outside any deployment pipeline, you only need to deploy the plan from your source workspace to the target workspace. Fabric automatically preserves the connection to the stand-alone semantic model in the target workspace.

[![Screenshot of plan item lineage showing its connection to a semantic model in a separate stand-alone workspace.](../media/resources/cicd-planning/item-lineage-stand-alone-semantic-model.png)](../media/resources/cicd-planning/item-lineage-stand-alone-semantic-model.png#lightbox)

1. Commit your plan to the Azure DevOps or GitHub repository connected to the workspace.
2. Open the deployment pipeline connected to the workspace. Select the plan and deploy it to the target workspace.

   [![Screenshot of deploying the plan item to the target workspace.](../media/resources/cicd-planning/standalone-deploy-plan.png)](../media/resources/cicd-planning/standalone-deploy-plan.png#lightbox)
3. Once you deploy the plan to the target workspace, Fabric automatically connects it to the semantic model in the stand-alone workspace and loads the data.

   [![Screenshot of the deployed plan connected to the semantic model in the stand-alone workspace.](../media/resources/cicd-planning/standalone-plan-connected-semantic-model.png)](../media/resources/cicd-planning/standalone-plan-connected-semantic-model.png#lightbox)

## Deploy planning items by using models from a different deployment pipeline

If your semantic model and plan are part of different pipelines, deploy them individually. For automatic binding, both pipelines must have the same number of stages, and the source plan and semantic model must occupy stages at the same numeric position; matching stage names alone isn't sufficient. First deploy the semantic model to the corresponding target stage in its own deployment pipeline, then deploy the plan. For more information, see [Autobinding across workspaces](../../../cicd/deployment-pipelines/understand-the-deployment-process#autobinding-across-workspaces).

To demonstrate this scenario, consider a planning item named *Plan\_2* created in the *Plan Docs* workspace.

- *Plan\_2* connects to the *Enterprise - Sales Transactions* semantic model in the *Org Semantic Models* workspace.
- *Plan\_2* is part of the *DP\_Fabric\_Planning* deployment pipeline.
- The *Org Semantic Models* workspace is part of a different deployment pipeline - *semantic\_model\_pipeline*.

[![Screenshot of plan and semantic models in different workspaces.](../media/resources/cicd-planning/plan-semantic-model-different-workspaces-pipelines.png)](../media/resources/cicd-planning/plan-semantic-model-different-workspaces-pipelines.png#lightbox)

1. Commit the semantic model and plan to the Git repository connected to their respective workspaces.
2. As the semantic model is in a different workspace and pipeline, use its own deployment pipeline to deploy it to the target stage.

   [![Screenshot of deploying the semantic model to the target stage using its own deployment pipeline.](../media/resources/cicd-planning/semantic-model-pipeline-deploy-target-stage.png)](../media/resources/cicd-planning/semantic-model-pipeline-deploy-target-stage.png#lightbox)
3. After the semantic model is successfully deployed, open the target workspace and refresh the semantic model.

   [![Screenshot of refreshing the semantic model after deploying to the target environment.](../media/resources/cicd-planning/semantic-model-refresh-target-workspace.png)](../media/resources/cicd-planning/semantic-model-refresh-target-workspace.png#lightbox)
4. Promote the plan to the next stage by using its dedicated deployment pipeline.

   [![Screenshot of deploying the plan using the DP_Fabric_Planning pipeline.](../media/resources/cicd-planning/semantic-model-different-pipeline-promote-plan.png)](../media/resources/cicd-planning/semantic-model-different-pipeline-promote-plan.png#lightbox)
5. Open the plan in the target workspace. Although the semantic model is in a different workspace, the plan seamlessly connects to the semantic model and loads data.

   [![Screenshot of a plan in the target workspace connecting to and loading data from a semantic model in a different workspace.](../media/resources/cicd-planning/semantic-model-diff-pipeline-target-workspace-plan.png)](../media/resources/cicd-planning/semantic-model-diff-pipeline-target-workspace-plan.png#lightbox)

## Use variable libraries to connect to semantic models

Create variables to dynamically assign the semantic model the plan uses across different environments. To learn more about variable libraries, see [Variable library overview](/en-us/fabric/cicd/variable-library/variable-library-overview).

For demonstration purposes, consider a deployment pipeline with three stages. In the dev and test stages, the plan connects to the same semantic model. In the prod workspace, the plan connects to another semantic model.

[![Screenshot of a deployment pipeline with Development, Test, and Production stages.](../media/resources/cicd-planning/deployment-pipeline-stages.png)](../media/resources/cicd-planning/deployment-pipeline-stages.png#lightbox)

1. Create a variable library in the workspace assigned to the first stage of the deployment pipeline. In this example, the *Plan Docs* workspace.
2. Add a new variable and set the type to **Item reference**. Select the semantic model from the development (first pipeline stage) workspace as the **Default value set.**

   [![Screenshot of creating an item reference variable for the semantic model.](../media/resources/cicd-planning/create-variable-dev-semantic-model.png)](../media/resources/cicd-planning/create-variable-dev-semantic-model.png#lightbox)
3. Select **Add value set**, then select the semantic model for the target stage (for example, UAT or production). In this example, you assign the *Enterprise - Txn - PROD* semantic model to the production environment. Repeat this step to configure different semantic models for additional stages as needed.

   [![Screenshot of configuring an alternate value set to hold the semantic model for production.](../media/resources/cicd-planning/variable-library-alternate-value-set-production.png)](../media/resources/cicd-planning/variable-library-alternate-value-set-production.png#lightbox)
4. Create a new plan item and select the **Variable Library** option when you connect to the semantic model. Select the variable you configured in steps 2 and 3.

   [![Screenshot of selecting the variable option to connect to a semantic model.](../media/resources/cicd-planning/select-variable-option-semantic-model.png)](../media/resources/cicd-planning/select-variable-option-semantic-model.png#lightbox)
5. Commit the variable library and plan item to the configured Git repository.
6. Deploy the variable library to the next stage (test) in the pipeline.
7. In this example, you use the same semantic model in the test stage, so you don't need to update the variable library after migrating to test - it uses the same active set as development. Deploy the plan item after the variable library is successfully deployed.
8. Deploy the variable library to the target stage (for example, production). If that stage requires a different semantic model, open the variable library in the target workspace (for example, *Plan Docs [PROD]*), set the target value set that contains the required values as active, and save your changes. In this example, you set the *PROD* value set to active.

   [![Screenshot of setting the alternate value set for PROD as the active set.](../media/resources/cicd-planning/variable-library-set-prod-value-set-active.png)](../media/resources/cicd-planning/variable-library-set-prod-value-set-active.png#lightbox)
9. Migrate the plan to the target environment.
10. Open the plan in the target (*Plan Docs [PROD]*) workspace. It automatically connects to the semantic model designated as the active set in the variable library.

    [![Screenshot of the plan in the production workspace automatically connecting to the semantic model set active in the variable library.](../media/resources/cicd-planning/plan-target-workspace-semantic-model.png)](../media/resources/cicd-planning/plan-target-workspace-semantic-model.png#lightbox)

## Migrate writeback destinations

To migrate the Fabric SQL writeback destination database, see [SQL database source control integration in Microsoft Fabric](/en-us/fabric/database/sql/source-control).

The deployment preserves the writeback destination configuration, but the generated target table name initially appears as a system-generated ID. You can manually rename the table and execute writeback.

[![Screenshot of the writeback destination showing a system-generated ID as the target table name after deployment.](../media/resources/cicd-planning/writeback-deployment-table-id.png)](../media/resources/cicd-planning/writeback-deployment-table-id.png#lightbox)

- **Writeback logs**: Execution logs from the source workspace don't transfer to the target workspace. Any writeback activity in the target workspace logs as a new, independent event.
- **Auto-Writeback and baselining**: If Auto-Writeback is enabled, the initial writeback attempt in the target workspace fails when you update cell values. This failure occurs because baseline data isn't established. To resolve this problem, perform a manual writeback in the target workspace first. Subsequent Auto-Writeback operations function normally.

## Use variables for writeback destinations and connections

Using variables for writeback connections and SQL destinations simplifies environment management across CI/CD stages like Dev, Test, and Prod. Instead of manually reconfiguring database settings in each workspace after deployment, variables dynamically route data to the correct database based on the active set in the variable library.

1. In the variable library, create two variables:

   - An **Item Reference** variable to store the writeback destination database.
   - A **Connection Reference** variable to store the database connection.

   [![Screenshot of creating an item variable and connection reference for writeback.](../media/resources/cicd-planning/writeback-cicd-variable-library.png)](../media/resources/cicd-planning/writeback-cicd-variable-library.png#lightbox)
2. For each target stage, configure a value set with the writeback database item reference and connection reference for that environment.
3. Open your planning or sheet or matrix visual in an intelligence sheet and configure the writeback destination. In the connection dropdown, select **Use Variable** and select the connection reference variable created in the variable library.

   [![Screenshot of selecting Use Variable and the connection reference variable in the writeback destination connection dropdown.](../media/resources/cicd-planning/writeback-cicd-select-connection-variable.png)](../media/resources/cicd-planning/writeback-cicd-select-connection-variable.png#lightbox)
4. Set **Select Database From** to **Variable Library**, then select the database item reference variable created in the variable library.

   [![Screenshot of selecting the item reference variable that holds the writeback database name.](../media/resources/cicd-planning/writeback-cicd-select-database-variable.png)](../media/resources/cicd-planning/writeback-cicd-select-database-variable.png#lightbox)
5. Deploy the variable library to the target stage. In the target workspace, select the required value set as active and save the library.
6. Deploy the plan to the target stage. Before executing writeback, verify that the active value set references the intended target database and connection. When you deploy the plan to other stages in the deployment pipeline, the writeback configuration automatically fetches from the active set for that stage in the variable library.

## Related content

- Get started with [CI/CD in Fabric](/en-us/fabric/cicd/cicd-overview).
- Create [variable libraries](/en-us/fabric/cicd/variable-library/variable-library-overview).
- Introduction to [writeback in planning](/en-us/fabric/iq/plan/planning-writeback/planning-how-to-persist-data).

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
