# Dataset Dictionary

| Variable Name | Type | Description | Role in Paper |
|---|---|---|---|
| contract_id_hash | object | SHA-256 hash of the original contract identifier | Anonymous contract-level identifier |
| authority_id_hash | object | SHA-256 hash of the contracting authority identifier | Anonymous authority-level identifier |
| contract_year | int64 | Year of the contract lifecycle | Descriptive / control variable |
| cpv_division | object | Two-digit CPV division code | Procurement category classification |
| contract_value_band | category | Banded contract value category | Financial descriptor |
| award_value_band | category | Banded award value category | Financial descriptor |
| request_value_band | category | Banded request value category | Financial descriptor |
| linked_payments_value_band | category | Banded cumulative payment value category | Financial descriptor |
| component_contract_count | int64 | Number of contracts belonging to the same lifecycle component | Lifecycle complexity measure |
| component_chain_depth | int64 | Length of the reconstructed lifecycle chain | Lifecycle complexity measure |
| linked_payment_count_total | int64 | Total number of linked payment events | Execution activity measure |
| L1_Duration | bool | Indicator identifying unusually long observable execution trajectories based on available execution-related observations | Lifecycle monitoring indicator |
| L2_Modifications | bool | Indicator capturing post-award contractual modifications | Lifecycle monitoring indicator |
| L3_Administrative_Complexity | bool | Indicator capturing elevated administrative complexity | Lifecycle monitoring indicator |
| L4_Financial_Evolution | bool | Indicator capturing financial inconsistencies or scale deviations across lifecycle stages | Lifecycle monitoring indicator |
| L5_Composite | int64 | Composite count of observed lifecycle monitoring signals (sum of positive L1–L4 indicators) | Composite monitoring measure |

## Notes

L1–L4 represent lifecycle monitoring indicators derived from the production procurement lifecycle reconstruction pipeline.

L5 is a composite score corresponding to the number of positive lifecycle indicators observed for a given contract lifecycle.

All identifiers have been anonymized and all financial values converted into bands to support replication while minimizing re-identification risk.