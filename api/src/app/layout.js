import './globals.css'

export const metadata = {
  title: 'Apollo server web api',
  description: 'An api for our project blabla',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
    )
}
