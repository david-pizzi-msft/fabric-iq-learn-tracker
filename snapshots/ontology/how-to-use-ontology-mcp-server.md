---
title: "Consume ontology (preview) as an MCP server"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-ontology-mcp-server](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-ontology-mcp-server) · Last updated on **2026-11-17**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Consume ontology (preview) as an MCP server

Summarize this article for me

Through the Model Context Protocol (MCP) server, AI systems can discover and interact with external tools in a structured way, extending beyond their own data and reasoning. Ontology (preview) can function as an MCP server, exposing an API so that external AI systems can interact with it through the MCP protocol. This capability helps integrate ontology into AI workflows.

Important

This feature is in [preview](../../fundamentals/preview).

Note

Due to a known issue, you can't currently use Service Principal to access the ontology MCP.

## Prerequisites

Before using ontology as an MCP server, make sure you have the following prerequisites:

- [A paid F2 or higher Fabric capacity](../../enterprise/fabric-features#feature-parity-list), or a [Power BI Premium per capacity (P1 or higher)](../../enterprise/licenses#workspace) capacity with [Microsoft Fabric enabled](../../admin/fabric-switch).
- **Users can create ontology (preview) items** and **Users can create Fabric items** [enabled on your Fabric tenant](overview-tenant-settings).
- An ontology (preview) item

## How it works

To create the MCP server endpoint, you need the URL of your ontology (preview) item.

To find the URL, follow these steps:

1. Open your ontology item in Fabric.
2. View the URL in the browser. The workspace ID follows `groups/`, and the ontology item ID follows `ontologies/`:

   ```
   https://app.fabric.microsoft.com/groups/<workspace-ID>/ontologies/<ontology-item-ID>
   ```

   Copy the values of `<workspace-ID>` and `<ontology-item-ID>`. If the URL includes extra path segments or query parameters, copy only the two IDs.
3. Form the **MCP server URL** by entering the copied values into this string: `https://api.fabric.microsoft.com/v1/mcp/dataPlane/workspaces/<workspace-ID>/items/<ontology-item-ID>/ontologyEndpoint`.

You use this **MCP server URL** in the next section.

## Setting up the MCP server in VS Code

1. Open **VS Code** and select a folder to work in.
2. Inside this folder, create a folder named **.vscode**.
3. Inside the inner folder, create a file called `mcp.json`.
4. VS Code automatically displays a blue **Add Server** button at the bottom right of the window.

   [![Screenshot showing the MCP server json file.](../../data-science/media/data-agent-mcp-server/include-mcp-json-vscode.png)](../../data-science/media/data-agent-mcp-server/include-mcp-json-vscode.png#lightbox)
5. Select **Add Server** and select **HTTP**. You're prompted to enter a URL. Use the **MCP server URL** that you copied in the previous section.

   [![Screenshot showing the selection of HTTP.](../../data-science/media/data-agent-mcp-server/include-mcp-server-select-http.png)](../../data-science/media/data-agent-mcp-server/include-mcp-server-select-http.png#lightbox)

   [![Screenshot showing to enter the URL for MCP server.](../../data-science/media/data-agent-mcp-server/include-mcp-server-url.png)](../../data-science/media/data-agent-mcp-server/include-mcp-server-url.png#lightbox)
6. Press **Enter** and provide a name for your MCP server. Use this name to display the MCP server in your VS Code environment.
7. VS Code attempts to authenticate with the server. Select **Allow** and sign in with your credentials.

The server is created.

[![Screenshot showing the MCP file of the ontology.](media/how-to-use-ontology-mcp-server/mcp-json.png)](media/how-to-use-ontology-mcp-server/mcp-json.png#lightbox)

## Enable agent mode

After adding the MCP server, enable **Agent Mode** in Visual Studio Code. In agent mode, VS Code acts as an orchestrator interface that connects your editor with MCP servers to interact with external tools like ontology. To enable it:

1. In VS Code, open chat (Ctrl + Shift + I).
2. Start the MCP server.

   [![Screenshot of starting the server in agent mode.](media/how-to-use-ontology-mcp-server/agent-mode-1.png)](media/how-to-use-ontology-mcp-server/agent-mode-1.png#lightbox)
3. Confirm that the server is running. Then, enter any prompts to activate the mode.

   [![Screenshot showing the running server and place for prompts in agent mode.](media/how-to-use-ontology-mcp-server/agent-mode-2.png)](media/how-to-use-ontology-mcp-server/agent-mode-2.png#lightbox)
4. When agent mode is active, select an **orchestrator** to handle your queries. Available orchestrators in public preview include **GPT-5, GPT-4.1, Claude Sonnet 4.5, Gemini 2.5 Pro**, and many more. The orchestrator manages the flow of information between your queries in VS Code and the ontology MCP server.

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
