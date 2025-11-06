import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../api/api";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [err, setErr] = useState("");
  const navigate = useNavigate();

  async function submit(e) {
    e.preventDefault();
    setErr("");
    try {
      const res = await api.login(email, password);
      localStorage.setItem("token", res.token);
      navigate("/");
    } catch (e) {
      setErr(e.body?.error || "Login failed");
    }
  }

  return (
    <div className="card">
      <h2>Login</h2>
      <form onSubmit={submit}>
        <label>Email<input value={email} onChange={e=>setEmail(e.target.value)} /></label>
        <label>Password<input type="password" value={password} onChange={e=>setPassword(e.target.value)} /></label>
        <button type="submit">Login</button>
        {err && <div className="error">{err}</div>}
      </form>
    </div>
  );
}
