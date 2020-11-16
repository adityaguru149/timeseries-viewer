import React, { useState } from "react";
import Datetime from 'react-datetime';
import "react-datetime/css/react-datetime.css";
import { Line } from "react-chartjs-2";
import { useSelector, useDispatch } from "react-redux";
import { getData, AWAITING } from "../state_mgmt/MeterAction";

export default function UsageViewer(props) {
  const [date, setDate] = useState(Date.UTC(2019, 0, 15, 7, 45, 0)); // 2019-01-15-07-45-00
  const [numData, setNumData] = useState(10);
  const [tick, setTick] = useState("15min");
  const meterChart = useSelector((state) => state.meterChart);
  const dispatch = useDispatch();
  const getMeterData = () => {
    dispatch(getData({ start: date, limit: numData, precision: tick }));
  };

  return (
    <div>
      <span>
        <label>Start Date:</label>
        <Datetime
          dateFormat="y-MM-DD"
          timeFormat="h:mm a"
          utc={true}
          onChange={setDate}
          value={date}
          // style={{display:"inline-block"}}
        />
      </span>
      <span>
        <label>Number of DataPoints:</label>
        <input
          onChange={(event) => {
            setNumData(event.target.value);
          }}
          value={numData}
        />
      </span>
      <span>
        <label>Precision:</label>
        <input onChange={(event) => setTick(event.target.value)} value={tick} />
      </span>
      <button onClick={getMeterData}>Go</button>

      {meterChart.status === AWAITING ? (
        <p>Loading...</p>
      ) : (
        <div id="chart">
          <Line data={meterChart.data} />
        </div>
      )}
    </div>
  );
}
