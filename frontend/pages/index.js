import { useState, useEffect } from 'react';

export default function Home() {
    const [stocks, setStocks] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [symbol, setSymbol] = useState("");
    const [watchlist, setWatchlist] = useState([]);

  useEffect(() => {
    fetch("/api/watchlist")
      .then((res) => res.json())
      .then(setWatchlist);
  }, []);

  const addStock = () => {
    fetch(`/api/watchlist/add?symbol=${symbol}`, { method: "POST" })
      .then(() => setWatchlist([...watchlist, symbol]))
      .then(() => setSymbol(""));
  };

  const removeStock = (symbol) => {
    fetch(`/api/watchlist/remove?symbol=${symbol}`, { method: "DELETE" })
      .then(() => setWatchlist(watchlist.filter((s) => s !== symbol)));
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Theo dõi cổ phiếu</h1>
      <div className="flex space-x-2 mt-4">
        <input
          className="border p-2 rounded"
          value={symbol}
          onChange={(e) => setSymbol(e.target.value.toUpperCase())}
          placeholder="Nhập mã cổ phiếu..."
        />
        <button className="bg-blue-500 text-white p-2 rounded" onClick={addStock}>
          Thêm
        </button>
      </div>

      <table className="mt-6 w-full border-collapse border border-gray-300">
        <thead>
          <tr className="bg-gray-200">
            <th className="border p-2">Mã</th>
            <th className="border p-2">Giá lịch sử</th>
            <th className="border p-2">Giao dịch phút</th>
            <th className="border p-2">Công ty</th>
            <th className="border p-2">Báo cáo tài chính</th>
            <th className="border p-2">Cổ tức</th>
            <th className="border p-2">Nước ngoài</th>
            <th className="border p-2">Tự doanh</th>
            <th className="border p-2">Tin tức</th>
            <th className="border p-2">Xóa</th>
          </tr>
        </thead>
        <tbody>
          {watchlist.map((symbol) => (
            <tr key={symbol} className="text-center">
              <td className="border p-2">{symbol}</td>
              <td className="border p-2"><a href={`/data/${symbol}/stock_historical_data.json`} className="text-blue-500">🔗</a></td>
              <td className="border p-2"><a href={`/data/${symbol}/stock_intraday_data.json`} className="text-blue-500">🔗</a></td>
              <td className="border p-2"><a href={`/data/${symbol}/company_overview.json`} className="text-blue-500">🔗</a></td>
              <td className="border p-2"><a href={`/data/${symbol}/financial_report.json`} className="text-blue-500">🔗</a></td>
              <td className="border p-2"><a href={`/data/${symbol}/stock_dividend.json`} className="text-blue-500">🔗</a></td>
              <td className="border p-2"><a href={`/data/${symbol}/stock_foreign_trading.json`} className="text-blue-500">🔗</a></td>
              <td className="border p-2"><a href={`/data/${symbol}/stock_proprietary_trading.json`} className="text-blue-500">🔗</a></td>
              <td className="border p-2"><a href={`/data/${symbol}/stock_news.json`} className="text-blue-500">🔗</a></td>
              <td className="border p-2">
                <button className="bg-red-500 text-white p-1 rounded" onClick={() => removeStock(symbol)}>X</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}    

    useEffect(() => {
        fetch('http://localhost:8000/stocks')  // Thay đổi URL nếu backend chạy trên cổng khác
            .then(res => {
                if (!res.ok) {
                    throw new Error('Failed to fetch stock data');
                }
                return res.json();
            })
            .then(data => {
                setStocks(data);
                setLoading(false);
            })
            .catch(err => {
                setError(err.message);
                setLoading(false);
            });
    }, []);

    return (
        <div>
            <h1>Stock Market Tracking</h1>
            
            {loading && <p>Loading data...</p>}
            {error && <p style={{ color: 'red' }}>Error: {error}</p>}

            <ul>
                {stocks.map(stock => (
                    <li key={stock.symbol}>
                        {stock.company_name} ({stock.symbol})
                    </li>
                ))}
            </ul>
        </div>
    );
}
