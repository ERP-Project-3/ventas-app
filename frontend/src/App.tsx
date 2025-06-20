import { useEffect, useState } from "react"

function App() {
  const [mensaje, setMensaje] = useState("Cargando...")

  useEffect(() => {
  fetch(`${import.meta.env.VITE_API_URL}/`)
    .then((res) => res.json())
    .then((data) => setMensaje(data.message))
    .catch(() => setMensaje("No se pudo conectar al backend"));
  }, []);

  return (
    <main style={{ padding: "2rem", textAlign: "center" }}>
      <h1>Registro de Ventas</h1>
      <p>{mensaje}</p>
    </main>
  )
}

export default App
