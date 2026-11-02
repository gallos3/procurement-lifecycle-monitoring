import pandas as pd
import numpy as np

def main():
    print("Loading anonymized dataset...")
    df = pd.read_parquet("contracts_metadata_anonymized.parquet")
    EXPECTED_N = 206143

    if len(df) != EXPECTED_N:
        raise ValueError(
            f"Unexpected dataset size. Expected {EXPECTED_N}, found {len(df)}."
        )
    total = len(df)
    
    print("Generating replication tables...")
    t1 = []
    cols = ['L1_Duration', 'L2_Modifications', 'L3_Administrative_Complexity', 'L4_Financial_Evolution']
    for col in cols:
        pos = df[col].sum()
        t1.append({'Indicator': col, 'Evaluated': total, 'Positive Finding': pos, 'Prevalence (%)': round((pos/total)*100, 1)})
    
    pd.DataFrame([{'Indicator': r['Indicator'], 'Evaluated': r['Evaluated'], 'Positive Finding': r['Positive Finding']} for r in t1]).to_csv("table_1.csv", index=False)
    pd.DataFrame([{'Indicator': r['Indicator'], 'Positive Finding': r['Positive Finding'], 'Prevalence (%)': r['Prevalence (%)']} for r in t1]).to_csv("table_2.csv", index=False)
    
    print("Generating Table 3...")
    t3 = df['L5_Composite'].value_counts().sort_index().reset_index()
    t3.columns = ['Findings', 'Count']
    t3['Percentage (%)'] = (t3['Count'] / total * 100).round(1)
    t3.to_csv("table_3.csv", index=False)
    
    print("Generating Table 4...")
    overlaps = []
    for i in range(len(cols)):
        for j in range(i+1, len(cols)):
            intersect = (df[cols[i]] & df[cols[j]]).sum()
            union = (df[cols[i]] | df[cols[j]]).sum()
            jaccard = round((intersect / union * 100), 1) if union > 0 else 0.0
            overlaps.append({
                'Indicator 1': cols[i], 
                'Indicator 2': cols[j], 
                'Overlap Count': intersect,
                'Jaccard Overlap (%)': jaccard
            })
    
    df_overlaps = pd.DataFrame(overlaps).sort_values(by='Overlap Count', ascending=False)
    df_overlaps.to_csv("table_4.csv", index=False)
    
    print("Exporting Excel...")
    with pd.ExcelWriter("publication_tables.xlsx") as writer:
        pd.DataFrame(t1).drop(columns=['Prevalence (%)']).to_excel(writer, sheet_name="Table 1", index=False)
        pd.DataFrame(t1).drop(columns=['Evaluated']).to_excel(writer, sheet_name="Table 2", index=False)
        t3.to_excel(writer, sheet_name="Table 3", index=False)
        df_overlaps.to_excel(writer, sheet_name="Table 4", index=False)
        
    print("Tables generated successfully.")
    print("Table 4 with Jaccard overlap successfully generated.")

if __name__ == "__main__":
    main()
