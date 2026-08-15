import Hero from "./components/Hero";
import About from "./components/About";
import Experience from "./components/Experience";
import Education from "./components/Education";
import Footer from "./components/Footer";
import "./App.css";

export default function App() {
  return (
    <div className="page">
      <Hero />
      <main>
        <About />
        <Experience />
        <Education />
      </main>
      <Footer />
    </div>
  );
}
