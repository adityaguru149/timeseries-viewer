import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import UsageViewer from "./components/UsageViewer";
import { NotFound } from "./components/common/Error";

export default function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route exact path="/" component={UsageViewer} />
          <Route component={NotFound} />
        </Switch>
      </BrowserRouter>
    </div>
  );
}
