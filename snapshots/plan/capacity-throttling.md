---
title: "Capacity throttling in Fabric Planning"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/capacity-throttling](https://learn.microsoft.com/en-us/fabric/iq/plan/capacity-throttling) · Last updated on **2026-09-30**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Capacity throttling in Fabric Planning

Summarize this article for me

Capacity throttling can prevent the creation of a new session or the upgrade of an existing session. Existing sessions continue to work.

When capacity usage reaches its limit, users might see a capacity usage limit error when they open a plan item or perform an action that requires a higher session type.

## Understand capacity throttling scenarios

The following scenarios describe what happens when capacity is throttled.

### Start a new Viewer session

When a user who doesn't have an existing session opens a plan item while the capacity is throttled, the new Viewer session fails. The user can't view the plan item and sees a capacity usage limit error.

[![Screenshot of the capacity usage limit error when a new Viewer session can't start.](media/capacity-throttling/capacity-throttling-new-viewer-session.png)](media/capacity-throttling/capacity-throttling-new-viewer-session.png#lightbox)

## Understand session upgrade failures

When a user has an active session and performs an action that requires a higher session type, the session upgrade fails if the capacity is throttled. The following scenarios describe the session upgrade failures.

### Upgrade a Viewer session to a Stakeholder session

When a user has an active Viewer session and performs an action that requires a Stakeholder session, the session upgrade fails if the capacity is throttled. The user sees a capacity usage limit error.

[![Screenshot of the capacity usage limit error when a Viewer session can't upgrade to a Stakeholder session.](media/capacity-throttling/capacity-throttling-viewer-to-stakeholder-session.png)](media/capacity-throttling/capacity-throttling-viewer-to-stakeholder-session.png#lightbox)

### Upgrade a Stakeholder session to a Planner session

When a user has an active Stakeholder session and performs an action that requires a Planner session, the session upgrade fails if the capacity is throttled. The user sees a capacity usage limit error.

[![Screenshot of the capacity usage limit error when a Stakeholder session can't upgrade to a Planner session.](media/capacity-throttling/capacity-throttling-stakeholder-to-planner-session.png)](media/capacity-throttling/capacity-throttling-stakeholder-to-planner-session.png#lightbox)

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
