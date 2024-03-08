import delta_sharing
import pandas

share_file_path = 'data/config.share'
 
# Create a SharingClient
client = delta_sharing.SharingClient(share_file_path)
 
# List all shared tables.

shares = client.list_shares()
 
for share in shares:
  schemas = client.list_schemas(share)
  for schema in schemas:
    tables = client.list_tables(schema)
    for table in tables:
      print(f'name = {table.name}, share = {table.share}, schema = {table.schema}')
      share_last = table.share
      schema_last = table.schema
      table_last = table.name

# Download the last table and save it as CSV
table_url = f"{share_file_path}#{share_last}.{schema_last}.{table_last}"
print(table_url)

# Use delta sharing client to load data
pandas_df = delta_sharing.load_as_pandas(table_url)
pandas_df.to_csv(f"downloads/{share_last}-{schema_last}-{table_last}.csv")