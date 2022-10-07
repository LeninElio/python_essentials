from google.cloud import bigquery

client = bigquery.Client()

# Perform a query.
QUERY = ('SELECT * FROM `amiable-way-360815.ubigeo.tabla_ubigeox`')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.name)


