class Transformer:
    data_type = "Generic"
    version = 1.0
    author = "Data Team"

csv_transformer = Transformer()
csv_transformer.data_type = "CSV"
csv_transformer.version = 2.0
csv_transformer.author = "CSV Specialist" 
csv_transformer.delimiter = "|"  

del csv_transformer.author
del csv_transformer.version
del csv_transformer.delimiter

print(f"Data Type: {csv_transformer.data_type}")  # Output: CSV
print(f"Version: {csv_transformer.version}")      # Output: 2.0
print(f"Author: {csv_transformer.author}")        # Output: Data Team   
print(f"Delimiter: {csv_transformer.delimiter}")  # Raises AttributeError
       