import { useState } from "react";
import Hero from "./components/Hero";
import About from "./components/About";
import Experience from "./components/Experience";
import Education from "./components/Education";
import Footer from "./components/Footer";
import { content } from "./data";
import "./App.css";

export default function App() {
  const [lang, setLang] = useState("pt");
  const data = content[lang];

  const toggleLang = () => setLang((prev) => (prev === "pt" ? "en" : "pt"));

  return (
    <div className="page">
      <Hero data={data} lang={lang} onToggleLang={toggleLang} />
      <main>
        <About data={data} />
        <Experience data={data} />
        <Education data={data} />
      </main>
      <Footer data={data} />
    </div>
  );
}
