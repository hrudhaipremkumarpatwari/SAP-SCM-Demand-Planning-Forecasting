# SAP SCM Demand Planning & Forecasting

A Week 1 SAP Supply Chain Management project demonstrating **Demand Planning and Forecasting using SAP SCM / SAP APO concepts**, simulated monthly demand data, statistical forecasting models, forecast-accuracy evaluation, and a practical SAP Demand Planning configuration workflow.

## Project Objective

The objective of this project is to understand how demand forecasting supports supply-chain decisions and how statistical forecasts can be translated into an SAP SCM/APO Demand Planning process.

The project evaluates three forecasting approaches on the same dataset and then maps the selected model into a practical SAP planning workflow.

## Business Scenario

The simulation uses a fictional company, **BreezeMax Appliances Pvt. Ltd.**, and product **BM-15INV**, a 1.5-ton inverter room air-conditioner distributed through Hyderabad.

Air-conditioner demand was selected because it demonstrates a strong seasonal pattern. Demand generally rises during the hotter months and decreases during the monsoon and winter periods. The company-level quantities used in this repository are **simulated for educational purposes** and are not proprietary sales data.

## Dataset

- Frequency: Monthly
- Period: January 2023 to June 2025
- Total observations: 30 months
- Training period: January 2023 to December 2024
- Holdout period: January 2025 to June 2025
- Main demand drivers considered: seasonality, temperature, promotions, market growth, channel availability and customer purchasing behavior

Dataset: [`data/demand_history.csv`](data/demand_history.csv)

## Forecasting Models

### 1. Three-Month Moving Average
Uses the most recent three periods to estimate future demand. It is simple and useful for relatively stable demand but reacts slowly to strong seasonal changes.

### 2. Simple Exponential Smoothing
Uses exponential weighting with **alpha = 0.30**. It responds more strongly to recent observations than a simple average but does not explicitly model annual seasonality.

### 3. Seasonal Holt-Winters
Uses **multiplicative 12-month seasonality** with no trend component. This approach is suitable when recurring seasonal peaks increase or decrease in proportion to the overall demand level.

## Model Evaluation

The six-month holdout period was evaluated using **MAE, RMSE, MAPE and forecast bias**.

| Forecasting Model | MAE | RMSE | MAPE | Bias |
|---|---:|---:|---:|---:|
| 3-Month Moving Average | 477.32 | 578.33 | 42.73% | -477.32 |
| Simple Exponential Smoothing | 413.49 | 510.96 | 36.61% | -396.74 |
| **Seasonal Holt-Winters** | **21.71** | **24.43** | **2.59%** | **-14.95** |

### Key Finding

The **Seasonal Holt-Winters model produced the lowest MAPE at 2.59%** and performed substantially better during the summer peak. This demonstrates that forecasting-model selection should match the demand pattern rather than being based only on simplicity.

Reference outputs:
- [`results/forecast_holdout_results.csv`](results/forecast_holdout_results.csv)
- [`results/model_accuracy.csv`](results/model_accuracy.csv)

## SAP SCM / APO Demand Planning Mapping

The analytical exercise is mapped to the following SAP Demand Planning workflow:

```mermaid
flowchart LR
    A[Characteristics] --> B[MPOS]
    B --> C[Planning Area]
    C --> D[CVCs]
    D --> E[Historical Data]
    E --> F[Planning Book and Data View]
    F --> G[Forecast Profile]
    G --> H[SDP94 Forecast]
    H --> I[Error Review]
    I --> J[Business Overrides]
    J --> K[Final Forecast]
    K --> L[Release to Supply Planning]
```

Important SAP APO concepts covered in the report include:

- Master Planning Object Structure (MPOS)
- Planning Area and Key Figures
- Characteristic Value Combinations (CVCs)
- Historical-demand loading
- Planning Books and Data Views
- Forecast Profiles
- Interactive Demand Planning
- Forecast-error review
- Manual adjustments and consensus planning
- Final forecast release to downstream supply planning

Transactions referenced include `/SAPAPO/MSDP_ADMIN`, `/SAPAPO/MC62`, `/SAPAPO/SDP8B`, `/SAPAPO/MC96B` and `/SAPAPO/SDP94`.

Detailed workflow: [`docs/sap_dp_workflow.md`](docs/sap_dp_workflow.md)

## Repository Structure

```text
SAP-SCM-Demand-Planning-Forecasting/
├── Hrudhai_Week1_SAP_SCM_Demand_Planning_Forecasting_Report.docx
├── README.md
├── requirements.txt
├── data/
│   └── demand_history.csv
├── docs/
│   └── sap_dp_workflow.md
├── results/
│   ├── forecast_holdout_results.csv
│   └── model_accuracy.csv
└── src/
    └── forecast_analysis.py
```

## Run the Forecasting Simulation

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
python src/forecast_analysis.py
```

The script reads the simulated demand history, trains the three forecasting approaches, evaluates the six-month holdout period, prints the accuracy metrics, and generates reproducible result CSV files.

## Report

The complete Word report contains the demand-planning theory, business scenario, forecasting methodology, simulated data, model comparison, visual analysis, SAP SCM/APO implementation steps, configuration checklist, risk controls, forecast governance recommendations and conclusions.

**Report file:** [`Hrudhai_Week1_SAP_SCM_Demand_Planning_Forecasting_Report.docx`](Hrudhai_Week1_SAP_SCM_Demand_Planning_Forecasting_Report.docx)

## Skills Demonstrated

`SAP SCM` · `SAP APO` · `Demand Planning` · `Forecasting` · `Supply Chain Planning` · `MPOS` · `CVC` · `Planning Area` · `SDP94` · `Moving Average` · `Exponential Smoothing` · `Holt-Winters` · `MAPE` · `MAE` · `RMSE` · `Python` · `Pandas` · `Statsmodels`

## Disclaimer

This repository is an **educational project and simulation**. The business name, SKU and company-level demand quantities are fictional/simulated. Public industry information is used only to support realistic assumptions about market growth and seasonality. This repository does not contain confidential or proprietary SAP/customer data.
