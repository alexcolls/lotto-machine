import React, { useEffect } from "react";

function Web() {

  useEffect(() => {
    window.location.href = "https://soluckylotto.com";
  }, []);

  return (
    <div>
      <h2>Contact</h2>
    </div>
  );
}

export default Web;