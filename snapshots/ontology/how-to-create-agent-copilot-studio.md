---
title: "Build a Copilot Studio agent grounded in an ontology (preview)"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-create-agent-copilot-studio](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-create-agent-copilot-studio) · Last updated on **2026-09-29**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Build a Copilot Studio agent grounded in an ontology (preview)

Summarize this article for me

By using [Copilot Studio](/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio), business analysts, developers, and domain experts can create intelligent, enterprise-grade AI agents without extensive coding expertise. By combining natural language processing with your ontology (preview), you can build custom copilots that understand your organization's unique data structure and business context.

Important

This feature is in [preview](../../fundamentals/preview).

In this article, you:

1. Create a new agent in Copilot Studio.
2. Configure your agent to use ontology (preview) as a data source by connecting to an existing ontology.
3. Validate your agent's functionality by using the built-in **Test** pane.

After completing the steps in this article, you have a fully functional agent capable of answering business questions by using your ontology as a trusted, single source of truth.

## Prerequisites

Before you begin, make sure you have:

- An active **Copilot Studio production environment** with ontology MCP tools allowed.
- A Microsoft Fabric workspace that contains at least one ontology (preview) item, accessible through the OneLake catalog. For more information, see [Create ontology (preview) item](tutorial-1-create-ontology#create-ontology-preview-item).
- An Edge or Chrome browser, signed in with the same identity that has access to both the Copilot Studio environment and the Fabric workspace.

## Step 1: Sign in to your Copilot Studio production environment

1. Open **Copilot Studio**: <https://copilotstudio.microsoft.com/>.

[![Screenshot of Copilot Studio.](media/how-to-create-agent-copilot-studio/copilot-studio.png)](media/how-to-create-agent-copilot-studio/copilot-studio.png#lightbox)

## Step 2: Create a new agent

1. Select **Agents** from the left navigation bar and select **+ Create blank agent**.
2. Provide a unique name for your agent. The agent opens when it's ready.

[![Screenshot of Sales-Insight-Agent in Copilot Studio.](media/how-to-create-agent-copilot-studio/new-agent.png)](media/how-to-create-agent-copilot-studio/new-agent.png#lightbox)

## Step 3: Add Fabric IQ MCP tool

1. Select **Tools** from the tabs next to the agent name, and select **+ Add tool**.
2. Search for *Fabric IQ* and select **Fabric IQ MCP (Preview)**.

   [![Screenshot of Copilot Studio agent tools.](media/how-to-create-agent-copilot-studio/add-mcp-tool.png)](media/how-to-create-agent-copilot-studio/add-mcp-tool.png#lightbox)
3. Expand the dropdown menu next to **Connection** and select **Create new connection**.

   [![Screenshot of Copilot Studio agent tools connection, creating a new connection.](media/how-to-create-agent-copilot-studio/new-connection-1.png)](media/how-to-create-agent-copilot-studio/new-connection-1.png#lightbox)
4. Keep the default **Authentication type** of *Login with Microsoft Entra ID*.

   Enter the **Workspace ID** and **Ontology ID** of your existing ontology (preview) item. For more information on how to find these values, see [Use ontology MCP server](how-to-use-ontology-mcp-server#how-it-works). Select **Create**.

   [![Screenshot of Copilot Studio agent tools connection, adding the details.](media/how-to-create-agent-copilot-studio/new-connection-2.png)](media/how-to-create-agent-copilot-studio/new-connection-2.png#lightbox)
5. Select **Add** to finalize the connection.

   [![Screenshot of Copilot Studio agent tools connection, the connection is ready.](media/how-to-create-agent-copilot-studio/new-connection-3.png)](media/how-to-create-agent-copilot-studio/new-connection-3.png#lightbox)
6. Select the name **Fabric IQ MCP (Preview)** from the list of tools to open its details.

   Scroll down to verify that both **list\_ontology\_entity\_types** and **search\_ontology** are visible in the **Tools** section.

   [![Screenshot of Copilot Studio agent tools connection MCP tools.](media/how-to-create-agent-copilot-studio/tools.png)](media/how-to-create-agent-copilot-studio/tools.png#lightbox)

## Step 4: Query and test the agent

1. Open the **Test** pane by using the **Test** button in the top right corner of the screen. Enter a natural language question.
2. **Allow** the MCP tool when prompted.

   [![Screenshot of Copilot Studio agent chat.](media/how-to-create-agent-copilot-studio/allow.png)](media/how-to-create-agent-copilot-studio/allow.png#lightbox)
3. Select **Open connection manager** and **Connect**.

   [![Screenshot of Copilot Studio agent chat connection.](media/how-to-create-agent-copilot-studio/connection-manager.png)](media/how-to-create-agent-copilot-studio/connection-manager.png#lightbox)
4. Back in the **Chat** pane, select **Retry** and verify the response.

   [![Screenshot of Copilot Studio agent chat connection response.](media/how-to-create-agent-copilot-studio/response.png)](media/how-to-create-agent-copilot-studio/response.png#lightbox)

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
