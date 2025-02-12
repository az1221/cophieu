import { useState, useEffect } from 'react';

export default function Home() {
    const [stocks, setStocks] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

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
