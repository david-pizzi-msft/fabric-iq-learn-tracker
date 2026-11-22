---
title: "Calculate ranking and quartiles"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/statistical-functions/calculate-ranking-quartiles](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/statistical-functions/calculate-ranking-quartiles) · Last updated on **2026-08-19**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Calculate ranking and quartiles

Summarize this article for me

Planning provides functions to rank values and calculate quartiles in a dataset. Use the functions in this section to determine the relative position of values and analyze the distribution of numerical data.

## QUARTILEINC

The *QUARTILEINC* function divides a set of numbers into four equal parts and returns the value for the specified quartile. The function uses the inclusive method, where the minimum and maximum values are included in the calculation.

### Syntax

```
QUARTILEINC(array, quart)
```

### Arguments

- `array`: The list or range of numeric values used to determine the quartile.
- `quart`: Specifies the quartile value to return.
  - `0`: Returns the minimum value.
  - `1`: Returns the first quartile (Q1), which represents the 25th percentile.
  - `2`: Returns the second quartile (Q2), which represents the median (50th percentile).
  - `3`: Returns the third quartile (Q3), which represents the 75th percentile.
  - `4`: Returns the maximum value.

### Return value

Returns the value corresponding to the specified quartile from the given set of numbers.

### Examples

```
QUARTILEINC(10,20,30,40,50,60,70,80,1)
```

Returns the first quartile (Q1) of the specified set of numbers. In this example, the function returns `25`.

```
QUARTILEINC(10,20,30,40,50,60,70,80,2)
```

Returns the second quartile (Q2), or median, of the specified set of numbers. In this example, the function returns `45`.

```
QUARTILEINC(10,20,30,40,50,60,70,80,3)
```

Returns the third quartile (Q3) of the specified set of numbers. In this example, the function returns `65`.

You can use the *QUARTILEINC* function to analyze the distribution of a dataset by dividing values into four equal parts for metrics such as sales, revenue, or performance scores.

