
import yfinance as yf   
import os            

def fetch_data(symbol: str, start: str, end: str, out_dir: str = "data"):
    os.makedirs(out_dir, exist_ok=True)
    data = yf.download(symbol, start=start, end=end, progress=False)
    file_path = f"{out_dir}/{symbol}.csv"
    data=data.reset_index()
    data.to_csv(file_path)
    print(f"✔️  Saved {symbol} data to {file_path}")

if __name__ == "__main__":
    fetch_data("AAPL", "2023-01-01", "2025-08-01")