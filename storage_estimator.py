storage_gb = float(input("Enter storage in GB: "))

storage_mb = storage_gb * 1024
storage_kb = storage_mb * 1024
storage_bytes = storage_kb * 1024

print("\n--- Storage Estimator Results ---")
print("Storage in GB:", round(storage_gb, 2))
print("Storage in MB:", round(storage_mb, 2))
print("Storage in KB:", round(storage_kb, 2))
print("Storage in bytes:", round(storage_bytes, 2))
