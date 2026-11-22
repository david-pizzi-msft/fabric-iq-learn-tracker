---
title: "Plan projects with Gantt charts"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-how-to-create-gantt-chart](https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-how-to-create-gantt-chart) · Last updated on **2026-07-28**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Plan projects with Gantt charts

Summarize this article for me

The intelligence sheet features a best-in-class Gantt chart for Fabric that helps visualize, communicate, and track project progress. The fully customizable Gantt chart enables you to:

- Plan projects by breaking work into tasks with defined start and end dates.
- Identify task dependencies and anticipate potential delays.
- Assign resources to tasks and balance workloads across teams.
- Track key deliverables, approvals, and project milestones.

## Sample data

The data used to plot the Gantt chart in this article can be found in the Fabric Samples GitHub repository: [gantt-data.csv](https://github.com/microsoft/fabric-samples/tree/main/docs-samples/iq/plan/gantt-data.csv).

## Configure Gantt charts

Follow these steps to build a Gantt chart:

1. Add the Gantt visual to the canvas.
2. Assign data to the **Task**, **Start Date**, **End Date**, and **Progress** fields.
3. Select the drill down icon to display the task breakdown.

   [![Screenshot of the drill down icon and task breakdown.](media/intelligence-how-to-create-gantt-chart/drill-down.png)](media/intelligence-how-to-create-gantt-chart/drill-down.png#lightbox)
4. Assign the field that captures dependencies to the **Connect to** bucket. You see connector lines rendered between tasks that have dependencies.

   [![Screenshot of dependencies in the chart.](media/intelligence-how-to-create-gantt-chart/connect-to.png)](media/intelligence-how-to-create-gantt-chart/connect-to.png#lightbox)
5. Select the **Analytics** option and **Add new reference**. Capture phases or project sprints with reference lines or reference bands.
6. Set **Date(s)** to *first-of-date*. Change the **Name** and **Label** to *Project kick off*.
7. Change the line format to a dashed line. Select **Apply**. The chart should look like the following image:

   [![Screenshot of selecting Analytics from the menu ribbon.](media/intelligence-how-to-create-gantt-chart/analytics.png)](media/intelligence-how-to-create-gantt-chart/analytics.png#lightbox)
8. Select **Gantt Options > Data colors** to customize the colors, style, and border of the progress bars. You can also change the appearance of the connector lines.

   [![Screenshot of the Gantt customization options.](media/intelligence-how-to-create-gantt-chart/customize.png)](media/intelligence-how-to-create-gantt-chart/customize.png#lightbox)

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
