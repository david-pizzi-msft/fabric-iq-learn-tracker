---
title: "Time shifting"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/time-intelligence-functions/time-shifting](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/time-intelligence-functions/time-shifting) · Last updated on **2026-10-21**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Time shifting

Summarize this article for me

Planning supports time shifting functions that retrieve values from different time periods. These functions help you shift between time periods and access measure values for comparative and trend analysis.

## SHIFT

The *SHIFT* function returns a date by shifting a specified date forward or backward by a given time interval, such as months, quarters, or years.

### Syntax

```
SHIFT(inputDate, offset)
```

### Arguments

- `inputDate`: The date to shift.
- `offset`: Specifies the number of time intervals by which the date is shifted. Use a positive value to shift the date forward and a negative value to shift it backward. Supported interval formats include months (`M`), quarters (`Q`), and years (`Y`).

### Return value

Returns the date obtained by shifting the input date by the specified time interval.

### Examples

```
SHIFT(COLUMN.CURRENT_PERIOD, "2M")
```

Returns the date two months after the current period. For example, if the current period is **January**, the function returns the corresponding date in **March**.

[![Screenshot of the Formula Measure pane with SHIFT formula using COLUMN.CURRENT_PERIOD.](../../media/planning-reference-formulas/time-intelligence-functions/time-shifting/shift-current-period.png)](../../media/planning-reference-formulas/time-intelligence-functions/time-shifting/shift-current-period.png#lightbox)

Note

Set the **Data type** to **Date** when configuring the **`SHIFT`** function to view the shifted date. Otherwise, the function returns a **`#VALUE!`** error.

The following formula shifts each *Open Date* by two months. For example, if the *Open Date* is `05/22/2026`, the function returns `7/22/2026`.

```
SHIFT([Open Date], "2M")
```

[![Screenshot showing the SHIFT formula shifting Open Date by two months.](../../media/planning-reference-formulas/time-intelligence-functions/time-shifting/shift-date.png)](../../media/planning-reference-formulas/time-intelligence-functions/time-shifting/shift-date.png#lightbox)

You can also use the *SHIFT* function with forecast open and closed periods. For example, you can shift the forecast open period end date backward by two quarters.

```
SHIFT([Forecast].OPEN_END, "-2Q")
```

[![Screenshot showing the SHIFT formula shifting the forecast open period end date back two quarters in a planning sheet.](../../media/planning-reference-formulas/time-intelligence-functions/time-shifting/shift-forecast.png)](../../media/planning-reference-formulas/time-intelligence-functions/time-shifting/shift-forecast.png#lightbox)

## VALUEAT

The *VALUEAT* function returns the value of a measure at a specified time offset relative to the current reporting period.

### Syntax

```
VALUEAT(measure, offset)
```

### Arguments

- `measure`: The measure for which the value is returned.
- `offset`: Specifies the number of time intervals by which the value is shifted. Use a positive value to retrieve a value from a future period and a negative value to retrieve a value from a previous period. Supported interval formats include months (`M`), quarters (`Q`), and years (`Y`).

### Return value

Returns the value of the specified measure at the given time offset.

### Examples

```
VALUEAT([Sales], "-1M")
```

Returns the *Sales* value from the previous month.

[![Screenshot showing VALUEAT measure returning previous month Sales values.](../../media/planning-reference-formulas/time-intelligence-functions/time-shifting/valueat-previous-month.png)](../../media/planning-reference-formulas/time-intelligence-functions/time-shifting/valueat-previous-month.png#lightbox)

```
VALUEAT([Sales], "1Q")
```

Returns the *Sales* value from the next quarter.

[![Screenshot showing VALUEAT measure returning next quarter Sales values across 2025 and 2026 quarters.](../../media/planning-reference-formulas/time-intelligence-functions/time-shifting/valueat-next-quarter.png)](../../media/planning-reference-formulas/time-intelligence-functions/time-shifting/valueat-next-quarter.png#lightbox)

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
