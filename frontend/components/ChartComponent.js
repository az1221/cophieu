import { Line } from "react-chartjs-2";

export default function ChartComponent({ data }) {
    const chartData = {
        labels: data.map(item => item.timestamp),
        datasets: [{
            label: "Stock Price",
            data: data.map(item => item.price),
            borderColor: "blue",
            borderWidth: 2,
            fill: false
        }]
    };

    return (
        <div>
            <h2>Biểu đồ giá cổ phiếu</h2>
            <Line data={chartData} />
        </div>
    );
}
