---
title: "Calculate relative time periods"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/time-intelligence-functions/relative-time-periods](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/time-intelligence-functions/relative-time-periods) · Last updated on **2026-08-25**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Calculate relative time periods

Summarize this article for me

Use the functions in this section to retrieve data relative to the current day, month, quarter, or year. Planning supports relative time period functions that help you analyze historical and future data by selecting a specified number of preceding or following time periods.

## LASTNDAY

The *LASTNDAY* function returns a range of dates for the specified number of days preceding the current day. Use this function with the `SELECT.BYDATE` function and an aggregate function, such as `SUM` or `AVERAGE`, to retrieve and aggregate data over the returned date range.

### Syntax

```
LASTNDAY(number_of_days)
```

### Arguments

- `number_of_days`: The number of preceding days for which data is returned.

### Return value

Returns a range of dates for the specified number of preceding days.

### Example

```
LASTNDAY(45)
```

Returns the date range for the 45 days preceding the current day.

[![Screenshot of a Planning sheet with LASTNDAY function.](../../media/planning-reference-formulas/time-intelligence-functions/relative-time-periods/lastnday.png)](../../media/planning-reference-formulas/time-intelligence-functions/relative-time-periods/lastnday.png#lightbox)

## LASTNMONTH

The *LASTNMONTH* function returns a range of dates for the specified number of months preceding the current month. Use this function with the `SELECT.BYDATE` function and an aggregate function, such as `SUM` or `AVERAGE`, to retrieve and aggregate data over the returned date range.

### Syntax

```
LASTNMONTH(number_of_months)
```

### Arguments

- `number_of_months`: The number of preceding months for which data is returned.

### Return value

Returns a range of dates for the specified number of preceding months.

### Example

```
LASTNMONTH(15)
```

Returns the date range for the 15 months preceding the current month.

[![Screenshot of a Planning sheet with LASTNMONTH function.](../../media/planning-reference-formulas/time-intelligence-functions/relative-time-periods/lastnmonth.png)](../../media/planning-reference-formulas/time-intelligence-functions/relative-time-periods/lastnmonth.png#lightbox)

## LASTNQTR

The *LASTNQTR* function returns a range of dates for the specified number of quarters preceding the current quarter. Use this function with the `SELECT.BYDATE` function and an aggregate function, such as `SUM` or `AVERAGE`, to retrieve and aggregate data over the returned date range.

### Syntax

```
LASTNQTR(number_of_quarters)
```

### Arguments

- `number_of_quarters`: The number of preceding quarters for which data is returned.

### Return value

Returns a range of dates for the specified number of preceding quarters.

### Example

```
LASTNQTR(5)
```

Returns the date range for the 5 quarters preceding the current quarter. In the following example, it returns the sum of *Sales* from *2025 Q2* to *2026 Q2*, which represents the five quarters preceding the current quarter (*2026 Q3*).

[![Screenshot of a Planning sheet with LASTNQTR function.](../../media/planning-reference-formulas/time-intelligence-functions/relative-time-periods/lastnqtr.png)](../../media/planning-reference-formulas/time-intelligence-functions/relative-time-periods/lastnqtr.png#lightbox)

## LASTNYEAR

The *LASTNYEAR* function returns a range of dates for the specified number of years preceding the current year. Use this function with the `SELECT.BYDATE` function and an aggregate function, such as `SUM` or `AVERAGE`, to retrieve and aggregate data over the returned date range.

### Syntax

```
LASTNYEAR(number_of_years)
```

### Arguments

- `number_of_years`: The number of preceding years for which data is returned.

### Return value

Returns a range of dates for the specified number of preceding years.

### Example

```
LASTNYEAR(2)
```

Returns the date range for the 2 years preceding the current year.

[![Screenshot of a Planning sheet with LASTNYEAR function.](../../media/planning-reference-formulas/time-intelligence-functions/relative-time-periods/lastnyear.png)](../../media/planning-reference-formulas/time-intelligence-functions/relative-time-periods/lastnyear.png#lightbox)

## NEXTNDAY

The *NEXTNDAY* function returns a range of dates for the specified number of days following the current day. Use this function with the `SELECT.BYDATE` function and an aggregate function, such as `SUM` or `AVERAGE`, to retrieve and aggregate data over the returned date range.

### Syntax

```
NEXTNDAY(number_of_days)
```

### Arguments

- `number_of_days`: The number of following days for which data is returned.

### Return value

Returns a range of dates for the specified number of following days.

### Example

```
NEXTNDAY(45)
```

Returns the date range for the 45 days following the current day.

[![Screenshot of a Planning sheet with NEXTNDAY function.](../../media/planning-reference-formulas/time-intelligence-functions/relative-time-periods/nextnday.png)](../../media/planning-reference-formulas/time-intelligence-functions/relative-time-periods/nextnday.png#lightbox)

## NEXTNMONTH

The *NEXTNMONTH* function returns a range of dates for the specified number of months following the current month. Use this function with the `SELECT.BYDATE` function and an aggregate function, such as `SUM` or `AVERAGE`, to retrieve and aggregate data over the returned date range.

### Syntax

```
NEXTNMONTH(number_of_months)
```

### Arguments

- `number_of_months`: The number of following months for which data is returned.

### Return value

Returns a range of dates for the specified number of following months.

### Example

```
NEXTNMONTH(4)
```

Returns the date range for the 4 months following the current month. For example, if the current month is **July**, it returns the aggregated sales for **August**, **September**, **October**, and **November**.

[![Screenshot of a Planning sheet with NEXTNMONTH function.](../../media/planning-reference-formulas/time-intelligence-functions/relative-time-periods/nextnmonth.png)](../../media/planning-reference-formulas/time-intelligence-functions/relative-time-periods/nextnmonth.png#lightbox)

## NEXTNQTR

The *NEXTNQTR* function returns a range of dates for the specified number of quarters following the current quarter. Use this function with the `SELECT.BYDATE` function and an aggregate function, such as `SUM` or `AVERAGE`, to retrieve and aggregate data over the returned date range.

### Syntax

```
NEXTNQTR(number_of_quarters)
```

### Arguments

- `number_of_quarters`: The number of following quarters for which data is returned.

### Return value

Returns a range of dates for the specified number of following quarters.

### Example

```
NEXTNQTR(2)
```

Returns the date range for the two quarters following the current quarter.

[![Screenshot of a Planning sheet with NEXTNQTR function.](../../media/planning-reference-formulas/time-intelligence-functions/relative-time-periods/nextnqtr.png)](../../media/planning-reference-formulas/time-intelligence-functions/relative-time-periods/nextnqtr.png#lightbox)

## NEXTNYEAR

The *NEXTNYEAR* function returns a range of dates for the specified number of years following the current year. Use this function with the `SELECT` function and an aggregate function, such as `SUM` or `AVERAGE`, to retrieve and aggregate data over the returned date range.

### Syntax

```
NEXTNYEAR(number_of_years)
```

### Arguments

- `number_of_years`: The number of following years for which data is returned.

### Return value

Returns a range of dates for the specified number of following years.

### Example

```
NEXTNYEAR(2)
```

Returns the date range for the two years following the current year.

[![Screenshot of a Planning sheet with NEXTNYEAR function.](../../media/planning-reference-formulas/time-intelligence-functions/relative-time-periods/nextnyear.png)](../../media/planning-reference-formulas/time-intelligence-functions/relative-time-periods/nextnyear.png#lightbox)

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
