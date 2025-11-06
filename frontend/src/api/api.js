const BASE = import.meta.env.VITE_API_BASE || "http://127.0.0.1:8000/api";
async function request(path, opts = {}) {
  const token = localStorage.getItem("token");
  const headers = opts.headers || {};
  headers["Content-Type"] = "application/json";
  if (token) headers["Authorization"] = `Bearer ${token}`;
  const res = await fetch(`${BASE}${path}`, { ...opts, headers });
  const json = await res.json().catch(() => ({}));
  if (!res.ok) throw { status: res.status, body: json };
  return json;
}

export const api = {
  register: (email, password, name) =>
    request("/auth/register", {
      method: "POST",
      body: JSON.stringify({ email, password, name })
    }),
  login: (email, password) =>
    request("/auth/login", {
      method: "POST",
      body: JSON.stringify({ email, password })
    }),
  profile: () => request("/profile"),
  generate: (prompt, params = {}, title = "Generated") =>
    request("/generate", {
      method: "POST",
      body: JSON.stringify({ prompt, params, title })
    }),
  listProjects: () => request("/projects")
};
