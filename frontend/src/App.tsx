import { useEffect } from "react"
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Layout from "./components/Layout"
import VentasModule from "./modules/Ventas"
import CobranzasModule from "./modules/Cobranza"
import CRMModule from "./modules/CMR"

function App() {
  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}/`)
      .then((res) => res.json())
      .then((data) => console.log("✅ Backend dice:", data.message))
      .catch(() => console.warn("❌ No se pudo conectar al backend"))
  }, [])

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Navigate to="/ventas" />} />
          <Route path="ventas" element={<VentasModule />} />
          <Route path="cobranzas" element={<CobranzasModule />} />
          <Route path="crm" element={<CRMModule />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
