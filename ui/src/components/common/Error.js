import React from "react";
import { Link } from "react-router-dom";

export function NotFound() {
  return (
    <div>
      <h2>Not Found</h2>
      {/* Need to cater access issues? */}
      <p>
        <Link to="/">Back to Home</Link>
      </p>
    </div>
  );
}
