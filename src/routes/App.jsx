import React from "react";
import Sidebar from "../components/sidebar";
import Navbar from "../components/navbar";
import "./App.css";
import { Outlet, useLocation } from "react-router-dom";

function App() {
  const location = useLocation();

  return (
    <div className="bg-gray-100 max-h-full max-w-full flex overflow-hidden">

      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Navbar />
        <main className="flex-1 overflow-hidden p-4">
          <Outlet />
        </main>
      </div>
    </div>
  );
}

export default App;
