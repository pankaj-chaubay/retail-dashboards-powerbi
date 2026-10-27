# Retail dashboards: Tableau to Power BI

Two dashboards I built in Tableau for my M.Sc. Data Analytics module "Visualization and Story Telling", rebuilt as Power BI projects with a proper data model and DAX measures.

| Dashboard | Data | Pages | Original |
|---|---|---|---|
| [Customer Behaviour](powerbi/CustomerBehaviour.pbip) | Retail customer orders, 15,250 rows, 2022-2024 (generated with Python for the assignment) | Customer overview · Category and region · Top customers and discount | [Tableau workbook](tableau-original/Customer%20Behaviour%20Dashboard.twb) · [Tableau Public](https://public.tableau.com/views/CustomerBehaviourDashboard_Final/CustomerDashboardCategoryRegion) |
| [Superstore Sales](powerbi/SuperstoreSales.pbip) | Sample Superstore, 9,994 order lines, 2014-2017 ([Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)) | Sales and profit overview · Product, segment and discount · Regional and customer insights | [Tableau workbook](tableau-original/Superstore%20Sales%20Dashboard.twb) |

Both reports have a year slicer. Every KPI compares the selected year with the year before, and clicking a chart filters the rest of the page.

## Open the reports

1. Install or update [Power BI Desktop](https://www.microsoft.com/power-platform/products/power-bi/desktop) (free).
2. Clone or download this repository.
3. Open `powerbi/CustomerBehaviour.pbip` or `powerbi/SuperstoreSales.pbip` and click **Refresh**. The data loads straight from the `data/` folder of this repository (parameter `DataSourceUrl`), so no local paths are needed.
4. If Desktop asks about privacy levels, choose **Public** for raw.githubusercontent.com.
5. The Superstore map needs **Options > Security > Use Map and Filled Map visuals** switched on.

The reports are saved as Power BI Projects (PBIP): the model is in TMDL and the report pages in the PBIR JSON format, so every measure and visual is readable and diff-able in Git.

## From Tableau to Power BI

| Tableau | Power BI |
|---|---|
| Parameter "Select year" | Disconnected table `Select Year` + measure `[Selected Year]` with `SELECTEDVALUE` |
| Calculated fields `Current Year (Sales)`, `Previous Year (Sales)` | Measures `[CY Sales]`, `[PY Sales]` using `CALCULATE` on the `Calendar` table |
| `% Diff Sales`, `% Diff Customer` | `[Sales vs PY %]`, `[Customers vs PY %]` with `DIVIDE` |
| `COUNTD(Customer ID)` and the FIXED LOD | `DISTINCTCOUNT` measures |
| Table calculation running sum (Pareto) | `[Cumulative Sales %]` over `ALLSELECTED` sub-categories |
| Top N filters (Top 10 customers, Top 10 states) | `RANKX` measures that return blank outside the top N, so the table hides those rows |
| Dashboard filter actions | Power BI cross-filtering between visuals |
| Story points | Page titles, subtitles and a "How to read this page" panel |

Data preparation is in [prep/prepare_data.py](prep/prepare_data.py): it writes UTF-8 CSVs with ISO dates so Power Query reads them the same way in any locale.

## Check the numbers

With the default year selected, the cards should show:

| Report | KPI | Value |
|---|---|---|
| Customer Behaviour (2024) | Customers | 4,964 (+3.2% on 2023) |
| | Sales | $5,206,538 (+1.1%) |
| | Profit | $1,046,620 (+1.7%) |
| | Sales per customer | $1,049 |
| | Return rate | 51.0% |
| Superstore (2017) | Sales | $733,215 (+20.4% on 2016) |
| | Profit | $93,439 (+14.2%) |
| | Profit margin | 12.7% |
| | Customers | 693 (+8.6%) |
| | Top state by sales | California $146,388 |

## Notes

- Retail customer data is synthetic, generated for the assignment, so trends are flat by design.
- Superstore is Tableau's public sample dataset.

Pankaj Chaubay · [LinkedIn](https://www.linkedin.com/in/pankaj-chaubay/) · [More projects](https://github.com/pankaj-chaubay)
