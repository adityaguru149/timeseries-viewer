import React, { useState } from "react";
import DateTimePicker from "react-datetime-picker";
import { Line } from "react-chartjs-2";
import { useSelector, useDispatch } from "react-redux";
import { getData, AWAITING } from "../state_mgmt/MeterAction";

export default function UsageViewer(props) {
  const [date, setDate] = useState(Date.UTC(2019, 1, 31, 7, 45, 0));
  const [numData, setNumData] = useState(10);
  const [tick, setTick] = useState("15min");
  const meterChart = useSelector((state) => state.meterChart);
  const dispatch = useDispatch();
  const getMeterData = () => {
    dispatch(getData({ start: date, limit: numData, precision: tick }));
  };

  // const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;

  return (
    <div>
      <span>
        <label>Start Date:</label>
        <DateTimePicker
          format="y-MM-dd h:mm a"
          maxDetail="minute"
          clearIcon={null}
          onChange={setDate}
          value={date}
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