[![Screenshot of a planning sheet with a QUARTILEINC function.](../../media/planning-reference-formulas/statistical-functions/calculate-ranking-quartiles/quartileinc.png)](../../media/planning-reference-formulas/statistical-functions/calculate-ranking-quartiles/quartileinc.png#lightbox)

### Excel equivalent

[QUARTILE.INC](https://support.microsoft.com/en-us/office/quartile-inc-function-1bbacc80-5075-42f1-aed6-47d735c4819d)

## QUARTILEEXC

The *QUARTILEEXC* function divides a set of numbers into four equal parts and returns the value for the specified quartile. The function uses the exclusive method, where the minimum and maximum values are excluded from the calculation.

### Syntax

```
QUARTILEEXC(array, quart)
```

### Arguments

- `array`: The list or range of numeric values used to determine the quartile.
- `quart`: Specifies the quartile value to return.
  - `1`: Returns the first quartile (Q1), which represents the 25th percentile.
  - `2`: Returns the second quartile (Q2), which represents the median (50th percentile).
  - `3`: Returns the third quartile (Q3), which represents the 75th percentile.

Note

The exclusive method supports only `1`, `2`, and `3` as valid quartile values. If any other value is specified, the *QUARTILEEXC* function returns a **`#VALUE!`** error.

### Return value

Returns the value corresponding to the specified quartile from the given set of numbers.

### Examples

```
QUARTILEEXC(10,20,30,40,50,60,70,80,1)
```

Returns the first quartile (Q1) of the specified set of numbers. In this example, the function returns `22.5`.

```
QUARTILEEXC(10,20,30,40,50,60,70,80,2)
```

Returns the second quartile (Q2), or median, of the specified set of numbers. In this example, the function returns `45`.

```
QUARTILEEXC(10,20,30,40,50,60,70,80,3)
```

Returns the third quartile (Q3) of the specified set of numbers. In this example, the function returns `67.5`.

You can use the *QUARTILEEXC* function to analyze the distribution of a dataset by dividing values into four equal parts for metrics such as sales, revenue, or performance scores.

[![Screenshot of a Planning sheet with QUARTILEEXC function.](../../media/planning-reference-formulas/statistical-functions/calculate-ranking-quartiles/quartileexc.png)](../../media/planning-reference-formulas/statistical-functions/calculate-ranking-quartiles/quartileexc.png#lightbox)

### Excel equivalent

[QUARTILE.EXC](https://support.microsoft.com/en-us/office/quartile-exc-function-5a355b7a-840b-4a01-b0f1-f538c2864cad)

## RANKEQ

The *RANKEQ* function returns the rank or position of a number in a set of numbers. The rank indicates the relative position of a number when the values are sorted in ascending or descending order. If duplicate values exist, they are assigned the same rank, and the subsequent rank is skipped.

### Syntax

```
RANKEQ(number, list, [order])
```

### Arguments

- `number`: The number whose rank is to be determined.
- `list`: The list or range of numbers used to determine the rank.
- `order` (optional): Specifies the sorting order for ranking.
  - If `order` is `0`, the values are ranked in descending order. The highest value is assigned a rank of `1`.
  - If `order` is omitted or any nonzero value is specified, the values are ranked in ascending order. The lowest value is assigned a rank of `1`.

### Return value

Returns the rank of the specified number in the given list of numbers.

### Examples

```
RANKEQ(2,[1,3,2,5,4],0)
```

Ranks the values in descending order. In this example, the function returns `4`.

```
RANKEQ(2,[1,3,2,5,4],1)
```

Ranks the values in ascending order. In this example, the function returns `2`.

```
RANKEQ(2,[1,3,2,5,4])
```

Ranks the values in ascending order by default. In this example, the function returns `2`.

```
RANKEQ(4,[1,2,2,5,4])
```

Returns the rank of the specified value when duplicate values exist. In this example, the function returns `4` because the duplicate values share the same rank, and the subsequent rank is skipped.

You can use the *RANKEQ* function to rank values based on metrics such as scores, costs, revenue, or sales.

[![Screenshot of a Planning sheet with RANKEQ function.](../../media/planning-reference-formulas/statistical-functions/calculate-ranking-quartiles/rankeq.png)](../../media/planning-reference-formulas/statistical-functions/calculate-ranking-quartiles/rankeq.png#lightbox)

### Excel equivalent

[RANK.EQ](https://support.microsoft.com/en-us/office/rank-eq-function-284858ce-8ef6-450e-b662-26245be04a40)

## RANKAVG

The *RANKAVG* function returns the rank or position of a number in a set of numbers. The rank indicates the relative position of a number when the values are sorted in ascending or descending order. If duplicate values exist, the function returns the average rank for those values.

### Syntax

```
RANKAVG(number, list, [order])
```

### Arguments

- `number`: The number whose rank is to be determined.
- `list`: The list or range of numbers used to determine the rank.
- `order` (optional): Specifies the sorting order for ranking.
  - If `order` is `0`, the values are ranked in descending order. The highest value is assigned a rank of `1`.
  - If `order` is omitted or any nonzero value is specified, the values are ranked in ascending order. The lowest value is assigned a rank of `1`.

### Return value

Returns the rank of the specified number in the given list of numbers. If duplicate values exist, the function returns the average rank for those values.

### Examples

```
RANKAVG(2,[1,2,2,5,4],0)
```

Ranks the values in descending order. In this example, the function returns `3.5`.

```
RANKAVG(2,[1,2,2,5,4],1)
```

Ranks the values in ascending order. In this example, the function returns `2.5`.

You can use the *RANKAVG* function to rank values based on metrics such as scores, costs, revenue, or sales, especially when duplicate values are expected and you want to assign them the average rank.

[![Screenshot of a Planning sheet with RANKAVG function.](../../media/planning-reference-formulas/statistical-functions/calculate-ranking-quartiles/rankavg.png)](../../media/planning-reference-formulas/statistical-functions/calculate-ranking-quartiles/rankavg.png#lightbox)

### Excel Equivalent

[RANK.AVG](https://support.microsoft.com/en-us/excel/functions/rank-avg-function)

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
