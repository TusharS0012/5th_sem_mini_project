import { Search } from "lucide-react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

function NavBar() {
  const [searchTerm, setSearchTerm] = useState("");
  const navigate = useNavigate();

  const handleSearch = () => {
    if (searchTerm.toLowerCase() === "reports") {
      navigate("/Reports");
    } else if (searchTerm.toLowerCase() === "settings") {
      navigate("/Settings");
    } else {
      alert("Page not found");
    }
  };

  return (
    <div className="navbar flex flex-row items-center justify-between p-4 bg-white shadow-md">
      <div className="flex flex-row gap-2">
        <input
          type="text"
          placeholder="Search..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              handleSearch();
            }
          }}
          className="searchbar rounded-lg border border-yellow-300 p-3 text-gray-800 font-semibold focus:outline-none focus:ring-2 focus:ring-yellow-500"
        />
        <Search
          className="text-yellow-500 mt-3 cursor-pointer hover:text-yellow-400 transition-colors"
          onClick={handleSearch}
        />
      </div>
      <div className="text-orange-500 text-3xl mr-4 font-bold">
        Dotanalytics
      </div>
    </div>
  );
}

export default NavBar;
