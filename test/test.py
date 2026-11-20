from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.data_loader import *
data = load_products()

dup_row = data[data.duplicated()]

print(dup_row)