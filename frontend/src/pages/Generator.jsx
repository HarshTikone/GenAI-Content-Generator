import React, { useState } from "react";
import { api } from "../api/api";
import { useNavigate } from "react-router-dom";

export default function Generator() {
  const [prompt, setPrompt] = useState("");
  const [out, setOut] = useState("");
  const [loading, setLoading] = useState(false);
  const [params, setParams] = useState({ max_length: 200, temperature: 0.9, top_k: 40, num_return_sequences: 1 });
  const [err, setErr] = useState("");
  const navigate = useNavigate();

  async function submit(e) {
    e.preventDefault();
    setErr("");
    setLoading(true);
    try {
      const res = await api.generate(prompt, params, "Generated content");
      setOut(res.outputs.join("\n\n---\n\n"));
      navigate("/");
    } catch (e) {
      setErr(e.body?.error || "Generation failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="card">
      <h2>Generate Content</h2>
      <form onSubmit={submit}>
        <label>Prompt<textarea value={prompt} onChange={e=>setPrompt(e.target.value)} rows={6} /></label>
        <div className="param-row">
          <label>Max Length<input type="number" value={params.max_length} onChange={e=>setParams({...params, max_length: Number(e.target.value)})} /></label>
          <label>Temperature<input type="number" step="0.1" value={params.temperature} onChange={e=>setParams({...params, temperature: Number(e.target.value)})} /></label>
          <label>Top K<input type="number" value={params.top_k} onChange={e=>setParams({...params, top_k: Number(e.target.value)})} /></label>
          <label>Return Seq<input type="number" value={params.num_return_sequences} onChange={e=>setParams({...params, num_return_sequences: Number(e.target.value)})} /></label>
        </div>
        <button type="submit" disabled={loading}>{loading ? "Generating..." : "Generate"}</button>
        {err && <div className="error">{err}</div>}
      </form>
      {out && <div className="output"><h3>Result</h3><pre>{out}</pre></div>}
    </div>
  );
}
