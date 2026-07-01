# Aura Intelligence Suite

> A premium, client-side business intelligence dashboard engineered for dynamic cross-client ledger ingest, schema normalization, and interactive transaction forensics.

[![Stack](https://img.shields.io/badge/Architecture-Vanilla%20JavaScript-f7df1e?style=flat-square)]()
[![Engine](https://img.shields.io/badge/Parsing-PapaParse%20v5.4-ff6b6b?style=flat-square)]()
[![Charts](https://img.shields.io/badge/Visualization-Chart.js%20v4-2c3e50?style=flat-square)]()
[![Design](https://img.shields.io/badge/Aesthetic-Minimalist%20Luxury-b89047?style=flat-square)]()

Aura Intelligence Suite is an executive-level single-page web application (SPA) designed to parse, reconcile, and visualize disparate retail transaction archives. Built purely with high-performance vanilla JavaScript, the system processes large-scale CSV files locally on the client's browser—ensuring absolute data privacy, zero server overhead, and near-instant computational rendering.

---

## 📊 Core Analytical Features

### 1. Unified Ledger Ingestion & Temporal Navigation
* **Parallel Archive Parsing:** Accepts multiple CSV transactional ledgers concurrently, seamlessly consolidating multi-month matrix records.
* **Dynamic Tab Generation:** Automatically sanitizes timeline timestamps and dynamically constructs localized workspace tabs ordered chronologically by operational month.

### 2. Executive Metric Anchors (KPI Blocks)
* Real-time compilation of macro indicators including **Gross Revenue Contribution (EUR)**, **Captured Settlement Volume**, and **Distinct Active Account Profiles**.

### 3. Visual Analysis Engines
* **Seasonal Volatility Trajectory:** Dynamically pivots between an aggregate macro seasonal revenue analysis and a daily micro chronological trend line based on the selected workspace target.
* **Peak Distribution Chronology:** Maps hourly transaction occurrences across a 24-hour matrix to identify high-density consumer activity windows.
* **Preferred Client Settlement Profiles (Pie Chart):** Utilizes a sophisticated categorical color mapping to isolate payment mechanism frequencies (`Cash Down`, `Mastercard`, `Credit Line`) via high-contrast angular proportion models.
* **Operational Domain Concentration:** Tracks gross fiscal distributions across multi-tier retail business vertical classifications.
* **Elite Spenders Hierarchy (VIP Leaderboard):** A programmatic leaderboard that ranks customers by aggregate spending volume, with algorithmic filtering to exclude internal data anomalies or anonymous logs (e.g., `Random`, `Null`).

<img width="1200" height="412" alt="image" src="https://github.com/user-attachments/assets/ca9b91a8-97aa-483b-ae37-59d210871575" />
<img width="1267" height="631" alt="image" src="https://github.com/user-attachments/assets/b5678475-7da8-4799-949f-5716f94f80ec" />

### 4. Supplementary Deep Dives (Extended Panel)
* **High-Demand Product Logistics:** A volume-centric bar distribution analyzing the top 10 physical inventory articles by quantity units moved.
* **Average Ticket Size Contribution (Category AOV Breakdown):** Calculates the true mathematical average order value ($\text{AOV} = \frac{\text{Gross Revenue}}{\text{Transaction Volume}}$) isolated by operational vertical to pinpoint high-yield consumer baskets.

<img width="1268" height="497" alt="image" src="https://github.com/user-attachments/assets/1decf27a-ccd1-4075-a9a5-e0206d19de7f" />

---

## 🎨 Design Philosophy & UX Architecture

The user interface implements a **Minimalist Luxury Theme** styled with fluid CSS structural tokens:
* **Color Grid:** Built using a high-contrast palette comprising *Obsidian Charcoal* (`#1c1a17`), *Brushed Gold* (`#b89047`), and *Warm Taupe* (`#706c64`) set against an open layout canvas.
* **Performance:** Leverages GPU-accelerated standard cubic-bezier scaling transitions (`cubic-bezier(0.25, 1, 0.5, 1)`) for all tab navigation and UI state shifts.
* **Responsiveness:** Fluid grid-flexbox hybrid structural framework that scales natively across multi-resolution displays and desktop monitoring systems.

---

## 🛠️ Technology Stack & Dependencies

* **Frontend Kernel:** HTML5 Semantics, Vanilla EcmaScript (ES6+), Native DOM Manipulation API.
* **Styling Core:** CSS3 Custom Properties (Variables) & CSS Grid Matrix Layouts.
* **Data Stream Streamlining:** [PapaParse v5.4.1](https://www.papaparse.com/) via CDN (Asynchronous, streaming chunk-by-chunk raw string file processor).
* **Graphic Mechanics:** [Chart.js v4.x](https://www.chartjs.org/) via CDN (HTML5 Canvas vector rendering engine).

---

## 📁 Data Schema Mapping Specification

The ingestion pipeline features adaptive key matching to support varied database structural exports. For optimal chart populating, standard data files should provide columns approximating the following relational definitions:

| Primary Header Field | Expected Data Matrix Type | Fallback/Alias Handlers |
| :--- | :--- | :--- |
| `Purchase_ID` | String / Token UUID | `order_id`, `id` |
| `Purchase_Date` | Timestamp (`MM/DD/YYYY HH:MM`) | `Timestamp`, `Order_Date`, `date` |
| `Total_Amount` | Numeric Float / Float64 | `Revenue`, `amount`, `Total_Sale`, `total` |
| `Quantity` | Numeric Integer | `quantity`, `Qty` |
| `Payment_Method` | Category Token Code (`CD`, `MC`, `CR`) | `payment`, `Payment` |
| `Category_Name` | String Classification Name | `Category`, `Merchant_Type` |
| `Stock_Name` | Product Description Text | `Product`, `Item_Description` |
| `First_Name` | Text Representation String | `Customer_Name`, `Client` |

---

## 🚀 Getting Started

Because the application relies exclusively on high-performance client-side browser processing, there is no requirement for Node.js runtimes, compilation tools, or complex webserver routing.

### Local Deployment
1. Clone the repository to your environment:
   ```bash
   git clone [https://github.com/your-username/aura-intelligence-suite.git](https://github.com/your-username/aura-intelligence-suite.git)
