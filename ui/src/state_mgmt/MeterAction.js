import axios from "axios";

export const AWAITING = "AWAITING_METER";
export const SUCCESS = "SUCCESS_METER";
export const REJECTED = "REJECTED_METER";
export const getData = ({ start, limit = 10, precision }) => async (
  dispatch
) => {
  try {
    dispatch({
      type: AWAITING,
    });

    // TODO: multi-location support
    const dataLabel = "Building 1";
    // TODO: move this out to env
    const rest_url = "http://localhost:8000";

    const payload = { start: start, limit: limit, precision: precision };
    const response = await axios.post(`${rest_url}/meter/query`, payload);

    const { data, labels } = response.data;

    dispatch({
      type: SUCCESS,
      payload: {
        data,
        labels,
        dataLabel,
      },
    });
  } catch (e) {
    dispatch({
      type: REJECTED,
    });
  }
};
