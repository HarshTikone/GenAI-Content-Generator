import React, { useEffect, useState } from "react";
import { api } from "../api/api";
import { Link } from "react-router-dom";

export default function Dashboard() {
  const [projects, setProjects] = useState([]);
  const [err, setErr] = useState("");

  useEffect(() => {
    api.listProjects().then(setProjects).catch(e => setErr(e.body?.error || "Failed"));
  }, []);

  return (
    <div>
      <h2>Your Projects</h2>
      <div style={{marginBottom: 12}}>
        <Link to="/generate"><button>Create New</button></Link>
      </div>
      {err && <div className="error">{err}</div>}
      <ul>
        {projects.map(p => (
          <li key={p.id} className="project">
            <h3>{p.title}</h3>
            <small>{new Date(p.created_at).toLocaleString()}</small>
            <pre>{p.output || "No output yet"}</pre>
          </li>
        ))}
      </ul>
    </div>
  );
}
