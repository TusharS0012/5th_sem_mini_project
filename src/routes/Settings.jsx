import React from "react";

function Settings() {
  return (
    <div className="flex flex-col items-center justify-center min-h-full bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-gray-800 mb-4">Settings</h1>
      <div className="bg-white rounded-lg shadow-lg p-6 w-full max-w-md">
        <h2 className="text-xl font-semibold mb-4">User Settings</h2>
        {/* Add your settings form or options here */}
        <p className="text-gray-600">Manage your account settings here.</p>
      </div>
    </div>
  );
}

export default Settings;
