// const colors = [
//   "rgba(235, 0, 0, 0.3)",
//   "rgba(0, 235, 0, 0.3)",
//   "rgba(0, 0, 235, 0.3)",
//   "rgba(238, 175, 0, 0.3)",
// ];
// const prepareChartData = () => {
//   let color = "rgba(0, 0, 0, 0.3)";
//   if (nextColor < colors.length) {
//     color = colors[nextColor];
//     setNextColor(nextColor + 1);
//   }
// const chartData = {
//     labels: ["Jan", "Feb", "Mar"],
//     datasets: [{ label: "Meter Usage", data: [5, 2, 1] }],
//     backgroundColor: color
//   };
//   return chartData;
// };
import { AWAITING, REJECTED, SUCCESS } from "./MeterAction";

const initialState = {};
const meterReducer = (state = initialState, action) => {
  const { type, payload } = action;
  switch (type) {
    case AWAITING:
      return {
        ...state,
        status: type,
      };
    case REJECTED:
      return {
        ...state,
        status: type,
      };
    case SUCCESS:
      return {
        ...state,
        status: type,
        data: {
          labels: payload.labels,
          datasets: [
            {
              data: payload.data,
              label: payload.dataLabel,
            },
          ],
        },
      };
    default:
      return state;
  }
};

export default meterReducer;
