import time
from my_utils import load_data, split_data
from processor import process_sequential, process_thread, process_multiprocessing
import os
print("Current Directory:", os.getcwd())
print("Files in Directory:", os.listdir())
from my_utils import load_data, split_data


def run_analysis(dataset, label):
    print(f"== {label} ==")
    time_seq = process_sequential(dataset)
    print(f"Sequential: {time_seq:.4f}s")

    time_thread = process_thread(dataset)
    print(f"Thread:     {time_thread:.4f}s")

    time_mp = process_multiprocessing(dataset)
    print(f"Multiproc:  {time_mp:.4f}s\n")

def main():
    path = "data/train.csv"
    df = load_data(path)

    sizes = [0.25, 0.5, 0.75, 1.0]
    for size in sizes:
        subset = split_data(df, size)
        label = f"{int(size * 100)}% Data ({len(subset)} rows)"
        run_analysis(subset, label)

if __name__ == "__main__":
    main()
