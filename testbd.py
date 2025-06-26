
import pandas as pd
from graphviz import Digraph

print("Starting the ER diagram generation...")


# Load the CSV files
try:
    table_info_df = pd.read_csv('/Users/perez.e.29/Results.csv')
    print("Loaded ImagePGDB.csv successfully.")
except Exception as e:
    print(f"Error loading EnergyDBPGDB.csv: {e}")
    exit(1)
try:
    fk_info_df = pd.read_csv('/Users/perez.e.29/Results.csv')
    print("Loaded ImagePGDB.csv successfully.")
except Exception as e:
    print(f"Error loading EnergyDBGDB.csv: {e}")
    exit(1)

    
# Create a Graphviz Digraph object
dot = Digraph(comment='ER Diagram')
print("Created Graphviz Digraph object.")
# Add nodes for each table
tables = table_info_df['table_name'].unique()
for table in tables:
    table_columns = table_info_df[table_info_df['table_name'] == table]
    label = f"{table}|"
    for _, row in table_columns.iterrows():
        column_info = f"{row['column_name']} : {row['data_type']}"
        if not pd.isnull(row['primary_key']):
            column_info += " PK"
        if not pd.isnull(row['foreign_key']):
            column_info += " FK"
        label += f"{column_info}\\l"  # Add newline character for Graphviz labels
    dot.node(table, label=label, shape='record')
    print(f"Added node for table: {table}")
# Add edges for foreign key relationships
for _, row in table_info_df.iterrows():
    if pd.isnull(row['foreign_key']) or pd.isnull(row['referenced_table']):
        continue
    dot.edge(row['table_name'], row['referenced_table'], label='')
    print(f"Added edge from {row['table_name']} to {row['referenced_table']} on column {row['foreign_key']}")
# Save the ER diagram to a file
output_file = 'er_diagram_askPGDBPROD'
dot.render(output_file, format='png')
print(f"ER diagram has been generated and saved as '{output_file}.png'.")
