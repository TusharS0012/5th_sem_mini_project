import React from "react";
function Body() {
  return (
    <div className="bg-white min-h-full min-w-full">
      <div className="">
        <script
          type="module"
          src="https://prod-apnortheast-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js"
        ></script>
        <tableau-viz
          id="tableau-viz"
          src="https://prod-apnortheast-a.online.tableau.com/t/sakshii0112-5e668877b3/views/AccountEngagement/AccountEngagement"
          width="1330"
          height="680"
          toolbar="bottom"
        ></tableau-viz>
      </div>
    </div>
  );
}

export default Body;
