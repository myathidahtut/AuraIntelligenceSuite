# Aura Intelligence Suite

A client-side business intelligence dashboard for retail transaction data. Upload one or more CSV exports and it parses, normalizes, and visualizes them entirely in the browser — no server, no upload of your data anywhere.

## Features

- **Multi-file CSV ingestion** — accepts several monthly exports at once and merges them into one dataset, with a tab per month plus an "All Months" view.
- **Adaptive column mapping** — matches common header variants (e.g. `Total_Amount`, `Revenue`, `Total_Sale`) so it works across differently-formatted exports without manual remapping.
- **KPIs**: total revenue, transaction count, and unique customer count for the selected period.
- **Charts**: revenue trend (seasonal vs. daily), transactions by hour of day, payment method breakdown, revenue by category, top products by volume, and average order value by category.
- **Top spenders leaderboard**, with anonymous/placeholder entries filtered out.

<img width="1200" height="412" alt="Dashboard overview" src="https://github.com/user-attachments/assets/ca9b91a8-97aa-483b-ae37-59d210871575" />
<img width="1267" height="631" alt="Category and payment breakdown" src="https://github.com/user-attachments/assets/b5678475-7da8-4799-949f-5716f94f80ec" />
<img width="1268" height="497" alt="Top products and AOV" src="https://github.com/user-attachments/assets/1decf27a-ccd1-4075-a9a5-e0206d19de7f" />

## Expected columns

The parser looks for these fields (or common aliases of them) in your CSV:

| Field | Type | Recognized aliases |
| :--- | :--- | :--- |
| `Purchase_ID` | string | `order_id`, `id` |
| `Purchase_Date` | date/time | `Timestamp`, `Order_Date`, `date` |
| `Total_Amount` | number | `Revenue`, `amount`, `Total_Sale`, `total` |
| `Quantity` | number | `quantity`, `Qty` |
| `Payment_Method` | string | `payment`, `Payment` |
| `Category_Name` | string | `Category`, `Merchant_Type` |
| `Stock_Name` | string | `Product`, `Item_Description` |
| `First_Name` | string | `Customer_Name`, `Client` |

## Tech stack

Vanilla HTML/CSS/JS, [PapaParse](https://www.papaparse.com/) for CSV parsing, and [Chart.js](https://www.chartjs.org/) for charts — all loaded via CDN, so there's no build step.

## Run it locally

No install required — it's a static page.

```bash
git clone https://github.com/myathidahtut/AuraIntelligenceSuite.git
cd AuraIntelligenceSuite
# open index.html in a browser
```
