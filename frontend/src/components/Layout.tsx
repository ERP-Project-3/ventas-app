import { Link, Outlet } from 'react-router-dom'

export default function Layout() {
  return (
    <>
      <nav style={{ padding: '1rem', background: '#eee' }}>
        <Link to="/ventas" style={{ marginRight: '1rem' }}>Ventas</Link>
        <Link to="/cobranzas" style={{ marginRight: '1rem' }}>Cobranzas</Link>
        <Link to="/crm">CRM</Link>
      </nav>
      <section style={{ padding: '2rem' }}>
        <Outlet />
      </section>
    </>
  )
}
