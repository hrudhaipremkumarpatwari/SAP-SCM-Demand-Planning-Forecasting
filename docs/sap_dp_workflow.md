# SAP SCM/APO Demand Planning Workflow

This note maps the project simulation to a practical SAP APO Demand Planning process.

```mermaid
flowchart LR
    A[Define Characteristics] --> B[Create MPOS]
    B --> C[Create Planning Area]
    C --> D[Create CVCs]
    D --> E[Load Historical Demand]
    E --> F[Create Planning Book and Data View]
    F --> G[Configure Forecast Profile]
    G --> H[Run Forecast in SDP94]
    H --> I[Review Forecast Errors]
    I --> J[Apply Controlled Overrides]
    J --> K[Approve Final Forecast]
    K --> L[Release to Supply Planning]
```

## Configuration Mapping

| Step | SAP Object / Transaction | Project Use |
|---|---|---|
| 1 | Characteristics | Product, Location, Region, Channel |
| 2 | `/SAPAPO/MSDP_ADMIN` | Create and activate MPOS |
| 3 | `/SAPAPO/MSDP_ADMIN` | Create planning area and key figures |
| 4 | `/SAPAPO/MC62` | Create Characteristic Value Combinations (CVCs) |
| 5 | BW / InfoCube / data load | Load monthly historical sales |
| 6 | `/SAPAPO/SDP8B` | Create planning book and monthly data view |
| 7 | Forecast Profile | Define horizon, strategy and parameters |
| 8 | `/SAPAPO/SDP94` | Run and review interactive statistical forecast |
| 9 | Forecast error review | Compare MAPE, MAE, RMSE and bias |
| 10 | Manual adjustment / consensus | Apply justified promotions or market overrides |
| 11 | Final forecast | Save approved demand plan |
| 12 | Release | Provide demand plan to downstream supply planning |

## Key Figures Used in the Scenario

- Historical Sales
- Baseline Forecast
- Promotional Uplift
- Manual Adjustment
- Final Forecast
- Forecast Error / MAPE

## Planning Logic

The project uses 24 months of history for training and a six-month holdout period for validation. Three statistical approaches are compared before selecting the seasonal model as the baseline. Business overrides should be documented with a reason and later evaluated through Forecast Value Added (FVA) so that manual changes remain controlled and auditable.

> Note: This is an educational simulation based on SAP SCM/APO Demand Planning concepts; it does not represent a live SAP production system or proprietary company data.
