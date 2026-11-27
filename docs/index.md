---
title: What's new
---

# Fabric IQ: What's new

Changes to the [Microsoft Fabric IQ documentation](https://learn.microsoft.com/en-us/fabric/iq/), detected from each page's *Last updated on* date. Use the search box to look through the documentation history. Earlier reports are in the [Archive](reports/index.md).

_Last checked: 2026-11-27. A new report appears only when something changed._

## Report: 2026-11-27


**5 updated · 1 new · 0 removed** (of 331 pages)

## Updated pages

### Planning – [Fabric planning tutorial part 0: Introduction and environment setup](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-tutorial/planning/tutorial-0-introduction)
_Last updated 2026-10-01 → 2026-11-27_

- **Updated** [Prerequisites](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-tutorial/planning/tutorial-0-introduction#prerequisites) (+0/−4 lines): content removed or reworded

### Planning – [Set up writeback to persist data](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/planning-how-to-persist-data)
_Last updated 2026-09-16 → 2026-11-26_

- **Updated** [Prerequisites](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/planning-how-to-persist-data#prerequisites) (+1/−0 lines): - To use OneLake as the writeback destination, enable the corresponding tenant and workspace settings.
- **Updated** [Create a writeback destination](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/planning-how-to-persist-data#create-a-writeback-destination) (+7/−9 lines): Before writing back your planning data, configure a writeback destination, either OneLake or a Fabric SQL database.
- **New section** [Fabric SQL destination](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/planning-how-to-persist-data#fabric-sql-destination): To add a Fabric SQL destination, follow these steps: 1.
- **New section** [OneLake](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/planning-how-to-persist-data#onelake): To add a OneLake destination, enter the schema name and writeback table name.

### Planning – [Writeback FAQ](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/writeback-faq)
_Last updated 2026-08-31 → 2026-11-26_

- **Updated** [Can I write back to more than one destination from the same planning sheet?](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/writeback-faq#can-i-write-back-to-more-than-one-destination-from-the-same-planning-sheet) (+1/−0 lines): However, you can't write back to multiple types of destinations, such as OneLake and Fabric SQL, together.
- **Updated** [Can I write back to a destination outside of Fabric SQLâfor example, to a SharePoint list or an Excel file?](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/writeback-faq#can-i-write-back-to-a-destination-outside-of-fabric-sqlfor-example-to-a-sharepoint-list-or-an-excel-file) (+1/−3 lines): Planning in Fabric writes back either to Fabric SQL databases or to OneLake.
- **New section** [I don't see the OneLake option while configuring the writeback destination. How do I enable it?](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/writeback-faq#i-dont-see-the-onelake-option-while-configuring-the-writeback-destination-how-do-i-enable-it): To start using OneLake writebacks, you need to first enable the native planning engine through the tenant and workspace settings.

### Planning – [Save analysis and insights with bookmarks](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-add-bookmark)
_Last updated 2026-05-14 → 2026-11-26_

- **Updated** [Introduction](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-add-bookmark) (+2/−2 lines): Save analysis and insights with bookmarks Bookmarks help you capture the current state of your report, such as applied filters, rankings, layout adjustments, and formatti…
- **Updated** [Prerequisite](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-add-bookmark#prerequisite) (+1/−1 lines): - You have access to the plan item.
- **New section** [Save applied filters](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-add-bookmark#save-applied-filters): Instead of manually reapplying filters and toggling columns for every review, use bookmarks to preserve curated views of your data.
- **New section** [Capture top and bottom performers](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-add-bookmark#capture-top-and-bottom-performers): Instead of scanning through hundreds of rows to spot outliers, use ranking rules to isolate your top revenue drivers or underperforming accounts.
- **New section** [Highlight key metrics with formatting](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-add-bookmark#highlight-key-metrics-with-formatting): Use bookmarks to capture custom formatting and layout changes so critical variances and KPI thresholds stand out immediately.
- **New section** [Manage bookmark options](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-add-bookmark#manage-bookmark-options): Select More options (â¦) next to a bookmark to access the following actions: - Update: Overwrite the bookmark with your current report view and settings.
- **Removed section** “Create a bookmark”
- **Removed section** “Manage bookmarks”
- **Removed section** “Common scenarios for bookmarks”

### Planning – [Known limitations in planning](https://learn.microsoft.com/en-us/fabric/iq/plan/overview-limitations)
_Last updated 2026-10-29 → 2026-11-26_

- **Updated** [Writeback limitations](https://learn.microsoft.com/en-us/fabric/iq/plan/overview-limitations#writeback-limitations) (+1/−0 lines): - A planning sheet can't use OneLake and SQL database in Fabric writeback destinations simultaneously.
- **Updated** [Writeback cell limit](https://learn.microsoft.com/en-us/fabric/iq/plan/overview-limitations#writeback-cell-limit) (+2/−1 lines): Writeback to Fabric SQL supports up to 2.4 million cells.

## New pages

- **Planning** – [Migration to OneLake - Native planning engine in Fabric plan](https://learn.microsoft.com/en-us/fabric/iq/plan/onelake-enablement-tenant-setting) · 2026-11-26

---
Source: [Microsoft Learn – Fabric IQ](https://learn.microsoft.com/en-us/fabric/iq/). Content © Microsoft, CC BY 4.0.

