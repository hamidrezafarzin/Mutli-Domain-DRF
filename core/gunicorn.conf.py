import multiprocessing

# #Number of workers (2 * CPUs + 1)
workers = multiprocessing.cpu_count() * 2 + 1
print(f"application running with {workers} workers")

# Binding address
bind = "0.0.0.0:8000"

# Log settings (optional)
# accesslog = "-" #None
# errorlog = "-"
loglevel = "info"

# Other settings (optional)
timeout = 30
