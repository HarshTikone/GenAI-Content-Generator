import React from "react";
import { Link, useNavigate } from "react-router-dom";

export default function Header() {
  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  function logout() {
    localStorage.removeItem("token");
    navigate("/login");
  }

  return (
    <header className="header">
      <div className="logo"><Link to="/">SmartGen</Link></div>
      <nav>
        {token ? (
          <>
            <Link to="/generate">Generator</Link>
            <Link to="/">Dashboard</Link>
            <button onClick={logout} className="link-button">Logout</button>
          </>
        ) : (
          <>
            <Link to="/login">Login</Link>
            <Link to="/register">Register</Link>
          </>
        )}
      </nav>
    </header>
  );
}
