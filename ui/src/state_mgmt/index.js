import { createStore, applyMiddleware, combineReducers } from "redux";
import thunk from "redux-thunk";
import meterReducer from "./MeterReducer";

const rootReducer = combineReducers({
  meterChart: meterReducer,
});

const store = createStore(rootReducer, applyMiddleware(thunk));

export { store };
