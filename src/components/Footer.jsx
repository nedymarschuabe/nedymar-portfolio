import { profile } from "../data";

export default function Footer() {
  return (
    <footer className="footer">
      <p>
        © {new Date().getFullYear()} {profile.name} ·{" "}
        <a href={profile.github} target="_blank" rel="noreferrer">
          github.com/nedymarschuabe
        </a>
      </p>
    </footer>
  );
}
